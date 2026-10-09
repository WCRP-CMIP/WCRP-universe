"""
Generate horizontal label entries

Following Table F3 of
[Taylor et al.](https://docs.google.com/document/d/19jzecgymgiiEsTDzaaqeLP6pTvLT-NzCMaq-wu-QoOc/edit?pli=1&tab=t.0)
"""

import json


def main():
    for drs_name, description in (
        (
            "hxy",
            ("Data on x-y (often lat-lon) grid, also referred to as gridded data."),
        ),
        (
            "hy",
            (
                "Data that is a function of the y horizontal dimension, but not x "
                "(i.e., often just a function of latitude). "
                "This is usually a zonal-mean or zonal-sum or some other zonal-aggregate data."
            ),
        ),
        (
            "hs",
            ("Data reported at specific sites."),
        ),
        (
            "hyb",
            (
                "Data that is a function of the y horizontal dimension "
                "(i.e., often just a function of latitude), "
                "representing a zonal-mean or zonal-sum or some other aggregate across the x dimension "
                "for individual ocean basins (e.g., a zonal mean across each of the ocean basins)."
            ),
        ),
        (
            "ht",
            (
                "Data along a transect. "
                "This is some aggregate (sum, mean etc.) along the transect(s)."
            ),
        ),
        (
            "hm",
            ("Data reported as a mean over some horizontal area."),
        ),
    ):
        id = drs_name.lower()
        content = {
            "@context": "000_context.jsonld",
            "id": id,
            "type": "horizontal_label",
            "description": description,
            "drs_name": drs_name,
        }

        out_file = f"horizontal_label/{id}.json"
        with open(out_file, "w") as fh:
            json.dump(content, fh, indent=4)
            fh.write("\n")

        print(f"Wrote {out_file}")


if __name__ == "__main__":
    main()
