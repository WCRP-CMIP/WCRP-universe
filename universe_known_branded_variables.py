#!/usr/bin/env python3
"""Generate CMIP7 known branded variables from the CMIP7 Data Request.

The script extracts branded variables from the DReq "Variables" table and
serialises them as JSON objects compliant with the KnownBrandedVariable
Pydantic model.

Output is one JSON file per branded variable in the output directory:

known_branded_variables/ta_tavg-p19-hxy-air.json

Each file contains one KnownBrandedVariable object with a JSON-LD context and
an explicit id matching the file stem.
"""

from __future__ import annotations

import argparse
import json
import re
from pprint import pprint
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field, ValidationError

import data_request_api.content.dreq_content as dc
import data_request_api.query.dreq_query as dq

DEFAULT_VERSION = "v1.2.2.5rc"
DEFAULT_OUTPUT_DIR = "known_branded_variable"
CONTEXT_FILE = "000_context.jsonld"

REGION_MAPPING = {
    "nh": "northern-hemisphere",
    "grl": "greenland",
    "sh": "southern-hemisphere",
    "ata": "antarctica",
    "glb": "global",
    "30S-90S": "30s-90s",
}

GRID_COORDINATE_NAMES = {"latitude", "longitude"}

LONG_NAME_MAPPING = {
    "siarea_tavg-u-hm-u": "Sea-Ice Area",
    "siextent_tavg-u-hm-u": "Sea-Ice Extent",
    "sisnmass_tavg-u-hm-si": "Snow Mass on Sea Ice",
    "sivol_tavg-u-hm-u": "Sea-Ice Volume",
}

class KnownBrandedVariable(BaseModel):
    """
    A climate-related quantity or measurement, including information about sampling.

    The concept of a branded variable was introduced in CMIP7.
    A branded variable is composed of two parts.
    The first part is the root variable (see :py:class:`Variable`).
    The second is the suffix (see :py:class:`BrandingSuffix`).

    For further details on the development of branded variables,
    see [this paper draft](https://docs.google.com/document/d/19jzecgymgiiEsTDzaaqeLP6pTvLT-NzCMaq-wu-QoOc/edit?pli=1&tab=t.0).
    """

    id: str = Field(description="Branded variable identifier, same as JSON file stem")
    type: str = Field(description="Branded variable type, always 'known_branded_variable'")
    drs_name: str = Field(description="DRS name, same as id")

    # CF Standard Name context (flattened from hierarchy)
    cf_standard_name: str = Field(description="CF standard name, e.g., 'air_temperature'")
    cf_units: str = Field(description="CF standard units, e.g., 'K'")

    # Variable Root context (flattened from hierarchy)
    variable_root_name: str = Field(description="Variable root name, e.g., 'ta'")
    branding_suffix_name: str = Field(description="Branding suffix, e.g., 'tavg-p19-hxy-air'")

    # Variable metadata
    long_name: str = Field(description="Long name from the DR variable title")
    physical_parameter: str = Field(description="Physical parameter")
    description: str | list[str] | None = Field(description="Variable description(s)")
    data_type: str = Field(description="Data type")
    cmor_dimensions: list[str] = Field(description="dimensions field used in CMOR tables")
    shape_coordinates: list[str] = Field(description="Coordinates that define the array shape (with exception of latitude and longitude grid coordinates and vertical parametric coordinates)")
    scalar_coordinates: list[str] = Field(default_factory=list, description="Scalar coordinates")
    grid_coordinates: list[str] = Field(default_factory=list, description="Grid coordinates - latitude and longitude")
    parametric_coordinates: list[str] = Field(default_factory=list, description="Generic vertical parametric coordinates (e.g., alevel, olevel)")
    cell_methods: str | list[str] = Field(description="CF cell_methods attribute(s)")
    cell_measures: str | list[str] | None = Field(default=None, description="CF cell_measures attribute(s)")
    realm: str | list[str] = Field(description="Earth system realms")
    region: str | list[str] = Field(description="Geographical or domain region")

    # Label components (embedded, not references)
    temporal_label: str = Field(description="Temporal label, e.g., 'tavg'")
    vertical_label: str = Field(description="Vertical label, e.g., 'p19'")
    horizontal_label: str = Field(description="Horizontal label, e.g., 'hxy'")
    area_label: str = Field(description="Area label, e.g., 'air'")

    # Additional required fields from specifications
    positive_direction: str | None = Field(default=None, description="Positive direction for the variable")

