#!/usr/bin/env python3
"""Generate CMIP7 coordinate JSON files from the CMIP7 Data Request.

The script extracts records from the DReq "Coordinates and Dimensions" table
and writes one JSON-LD-compatible file per coordinate.

Example output file:

  coordinates/alevel.json

Each file contains one coordinate descriptor:

  {
    "@context": "000_context.jsonld",
    "id": "alevel",
    "type": "coordinate",
    "drs_name": "lev",
    ...
  }
"""

from __future__ import annotations

import argparse
import json
import re
import urllib.request
from pathlib import Path
from typing import Any, TypeAlias

from pydantic import BaseModel, Field

import data_request_api.content.dreq_content as dc
import data_request_api.query.dreq_query as dq

DEFAULT_VERSION = "v1.2.2.4"
DEFAULT_OUTPUT_DIR = "coordinate"
CONTEXT_FILE = "000_context.jsonld"

CMOR_REFERENCE_URLS = (
    "https://github.com/WCRP-CMIP/cmip7-cmor-tables/blob/main/tables/CMIP7_formula_terms.json",
    "https://github.com/WCRP-CMIP/cmip7-cmor-tables/blob/main/tables/CMIP7_grids.json",
    "https://github.com/WCRP-CMIP/cmip7-cmor-tables/blob/main/tables/CMIP7_coordinate.json",
    "https://github.com/WCRP-CMIP/cmip7-cmor-tables/blob/main/reference/MIP_coordinate.json",
    "https://github.com/WCRP-CMIP/cmip7-cmor-tables/blob/main/reference/MIP_formula_terms.json",
    "https://github.com/WCRP-CMIP/cmip7-cmor-tables/blob/main/reference/MIP_grids.json"
)

ScalarValue: TypeAlias = int | float | str

class Coordinate(BaseModel):
    """
    A coordinate, coordinate variable, auxiliary coordinate, scalar coordinate,
    or dimension used to describe how climate data are located in space, time,
    or along other physical or categorical axes.

    Examples: "longitude", "latitude", "time", "plev", "height2m", "basin"

    Coordinates define the reference system used to interpret the values of
    climate variables. They provide information about where and when data are
    valid, and how values are organised along physical, temporal, vertical,
    spectral, or categorical dimensions.

    Following the CF conventions, coordinates may take several forms:

    - *Coordinate variables*: one-dimensional variables whose name matches the
      corresponding dimension and whose values define the axis positions.
    - *Auxiliary coordinate variables*: additional coordinates associated with
      one or more dimensions that cannot be represented as a coordinate variable
      alone.
    - *Scalar coordinates*: coordinates represented by a single value and
      applying uniformly to an entire variable.

    Coordinates may optionally define axis orientation, units, direction,
    bounds, valid ranges, scalar values, or requested discrete values. Unlike
    variables, coordinates do not represent measured quantities themselves; they
    describe the domain over which variables are defined.
    """

    drs_name: str = Field(description="DRS-facing name expected in the output dataset")
    data_type: str = Field(description="Data type expected for the coordinate")
    dimensions: list[str] = Field(default=None, description="Dimensions associated with the coordinate-like entry")
    cf_standard_name: str = Field(default=None, description="CF standard name associated with the coordinate")
    long_name: str = Field(default=None, description="Human-readable long name of the coordinate")
    description: str = Field(default=None, description="Free-text description of the coordinate")
    axis: str = Field(default=None, pattern=r"^[XYZT]$", description="Coordinate axis when applicable: X, Y, Z or T")
    positive_direction: str = Field(default=None, description="Positive direction for vertical coordinates, e.g. up or down")
    stored_direction: str = Field(default=None, description="Expected storage direction, e.g. increasing or decreasing")
    units: str = Field(default=None, description="Units of the coordinate")
    has_bounds: bool = Field(default=None, description="Whether coordinate bounds are expected")
    value: ScalarValue = Field(default=None, description="Scalar coordinate value from value_scalar_or_string")
    lower_bound: ScalarValue = Field(default=None, description="Lower scalar bound when the coordinate defines one interval")
    upper_bound: ScalarValue = Field(default=None, description="Upper scalar bound when the coordinate defines one interval")
    values: list[ScalarValue] = Field(default=None, description="Requested coordinate values from requested_values")
    bounds: list[ScalarValue] = Field(default=None, description="Requested coordinate bounds from requested_bounds")
    valid_min: ScalarValue = Field(default=None, description="Minimum valid value, when defined")
    valid_max: ScalarValue = Field(default=None, description="Maximum valid value, when defined")
    size: int = Field(default=None, description="Declared coordinate size, when defined")
    is_climatology: bool = Field(default=None, description="Whether the coordinate represents climatological time")

