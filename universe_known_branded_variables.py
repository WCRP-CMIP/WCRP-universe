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
from pathlib import Path
from typing import Any

from pydantic import BaseModel, Field, ValidationError

import data_request_api.content.dreq_content as dc
import data_request_api.query.dreq_query as dq

DEFAULT_VERSION = "v1.2.2.4"
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

REALM_MAPPING = {
    "tas.tavg-h2m-hxy-u": "atmos",
}

LONG_NAME_MAPPING = {
    "siarea_tavg-u-hm-u": "Sea-Ice Area",
    "siarea_tavg-u-hm-u": "Sea-Ice Area",
    "siextent_tavg-u-hm-u": "Sea-Ice Extent",
    "siextent_tavg-u-hm-u": "Sea-Ice Extent",
    "sisnmass_tavg-u-hm-si": "Snow Mass on Sea Ice",
    "sisnmass_tavg-u-hm-si": "Snow Mass on Sea Ice",
    "sivol_tavg-u-hm-u": "Sea-Ice Volume",
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
    dimensions: list[str] = Field(description="NetCDF dimensions")
    shapes_coordinates: list[str] = Field(description="Coordinate record names used to define spatial and temporal shapes")
    coordinates: str = Field(default_factory=list, description="Required scalar or auxiliary coordinates")
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

def get_linked_attr(table: Any, links: Any, attr_name: str, default: str = "") -> str:
    """Return attr_name from linked records as one whitespace-separated string."""
    values: list[str] = []
    for link in list_or_empty(links):
        record = table.get_record(link)
        value = get_attr(record, attr_name)
        if value:
            values.append(value)
    return " ".join(values) if values else default

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

def get_coordinate_output_name(coord_record: Any) -> str:
    """Return the NetCDF output name used for a coordinate/dimension."""
    return (
        str_or_default(get_attr(coord_record, "output_name"))
        or str_or_default(get_attr(coord_record, "out_name"))
        or str_or_default(get_attr(coord_record, "name"))
    )

def get_coordinate_name(coord_record: Any) -> str:
    """Return the DReq coordinate record name used as coordinate JSON identifier."""
    return str_or_default(get_attr(coord_record, "name"))

def add_shape_dimensions(result: list[str], shape_record: Any, coordinates: Any) -> None:
    """Append dimensions from a spatial/temporal shape record."""
    for dim_link in list_or_empty(get_attr(shape_record, "dimensions")):
        coord_record = coordinates.get_record(dim_link)
        coord_name = get_coordinate_output_name(coord_record)
        if coord_name and coord_name not in result:
            result.append(coord_name)

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

def get_dimensions(var: Any, spatial_shapes: Any, temporal_shapes: Any, coordinates: Any) -> list[str]:
    """Return NetCDF dimensions from spatial and temporal DReq shapes."""
    dims: list[str] = []

    spatial_shape = get_first_record(spatial_shapes, get_attr(var, "spatial_shape"))
    if spatial_shape is not None:
        add_shape_dimensions(dims, spatial_shape, coordinates)

    temporal_shape = get_first_record(temporal_shapes, get_attr(var, "temporal_shape"))
    if temporal_shape is not None:
        add_shape_dimensions(dims, temporal_shape, coordinates)

    return dims

def get_coordinate_names_from_shapes(var: Any, spatial_shapes: Any, temporal_shapes: Any, coordinates: Any) -> list[str]:
    """Return DReq coordinate names from spatial and temporal DReq shapes."""
    coord_names: list[str] = []

    spatial_shape = get_first_record(spatial_shapes, get_attr(var, "spatial_shape"))
    if spatial_shape is not None:
        add_shape_coordinate_names(coord_names, spatial_shape, coordinates)

    temporal_shape = get_first_record(temporal_shapes, get_attr(var, "temporal_shape"))
    if temporal_shape is not None:
        add_shape_coordinate_names(coord_names, temporal_shape, coordinates)

    return coord_names

def get_coordinates(var: Any) -> str:
    """Return coordinate names directly from the DR Variables Coordinates column."""
    return clean_str(str_or_default(get_attr(var, "coordinates")))

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

def list_or_none(values: list[str]) -> list[str] | None:
    """Return a non-empty list, or None."""
    return values or None
    
def build_known_branded_variable(
    var: Any,
    spatial_shapes: Any,
    temporal_shapes: Any,
    coordinates: Any,
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
        "dimensions": get_dimensions(var, spatial_shapes, temporal_shapes, coordinates),
        "shapes_coordinates": get_coordinate_names_from_shapes(var, spatial_shapes, temporal_shapes, coordinates),
        "coordinates": get_coordinates(var),
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

    #print(f"Warning: duplicated branded variable differs and will be merged: {branded_name}")

    list_fields = {"description", "cell_methods", "cell_measures", "region", "realm", "dimensions", "coordinates"}

    for key in differing_keys:
        existing_value = existing_data.get(key)
        incoming_value = incoming_data.get(key)
        #print(f"  - {key}: first={existing_value!r} duplicate={incoming_value!r}")

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
    coordinates = tables["Coordinates and Dimensions"]
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
                coordinates=coordinates,
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