# -----------------------------------------------------------------------------
# Generic helpers
# -----------------------------------------------------------------------------

def get_attr(record: Any, key: str, default: Any = None) -> Any:
    """Return an attribute from a DR record object."""
    if record is None or key is None:
        return None
    if hasattr(record, key):
        return getattr(record, key)
    return default

def none_if_empty(value: Any) -> Any:
    if value in (None, "", []):
        return None
    return value

def str_or_default(value: Any, default: str = "") -> str:
    """Return a stable string for scalar or list-like DR values."""
    value = none_if_empty(value)
    if value is None:
        return default
    if isinstance(value, (list, tuple, set)):
        values = [str(v) for v in value if v not in (None, "")]
        return " ".join(values) if values else default
    return str(value)

def str_list_or_empty(value: Any) -> list[str]:
    """Return a list of cleaned strings from scalar or list-like values."""
    value = none_if_empty(value)
    if value is None:
        return []
    if isinstance(value, (list, tuple, set)):
        raw_values = list(value)
    else:
        raw_values = [value]

    result: list[str] = []
    for raw_value in raw_values:
        text = clean_str(str_or_default(raw_value))
        if text and text not in result:
            result.append(text)
    return result

def clean_str(value: str) -> str:
    """Remove DR/LaTeX-like escaping that is not useful in JSON strings."""
    # Keep real JSON escaping handled by json.dump, but remove source-level
    # backslash escapes such as \_, \%, \& that may appear in DReq text.
    value = re.sub(r"\\([_/%#&{}$])", r"\1", value)
    # Remove a remaining backslash before ordinary punctuation/letters when it
    # is clearly a source formatting escape, not a newline/tab escape.
    value = re.sub(r"\\(?![nrt\"\\/bfu])", "", value)
    return value

def list_or_empty(value: Any) -> list[Any]:
    value = none_if_empty(value)
    if value is None:
        return []
    if isinstance(value, (list, tuple, set)):
        return list(value)
    return [value]

def get_first_record(table: Any, links: Any) -> Any | None:
    links = list_or_empty(links)
    if not links:
        return None
    return table.get_record(links[0])

def get_linked_values(table: Any, links: Any, attr_names: tuple[str, ...]) -> list[str]:
    """Return selected attributes from all linked records, preserving order and uniqueness."""
    values: list[str] = []
    for link in list_or_empty(links):
        record = table.get_record(link)
        for attr_name in attr_names:
            value = str_or_default(get_attr(record, attr_name))
            if value:
                if value not in values:
                    values.append(value)
                break
    return values

def get_table(tables: Any, *names: str) -> Any | None:
    """Return the table from possible DR table names."""
    for name in names:
        try:
            return tables[name]
        except Exception:  # noqa: BLE001 - DReq table accessor may raise different errors.
            continue
    return None

def get_coordinate_name(coord_record: Any) -> str:
    """Return the DReq coordinate record name used as coordinate JSON identifier."""
    return str_or_default(get_attr(coord_record, "name"))


def append_unique(values: list[str], incoming: str) -> None:
    value = clean_str(str_or_default(incoming)).strip()
    if value and value not in values:
        values.append(value)