def get_attr(record: Any, key: str, default: Any = None) -> Any:
    """Return an attribute from a DR record object."""
    if record is None or key is None:
        return None
    if hasattr(record, key):
        return getattr(record, key)
    return default

def none_if_empty(value: Any) -> Any:
    """Return None for DReq empty values."""
    if value in (None, "", []):
        return None
    return value

def str_or_none(value: Any) -> str | None:
    """Return a string or None from scalar or one-value DReq fields."""
    value = none_if_empty(value)
    if value is None:
        return None
    if isinstance(value, (list, tuple, set)):
        values = [str(v) for v in value if v not in (None, "")]
        return " ".join(values) if values else None
    return str(value)

def int_or_none(value: Any) -> int | None:
    """Return an integer or None."""
    value = none_if_empty(value)
    if value is None:
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        print(f"Warning: cannot cast value to int: {value!r}; field ignored.")
        return None

def bool_or_none(value: Any) -> bool | None:
    """Return a boolean or None from DReq boolean-like values."""
    value = none_if_empty(value)
    if value is None:
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in {"yes", "true", "1", "y"}:
            return True
        if lowered in {"no", "false", "0", "n"}:
            return False
    print(f"Warning: cannot cast value to bool safely: {value!r}; using bool(value).")
    return bool(value)

def parse_scalar(value: Any) -> ScalarValue | None:
    """Parse a scalar as int or float when possible, otherwise keep a string."""
    value = none_if_empty(value)
    if value is None:
        return None
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return value

    text = str(value).strip()
    if not text:
        return None

    try:
        if re.fullmatch(r"[+-]?\d+", text):
            return int(text)
        if re.fullmatch(r"[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?", text):
            return float(text)
    except ValueError:
        pass

    return text

def parse_sequence(value: Any) -> list[ScalarValue] | None:
    """Parse a scalar/list/string DReq sequence into a typed list."""
    value = none_if_empty(value)
    if value is None:
        return None
    if isinstance(value, (list, tuple, set)):
        parsed = [parse_scalar(v) for v in value]
        return [v for v in parsed if v is not None] or None

    text = str(value).strip()
    if not text:
        return None

    parts = [part.strip() for part in text.split(",")] if "," in text else text.split()
    parsed = [parse_scalar(part) for part in parts if part.strip()]
    return [v for v in parsed if v is not None] or None

def parse_bounds_scalar(value: Any, coord_name: str) -> tuple[ScalarValue | None, ScalarValue | None]:
    """Parse bounds_scalar into lower_bound and upper_bound."""
    values = parse_sequence(value)
    if values is None:
        return None, None
    if len(values) != 2:
        print(
            f"Warning: coordinate {coord_name!r} has bounds_scalar with "
            f"{len(values)} values instead of 2: {values!r}; bounds ignored."
        )
        return None, None
    return values[0], values[1]

def drop_none(data: dict[str, Any]) -> dict[str, Any]:
    """Return a copy without None values."""
    return {key: value for key, value in data.items() if value is not None}

def model_dump_excluding_none(model: BaseModel) -> dict[str, Any]:
    """Return model data without None values, compatible with Pydantic v1/v2."""
    if hasattr(model, "model_dump"):
        return model.model_dump(exclude_none=True)
    return model.dict(exclude_none=True)

