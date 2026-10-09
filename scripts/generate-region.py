"""
Generate region entries
"""

import json


def main():
    for id, drs_name, description, cf_standard_region, iso_region in (
        (
            "global",
            "glb",
            "The geographical region of the whole of the Earth’s surface, as defined by the CF conventions.",
            "global",
            None,
        ),
        ("antarctica", "ata", "Antarctica.", "antarctica", "ata"),
        (
            "greenland",
            "grl",
            "The geographical region of Greenland, as defined by the CF conventions.",
            "greenland",
            "grl",
        ),
        (
            "30s-90s",
            "30S-90S",
            "The geographical region of the Earth’s surface between 30 and 90 degrees south.",
            None,
            None,
        ),
        (
            "northern-hemisphere",
            "nh",
            "The Northern Hemisphere.",
            "northern_hemisphere",
            None,
        ),
        (
            "southern-hemisphere",
            "sh",
            "The Southern Hemisphere.",
            "southern_hemisphere",
            None,
        ),
    ):
        content = {
            "@context": "000_context.jsonld",
            "id": id,
            "type": "region",
            "description": description,
            "drs_name": drs_name,
            "cf_standard_region": cf_standard_region,
            "iso_region": iso_region,
        }

        out_file = f"region/{id}.json"
        with open(out_file, "w") as fh:
            json.dump(content, fh, indent=4, ensure_ascii=False)
            fh.write("\n")

        print(f"Wrote {out_file}")


if __name__ == "__main__":
    main()