def parse_dimension_tokens(value: Any) -> list[str]:
    """Return dimension-like tokens from DR values preserving order and uniqueness."""
    tokens: list[str] = []
    if value in (None, "", []):
        return tokens

    if isinstance(value, str):
        raw_tokens = re.split(r"[,\s]+", value)
        for raw in raw_tokens:
            append_unique(tokens, raw)
        return tokens

    for item in list_or_empty(value):
        if isinstance(item, str):
            for raw in re.split(r"[,\s]+", item):
                append_unique(tokens, raw)
        else:
            append_unique(tokens, str(item))
    return tokens


def resolve_dimension_name(coordinates: Any, token: Any) -> str:
    """Resolve a dimensions token to its DReq coordinate/dimension name when possible."""
    text = clean_str(str_or_default(token)).strip()
    if not text:
        return ""

    def get_name_from_record_id(record_id: str) -> str | None:
        try:
            record = coordinates.get_record(record_id)
        except Exception:  # noqa: BLE001 - unknown or malformed record id.
            return None
        name = get_coordinate_name(record)
        return name or None

    try:
        record = coordinates.get_record(token)
    except Exception:  # noqa: BLE001 - token can already be a plain dimension name.
        if "record=" in text:
            record_id = text.split("record=", 1)[1].strip()
            record_id = re.split(r"[,\s]+", record_id)[0]
            resolved_name = get_name_from_record_id(record_id)
            if resolved_name:
                return resolved_name
        return text
    name = get_coordinate_name(record)
    return name or text


def get_coordinate_record_by_name(coordinates: Any, name: str) -> Any | None:
    """Return a coordinate/dimension record by name when available."""
    try:
        return coordinates.get_attr_record("name", name, unique=True)
    except Exception:  # noqa: BLE001 - some names may not have a unique/available record.
        return None


def get_coordinate_attr_by_name(coordinates: Any, name: str, attr_name: str) -> str:
    record = get_coordinate_record_by_name(coordinates, name)
    return str_or_default(get_attr(record, attr_name)).strip()


def classify_coordinate_name(name: str, grid_class: str, cf_category: str) -> str:
    """Return target bucket for one coordinate name based on DR metadata."""
    lower_name = name.lower()
    lower_grid_class = grid_class.lower()
    lower_cf_category = cf_category.lower()

    if lower_name in GRID_COORDINATE_NAMES:
        return "grid_coordinates"
    if lower_grid_class == "fixedscalar":
        return "scalar_coordinates"
    if lower_grid_class == "options":
        return "parametric_coordinates"
    if lower_cf_category == "dimension":
        return "shape_coordinates"
    raise ValueError(
        "Unclassified coordinate in Coordinates and Dimensions table: "
        f"name={name!r}, grid_class={grid_class!r}, cf_category={cf_category!r}. "
        "Update classification rules to include this coordinate type."
    )


def build_coordinate_classification_lookup(coordinates: Any) -> tuple[dict[str, str], dict[str, list[str]]]:
    """Build one dictionary mapping coordinate name -> coordinate type."""
    by_name: dict[str, str] = {}
    coord_types: dict[str, list[str]] = {
        "scalar_coordinates": [],
        "grid_coordinates": [],
        "shape_coordinates": [],
        "parametric_coordinates": [],
    }

    for record in coordinates.records.values():
        name = get_coordinate_name(record)
        if not name:
            raise ValueError(f"Coordinate record without a name found in Coordinates and Dimensions table: {record}")
        grid_class = str_or_default(get_attr(record, "grid_class"))
        cf_category = str_or_default(get_attr(record, "cf_category"))

        coord_type = classify_coordinate_name(name, grid_class, cf_category)
        by_name[name] = coord_type
        append_unique(coord_types[coord_type], name)

    return by_name, coord_types