def dreq_record_to_coordinate(record: Any) -> tuple[str, Coordinate]:
    """Build one Coordinate from one DReq coordinate record."""
    coord_name = str_or_none(get_attr(record, "name"))
    if coord_name is None:
        raise ValueError(f"Coordinate record without name: {record!r}")

    lower_bound, upper_bound = parse_bounds_scalar(
        get_attr(record, "bounds_scalar"),
        coord_name,
    )

    data = {
        "drs_name": get_attr(record, "output_name"),
        "data_type": get_attr(record, "type"),
        "standard_name": get_attr(record, "cf_standard_name"),
        "long_name": get_attr(record, "title"),
        "description": str_or_none(get_attr(record, "description")),
        "axis": get_attr(record, "axis_flag"),
        "positive_direction": str_or_none(get_attr(record, "positive_direction")),
        "stored_direction": str_or_none(get_attr(record, "stored_direction")),
        "units": str_or_none(get_attr(record, "units")),
        "has_bounds": bool_or_none(get_attr(record, "bounds_flag")),
        "value": parse_scalar(get_attr(record, "value_scalar_or_string")),
        "lower_bound": lower_bound,
        "upper_bound": upper_bound,
        "values": parse_sequence(get_attr(record, "requested_values")),
        "bounds": parse_sequence(get_attr(record, "requested_bounds")),
        "valid_min": parse_scalar(get_attr(record, "minimum_valid_value")),
        "valid_max": parse_scalar(get_attr(record, "maximum_valid_value")),
        "size": int_or_none(get_attr(record, "size")),
        "is_climatology": bool_or_none(get_attr(record, "climatology_flag")),
    }

    return coord_name, Coordinate(**drop_none(data))

def merge_list_values(*values: Any) -> list[ScalarValue]:
    """Merge scalar/list values into a unique list preserving order."""
    merged: list[ScalarValue] = []
    for value in values:
        candidates = value if isinstance(value, list) else [value]
        for candidate in candidates:
            if candidate in (None, ""):
                continue
            if candidate not in merged:
                merged.append(candidate)
    return merged

def merge_duplicate_coordinate(
    coord_name: str,
    existing: Coordinate,
    incoming: Coordinate,
) -> Coordinate:
    """Merge duplicated DReq coordinate names."""
    existing_data = model_dump_excluding_none(existing)
    incoming_data = model_dump_excluding_none(incoming)
    merged = dict(existing_data)
    list_fields = {"values", "bounds"}

    for key, incoming_value in incoming_data.items():
        existing_value = merged.get(key)
        if existing_value in (None, "", []):
            merged[key] = incoming_value
        elif incoming_value in (None, "", []):
            continue
        elif existing_value == incoming_value:
            continue
        elif key in list_fields:
            print(
                f"Warning: duplicated coordinate {coord_name!r} has different {key}: "
                f"{existing_value!r} vs {incoming_value!r}; keeping both values."
            )
            merged[key] = merge_list_values(existing_value, incoming_value)
        else:
            print(
                f"Warning: duplicated coordinate {coord_name!r} has different {key}: "
                f"{existing_value!r} vs {incoming_value!r}; keeping first value."
            )

    return Coordinate(**merged)

def github_url_to_raw(url: str) -> str:
    """Return a raw GitHub URL from either a blob URL or an already raw URL."""
    if "github.com" in url and "/blob/" in url:
        return url.replace("https://github.com/", "https://raw.githubusercontent.com/").replace("/blob/", "/")
    return url

def load_json_url(url: str) -> Any:
    """Load a JSON document from a URL."""
    raw_url = github_url_to_raw(url)
    with urllib.request.urlopen(raw_url) as response:
        return json.loads(response.read().decode("utf-8"))