def classify_coordinates(
    cmor_dimensions: list[str],
    coordinate_classification_by_name: dict[str, str],
    coordinates: Any,
) -> dict[str, list[str]]:
    """Classify each CMOR dimension using a precomputed coordinate->coord_type lookup."""
    coord_types: dict[str, list[str]] = {
        "scalar_coordinates": [],
        "grid_coordinates": [],
        "shape_coordinates": [],
        "parametric_coordinates": [],
    }

    for dim in cmor_dimensions:
        coord_type = coordinate_classification_by_name.get(dim)
        if coord_type is None:
            resolved_dim = resolve_dimension_name(coordinates, dim)
            coord_type = coordinate_classification_by_name.get(resolved_dim)
        else:
            resolved_dim = dim

        if coord_type is None:
            raise ValueError(
                "CMOR dimension has no coordinate classification: "
                f"name={dim!r}, resolved_name={resolved_dim!r}. "
                "Update classification rules and/or DR mapping."
            )
        append_unique(coord_types[coord_type], resolved_dim)

    return coord_types

def add_shape_coordinate_names(result: list[str], shape_record: Any, coordinates: Any) -> None:
    """Append coordinate record names from a spatial/temporal shape record."""
    for dim_link in list_or_empty(get_attr(shape_record, "dimensions")):
        coord_record = coordinates.get_record(dim_link)
        coord_name = get_coordinate_name(coord_record)
        if coord_name and coord_name not in result:
            result.append(coord_name)

# -----------------------------------------------------------------------------
# Branded variable helpers
# -----------------------------------------------------------------------------

def split_branded_variable_name(branded_name: str) -> tuple[str, str, str, str, str]:
    """Return branding suffix and its four expected label components.

    Expected branded name pattern:
        <variable_root_name>_<temporal>-<vertical>-<horizontal>-<area>

    The function is intentionally permissive and returns empty strings for
    missing components, while printing warnings from the caller if needed.
    """
    suffix = branded_name.split("_", 1)[1]

    parts = suffix.split("-") if suffix else []
    temporal_label = parts[0] if len(parts) > 0 else ""
    vertical_label = parts[1] if len(parts) > 1 else ""
    horizontal_label = parts[2] if len(parts) > 2 else ""
    area_label = "-".join(parts[3:]) if len(parts) > 3 else ""

    return suffix, temporal_label, vertical_label, horizontal_label, area_label

def get_linked_dimensions_in_dreq_order(
    var: Any,
    spatial_shapes: Any,
    temporal_shapes: Any,
    structures: Any | None,
    coordinates: Any,
) -> list[str]:
    """Return dimensions in DR linked order: spatial, structure, temporal, coordinates."""
    dims: list[str] = []

    spatial_shape = get_first_record(spatial_shapes, get_attr(var, "spatial_shape"))
    if spatial_shape is not None:
        add_shape_coordinate_names(dims, spatial_shape, coordinates)

    if structures is not None and hasattr(var, "structure_title"):
        structure = get_first_record(structures, get_attr(var, "structure_title"))
        if structure is not None:
            for dim_link in list_or_empty(get_attr(structure, "dimensions")):
                dim_record = coordinates.get_record(dim_link)
                append_unique(dims, get_coordinate_name(dim_record))

    temporal_shape = get_first_record(temporal_shapes, get_attr(var, "temporal_shape"))
    if temporal_shape is not None:
        add_shape_coordinate_names(dims, temporal_shape, coordinates)

    for coord_link in list_or_empty(get_attr(var, "coordinates")):
        coord_record = coordinates.get_record(coord_link)
        append_unique(dims, get_coordinate_name(coord_record))

    return dims


def get_cmor_dimensions(
    var: Any,
    spatial_shapes: Any,
    temporal_shapes: Any,
    structures: Any | None,
    coordinates: Any,
) -> list[str]:
    """Return CMOR dimensions preserving DR ordering and including extra_dimensions."""
    dims: list[str] = []

    # Follow DR logic: prefer variable.dimensions when present, otherwise linked order.
    if hasattr(var, "dimensions"):
        for token in parse_dimension_tokens(get_attr(var, "dimensions")):
            append_unique(dims, resolve_dimension_name(coordinates, token))
    else:
        for dim in get_linked_dimensions_in_dreq_order(var, spatial_shapes, temporal_shapes, structures, coordinates):
            append_unique(dims, dim)

    # Append additional dimensions from explicit extra_dimension(s) fields.
    for attr_name in ("extra_dimensions", "extra_dimension"):
        if not hasattr(var, attr_name):
            continue
        for token in parse_dimension_tokens(get_attr(var, attr_name)):
            append_unique(dims, resolve_dimension_name(coordinates, token))

    return dims