def find_reference_entries(document: Any) -> dict[str, dict[str, Any]]:
    """Return coordinate-like entries from a CMOR reference JSON document.

    The CMOR reference files may expose entries either directly at top level or
    below a container key. This function deliberately ignores metadata/header
    blocks and keeps only mapping entries whose values are dictionaries.
    """
    if not isinstance(document, dict):
        return {}

    preferred_containers = (
        "axis_entry",
        "formula_entry"
    )

    for container in preferred_containers:
        value = document.get(container)
        if isinstance(value, dict):
            return {
                str(key): entry
                for key, entry in value.items()
                if isinstance(entry, dict)
            }

    ignored_keys = {
        "Header"
    }

    return {
        str(key): entry
        for key, entry in document.items()
        if key not in ignored_keys and isinstance(entry, dict)
    }

def list_strings_or_none(value: Any) -> list[str] | None:
    """Return a non-empty list of strings, or None."""
    value = none_if_empty(value)
    if value is None:
        return None
    if isinstance(value, (list, tuple, set)):
        values = [str(v) for v in value if v not in (None, "")]
    else:
        values = [str(value)]
    cleaned = []
    for item in values:
        if item and item not in cleaned:
            cleaned.append(item)
    return cleaned or None

def bool_from_reference(value: Any) -> bool | None:
    """Return a boolean from CMOR reference boolean-like values."""
    if value in (None, "", []):
        return None
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        lowered = value.strip().lower()
        if lowered in {"yes", "true", "1", "y", "required"}:
            return True
        if lowered in {"no", "false", "0", "n", "optional"}:
            return False
    return bool(value)

def reference_entry_to_coordinate(name: str, entry: dict[str, Any]) -> Coordinate:
    """Convert one CMOR reference entry into the current Coordinate model."""
    lower_bound, upper_bound = parse_bounds_scalar(
        entry.get("bounds_scalar"),
        name,
    )

    data = {
        "drs_name": str_or_none(
            entry.get("output_name")
            or entry.get("out_name")
            or entry.get("name")
            or name
        ),
        "data_type": str_or_none(
            entry.get("data_type")
            or entry.get("type")
            or entry.get("datatype")
            or "double"
        ),
        "dimensions": list_strings_or_none(
            entry.get("dimensions")
            or entry.get("dimension")
        ),
        "cf_standard_name": str_or_none(
            entry.get("cf_standard_name")
            or entry.get("standard_name")
        ),
        "long_name": str_or_none(
            entry.get("long_name")
            or entry.get("title")
        ),
        "description": str_or_none(
            entry.get("description")
            or entry.get("comment")
        ),
        "axis": str_or_none(
            entry.get("axis")
            or entry.get("axis_flag")
        ),
        "positive_direction": str_or_none(
            entry.get("positive_direction")
            or entry.get("positive")
        ),
        "stored_direction": str_or_none(
            entry.get("stored_direction")
            or entry.get("direction")
        ),
        "units": str_or_none(entry.get("units")),
        "has_bounds": bool_from_reference(
            entry.get("has_bounds")
            or entry.get("bounds_flag")
            or entry.get("must_have_bounds")
        ),
        "value": parse_scalar(
            entry.get("value")
            or entry.get("requested")
            or entry.get("value_scalar_or_string")
        ),
        "lower_bound": lower_bound,
        "upper_bound": upper_bound,
        "values": parse_sequence(
            entry.get("values")
            or entry.get("requested_values")
        ),
        "bounds": parse_sequence(
            entry.get("bounds")
            or entry.get("requested_bounds")
        ),
        "valid_min": parse_scalar(
            entry.get("valid_min")
            or entry.get("minimum_valid_value")
        ),
        "valid_max": parse_scalar(
            entry.get("valid_max")
            or entry.get("maximum_valid_value")
        ),
        "size": int_or_none(entry.get("size")),
        "is_climatology": bool_from_reference(
            entry.get("is_climatology")
            or entry.get("climatology_flag")
        ),
    }

    return Coordinate(**drop_none(data))

def load_cmor_reference_coordinates(urls: tuple[str, ...]) -> dict[str, Coordinate]:
    """Load coordinate-like entries from CMOR reference JSON files."""
    coordinates: dict[str, Coordinate] = {}

    for url in urls:
        try:
            document = load_json_url(url)
        except Exception as exc:
            print(f"Warning: unable to load CMOR reference file {url!r}: {exc}")
            continue

        entries = find_reference_entries(document)
        print(f"CMOR reference entries from {url.rsplit('/', 1)[-1]}: {len(entries)}")

        for name, entry in entries.items():
            if name in coordinates:
                print(f"Info: duplicated CMOR reference coordinate skipped: {name}")
                continue
            try:
                coordinates[name] = reference_entry_to_coordinate(name, entry)
            except Exception as exc:
                print(f"Warning: unable to convert CMOR reference entry {name!r}: {exc}")

    return coordinates

def merge_dreq_and_cmor_coordinates(
    dreq_coordinates: dict[str, Coordinate],
    cmor_coordinates: dict[str, Coordinate],
) -> dict[str, Coordinate]:
    """Merge DReq and CMOR coordinates, keeping DReq entries in priority."""
    merged = dict(dreq_coordinates)
    added = 0
    skipped = 0

    for name, coordinate in cmor_coordinates.items():
        if name in merged:
            skipped += 1
            continue
        merged[name] = coordinate
        added += 1

    print(f"CMOR reference coordinates added: {added}")
    print(f"CMOR reference coordinates skipped because already in DReq: {skipped}")
    print(f"Total coordinates: {len(merged)}")
    return merged

def load_dreq_coordinates(version: str) -> dict[str, Coordinate]:
    """Load and convert DReq coordinates."""
    dc.retrieve(version)
    content = dc.load(version)
    tables = dq.create_dreq_tables_for_request(content, version)
    dreq_coordinates = tables["Coordinates and Dimensions"]

    coordinates: dict[str, Coordinate] = {}

    for record in dreq_coordinates.records.values():
        coord_name, coordinate = dreq_record_to_coordinate(record)
        if coord_name in coordinates:
            print(f"Warning: duplicated DReq coordinate name {coord_name!r}; merging.")
            coordinates[coord_name] = merge_duplicate_coordinate(
                coord_name,
                coordinates[coord_name],
                coordinate,
            )
        else:
            coordinates[coord_name] = coordinate

    print(f"DReq Coordinates: {len(coordinates)}")
    return coordinates

def write_coordinate_json_files(records: dict[str, Coordinate], output_dir: Path) -> None:
    """Write one coordinate JSON-LD-compatible file per coordinate."""
    output_dir.mkdir(parents=True, exist_ok=True)

    for name, record in sorted(records.items()):
        payload = {
            "@context": CONTEXT_FILE,
            "id": name,
            "type": "coordinate",
            **model_dump_excluding_none(record),
        }

        output_file = output_dir / f"{name}.json"
        with output_file.open("w", encoding="utf-8") as f:
            json.dump(payload, f, indent=2, ensure_ascii=False)
            f.write("\n")

    print(f"Wrote {len(records)} coordinate JSON files to {output_dir}")

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Generate one CMIP7 coordinate JSON file per DReq coordinate record.",
    )
    parser.add_argument("--version", default=DEFAULT_VERSION, help="DReq version")
    parser.add_argument(
        "--output-dir",
        default=DEFAULT_OUTPUT_DIR,
        help="Directory where one JSON file per coordinate will be written",
    )
    args = parser.parse_args()

    dreq_coordinates = load_dreq_coordinates(args.version)
    cmor_coordinates = load_cmor_reference_coordinates(CMOR_REFERENCE_URLS)
    coordinates = merge_dreq_and_cmor_coordinates(dreq_coordinates, cmor_coordinates)
    write_coordinate_json_files(coordinates, Path(args.output_dir))

if __name__ == "__main__":
    main()