def get_realms(var: Any, modelling_realms: Any | None) -> str | list[str] | None:
    """Resolve primary and secondary modelling realms from DReq links."""
    realms: list[str] = []
    for key in ("modelling_realm___primary", "modelling_realm___secondary"):
        links = get_attr(var, key)
        if modelling_realms is not None:
            values = get_linked_values(modelling_realms, links, ("id",),)
        else:
            values = [str_or_default(link) for link in list_or_empty(links)]
        for value in values:
            if value and value.lower() not in realms:
                realms.append(value.lower())
    if not realms:
        return None
    if len(realms) == 1:
        return realms[0]
    return realms

def get_region(var: Any) -> str:
    """Return region/domain information with controlled vocabulary mapping."""
    value = get_attr(var, "region")
    return REGION_MAPPING.get(value, value)

def get_long_name(var: Any, branded_name: str) -> str:
    """Return corrected long name for selected branded variables, otherwise DReq title."""
    return LONG_NAME_MAPPING.get(
        branded_name,
        LONG_NAME_MAPPING.get(
            branded_name,
            get_attr(var, "title"),
        ),
    )

def build_known_branded_variable(
    var: Any,
    spatial_shapes: Any,
    temporal_shapes: Any,
    structures: Any | None,
    coordinates: Any,
    coordinate_classification_by_name: dict[str, str],
    cell_methods: Any,
    cell_measures: Any,
    physical_parameters: Any,
    cf_standard_names: Any,
    modelling_realms: Any | None,
) -> KnownBrandedVariable:
    """Build and validate one KnownBrandedVariable from a DR variable record."""
    branded_name = str_or_default(get_attr(var, "branded_variable_name"))
    if not branded_name:
        raise ValueError("Variable record has no branded_variable_name")

    branding_suffix_name, temporal_label, vertical_label, horizontal_label, area_label = (
        split_branded_variable_name(branded_name)
    )

    assert len(get_attr(var, "cf_standard_name_from_physical_parameter")) == 1
    assert len(get_attr(var, "units_from_physical_parameter")) == 1
    assert len(get_attr(var, "physical_parameter")) == 1
    assert len(get_attr(var, "cell_methods")) == 1

    cmor_dimensions = get_cmor_dimensions(
        var,
        spatial_shapes,
        temporal_shapes,
        structures,
        coordinates,
    )
    coordinate_assignment = classify_coordinates(
        cmor_dimensions[::-1],
        coordinate_classification_by_name,
        coordinates,
    )

    payload = {
        "id": branded_name.lower(),
        "type": "known_branded_variable",
        "drs_name": branded_name,
        "cf_standard_name": get_attr(cf_standard_names.get_record(get_attr(var, "cf_standard_name_from_physical_parameter")[0]), "name"),
        "cf_units": get_attr(var, "units_from_physical_parameter")[0],
        "variable_root_name": branded_name.split("_", 1)[0],
        "branding_suffix_name": branding_suffix_name,
        "long_name": clean_str(get_long_name(var, branded_name)),
        "physical_parameter": get_attr(physical_parameters.get_record(get_attr(var, "physical_parameter")[0]), "name"),
        "description": clean_str(get_attr(var, "description")),
        "data_type": get_attr(var, "type"),
        "cmor_dimensions": cmor_dimensions,
        "shape_coordinates": coordinate_assignment["shape_coordinates"],
        "scalar_coordinates": coordinate_assignment["scalar_coordinates"],
        "grid_coordinates": coordinate_assignment["grid_coordinates"],
        "parametric_coordinates": coordinate_assignment["parametric_coordinates"],
        "cell_methods": get_attr(cell_methods.get_record(get_attr(var, "cell_methods")[0]), "cell_methods"),
        "cell_measures": (get_attr(cell_measures.get_record(get_attr(var, "cell_measures")[0]),"name",) if get_attr(var, "cell_measures") else None),
       "realm": get_realms(var, modelling_realms),
        "region": get_region(var),
        "temporal_label": temporal_label,
        "vertical_label": vertical_label,
        "horizontal_label": horizontal_label,
        "area_label": area_label,
        "positive_direction": get_attr(var, "positive_direction"),
    }

    return KnownBrandedVariable(**payload)

def values_equal(left: Any, right: Any) -> bool:
    return left == right

def unique_strings(values: list[Any]) -> list[str]:
    """Flatten values and return unique string values preserving order."""
    result: list[str] = []
    for value in values:
        if value in (None, "", []):
            continue
        if isinstance(value, list):
            candidates = value
        else:
            candidates = [value]
        for candidate in candidates:
            if candidate in (None, ""):
                continue
            text = clean_str(str(candidate))
            if text and text not in result:
                result.append(text)
    return result

def merge_list_values(existing_value: Any, incoming_value: Any) -> list[str]:
    """Merge two list-like attributes into a unique list of strings."""
    return unique_strings([existing_value, incoming_value])

def merge_scalar_values(existing_value: Any, incoming_value: Any) -> str:
    """Merge two scalar attributes into one forced string.

    Scalar fields are not allowed to become lists in the target model. When two
    duplicate branded variables expose different scalar values, keep both values
    in one string separated by `` | `` so the output remains model-compliant.
    """
    values = unique_strings([existing_value, incoming_value])
    return " | ".join(values) if values else ""

def merge_duplicate_branded_variable(
    branded_name: str,
    existing: KnownBrandedVariable,
    incoming: KnownBrandedVariable,
) -> KnownBrandedVariable:
    """Merge duplicated branded variables and list possible differing values."""
    existing_data = model_dump_excluding_none(existing)
    incoming_data = model_dump_excluding_none(incoming)
    merged: dict[str, Any] = dict(existing_data)

    differing_keys = [
        key
        for key in sorted(set(existing_data) | set(incoming_data))
        if not values_equal(existing_data.get(key), incoming_data.get(key))
    ]

    print(f"Warning: duplicated branded variable differs and will be merged: {branded_name}")

    list_fields = {
        "description",
        "cell_methods",
        "cell_measures",
        "region",
        "realm",
        "cmor_dimensions",
        "shape_coordinates",
        "scalar_coordinates",
        "grid_coordinates",
        "parametric_coordinates",
    }

    for key in differing_keys:
        existing_value = existing_data.get(key)
        incoming_value = incoming_data.get(key)
        if key in [
           "type",
           "drs_name",
           "variable_root_name",
           "branding_suffix_name",
           "temporal_label",
           "vertical_label",
           "horizontal_label",
           "area_label"
        ]:
            raise ValueError(f"  - {key}: first={existing_value!r} duplicate={incoming_value!r}")
        if key in [
            "cf_standard_name",
            "cf_units",
            "cmor_dimensions",
            "cell_methods",
            "physical_parameter",
            "data_type"
        ] or key.endswith("coordinates"):
            print(f"  - {key}: first={existing_value!r} duplicate={incoming_value!r}")

        if key in list_fields:
            merged[key] = merge_list_values(existing_value, incoming_value)
        else:
            merged[key] = merge_scalar_values(existing_value, incoming_value)

    # Clean descriptions once more after potential list merge.
    if "description" in merged:
        merged["description"] = str_list_or_empty(merged["description"])

    return KnownBrandedVariable(**merged)

# -----------------------------------------------------------------------------
# Main extraction
# -----------------------------------------------------------------------------

def load_known_branded_variables(version: str) -> dict[str, KnownBrandedVariable]:
    dc.retrieve(version)
    content = dc.load(version)
    tables = dq.create_dreq_tables_for_request(content, version)

    variables = tables["Variables"]
    spatial_shapes = tables["Spatial Shape"]
    temporal_shapes = tables["Temporal Shape"]
    structures = get_table(tables, "Structure", "structure")
    coordinates = tables["Coordinates and Dimensions"]
    coordinate_classification_by_name, coordinate_classification_summary = build_coordinate_classification_lookup(coordinates)
    print("Overall coordinate classification:")
    pprint(coordinate_classification_summary, sort_dicts=False)
    cell_methods = tables["Cell Methods"]
    cell_measures = tables["Cell Measures"]
    physical_parameters = tables["Physical Parameters"]
    cf_standard_names = tables["CF Standard Names"]
    modelling_realms = tables["Modelling Realm"]
    result: dict[str, KnownBrandedVariable] = {}
    skipped = 0
    validation_errors = 0
    duplicate_identical = 0
    duplicate_different = 0

    for var in variables.records.values():
        branded_name = str_or_default(get_attr(var, "branded_variable_name"))
        if not branded_name:
            skipped += 1
            print("Warning: variable without branded_variable_name skipped")
            continue

        try:
            known = build_known_branded_variable(
                var,
                spatial_shapes=spatial_shapes,
                temporal_shapes=temporal_shapes,
                structures=structures,
                coordinates=coordinates,
                coordinate_classification_by_name=coordinate_classification_by_name,
                cell_methods=cell_methods,
                cell_measures=cell_measures,
                physical_parameters=physical_parameters,
                cf_standard_names=cf_standard_names,
                modelling_realms=modelling_realms,
            )
        except ValidationError as exc:
            validation_errors += 1
            print(f"Warning: validation failed for {branded_name}: {exc}")
            continue
        except Exception as exc:  # noqa: BLE001 - script should report and continue.
            validation_errors += 1
            print(f"Warning: failed to build {branded_name}: {exc}")
            continue

        if branded_name in result:
            if result[branded_name] == known:
                duplicate_identical += 1
                print(f"Info: duplicated branded variable identical, skipped: {branded_name}")
            else:
                duplicate_different += 1
                result[branded_name] = merge_duplicate_branded_variable(
                    branded_name,
                    result[branded_name],
                    known,
                )
            continue

        result[branded_name] = known

    print(f"Known branded variables written: {len(result)}")
    print(f"Variables skipped without branded name: {skipped}")
    print(f"Validation/build errors: {validation_errors}")
    print(f"Duplicated identical branded variables: {duplicate_identical}")
    print(f"Duplicated different branded variables merged: {duplicate_different}")

    return result

def model_dump_excluding_none(model: BaseModel) -> dict[str, Any]:
    if hasattr(model, "model_dump"):
        return model.model_dump(exclude_none=True)
    return model.dict(exclude_none=True)

def write_branded_variable_json_files(records: dict[str, KnownBrandedVariable], output_dir: Path) -> None:
    """Write one JSON-LD-compatible file per branded variable."""
    output_dir.mkdir(parents=True, exist_ok=True)
    for name, record in sorted(records.items()):
        output_file = output_dir / f"{name.lower()}.json"
        payload = {
            "@context": CONTEXT_FILE,
            **model_dump_excluding_none(record),
        }
        with output_file.open("w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)
            f.write("\n")
    print(f"Wrote {len(records)} files to {output_dir}")

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate one KnownBrandedVariable JSON file per CMIP7 branded variable.",
    )
    parser.add_argument("--version", default=DEFAULT_VERSION, help="DReq version")
    parser.add_argument(
        "--output-dir",
        default=DEFAULT_OUTPUT_DIR,
        help="Directory where one JSON file per branded variable will be written",
    )
    args = parser.parse_args()

    records = load_known_branded_variables(args.version)
    write_branded_variable_json_files(records, Path(args.output_dir))

if __name__ == "__main__":
    main()
