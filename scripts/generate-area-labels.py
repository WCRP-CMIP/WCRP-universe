"""
Generate area label entries

Following Table F4 of
[Taylor et al.](https://docs.google.com/document/d/19jzecgymgiiEsTDzaaqeLP6pTvLT-NzCMaq-wu-QoOc/edit?pli=1&tab=t.0)
"""

import json


def main():
    for drs_name, description, cf_area_type in (
        (
            "air",
            (
                "Data come solely from regions occupied by air "
                "(this isn't always the case e.g. if a variable is reported at sea level pressure "
                "but there is a mountain then the surface would not be air)."
            ),
            "air",
        ),
        (
            "cl",
            (
                "Data come solely from the portion of the atmosphere "
                "or the portion of an atmospheric column occupied by cloud."
            ),
            "cloud",
        ),
        (
            "ccl",
            (
                "Data come solely from the portion of the atmosphere "
                "or the portion of an atmospheric column occupied by convective cloud."
            ),
            "convective_cloud",
        ),
        (
            "crp",
            (
                "Data come solely from land areas covered by crops. "
                "'Crops' is loosely defined and model dependent."
            ),
            "crops",
        ),
        (
            "fis",
            (
                "Data come solely from areas of floating ice shelf. "
                "'Ice shelves' are the component of ice sheets that flow over the ocean."
            ),
            "floating_ice_shelf",
        ),
        (
            "gis",
            (
                "Data come solely from areas of grounded ice sheet. "
                "Grounded ice sheets rest over bedrock, excluding ice-caps, glaciers and floating ice shelves."
            ),
            "grounded_ice_sheet",
        ),
        (
            "ifs",
            ("Data come solely from sea areas that are free of ice."),
            "ice_free_sea",
        ),
        (
            "is",
            (
                "Data come solely from areas of ice sheets. "
                "'Ice sheets' include both grounded ice sheets resting on bedrock and any ice shelves flowing over the ocean "
                "that are attached to grounded ice sheets. "
                "It excludes ice-caps and glaciers and any floating ice shelves and ice tongues "
                "attached to them."
            ),
            "ice_sheet",
        ),
        (
            "lnd",
            (
                "Data come solely from land areas.  "
                "Every location on earth is classified as either land or sea, "
                "but further area type labels also apply to these primary types "
                "(e.g., crops or land ice apply to portions of the land area)."
            ),
            "land",
        ),
        (
            "li",
            (
                "Data come solely from areas of land ice. "
                "'Land ice' means glaciers, ice-caps, grounded ice sheets resting on bedrock and floating ice-shelves."
            ),
            "land_ice",
        ),
        (
            "ng",
            (
                "Data come solely from land areas covered by natural grasses. "
                "'Natural grasses' means grasses growing in areas of low productivity, "
                "often situated on rough or uneven ground. This can include rocky areas, briars and heathland."
            ),
            "natural_grasses",
        ),
        (
            "pst",
            (
                "Data come solely from land areas covered by pasture. "
                "Pastures are assumed to be anthropogenic in origin. "
                "They include anthropogenically managed pastureland and rangeland."
            ),
            "pastures",
        ),
        (
            "sea",
            (
                "Data come solely from areas covered by sea.  "
                "Every location on earth is classified as either land or sea, "
                "but further area type labels also apply to these primary types "
                "(e.g., sea ice or floating ice shelf)."
            ),
            "sea",
        ),
        (
            "si",
            ("Data come solely from areas of sea ice."),
            "sea_ice",
        ),
        (
            "simp",
            ("Data come solely from areas where melt pond is present atop sea ice."),
            "sea_ice_melt_pond",
        ),
        (
            "sir",
            ("Data come solely from areas where sea ice is 'ridged'."),
            "sea_ice_ridges",
        ),
        (
            "multi",
            (
                "Data come from several different area types "
                "with data from each area type stored separately in the variable's array "
                "as identified by its 'sector' dimension. "
                "This area type is typically used for including multiple land-use or vegetation area types in a single file."
            ),
            None,
        ),
        (
            "shb",
            (
                "Data come solely from land areas covered by shrubs. "
                "Shrubs is loosely defined and model dependent."
            ),
            "shrubs",
        ),
        (
            "sn",
            ("Data come solely from areas where the surface is covered by snow."),
            "snow",
        ),
        (
            "scl",
            (
                "Data come solely from the portion of the atmosphere "
                "or the portion of an atmospheric column occupied by stratiform cloud."
            ),
            "stratiform_cloud",
        ),
        (
            "tree",
            (
                "Data come solely from land areas covered by trees. "
                "All trees are in the C3 plant functional type. "
                "'Trees' is loosely defined and model dependent."
            ),
            "trees",
        ),
        (
            "ufs",
            (
                "Data come solely from areas of unfrozen soil. "
                "Unfrozen soil means that the soil at the surface is unfrozen. "
                "Frozen soil may be present at lower levels."
            ),
            "unfrozen_soil",
        ),
        (
            "veg",
            ("Data come solely from land areas covered by vegetation."),
            "vegetation",
        ),
        (
            "wl",
            (
                "Data come solely from wetland areas. "
                "Wetlands are land areas where water covers the soil, "
                "or is present either at or near the surface of the soil all year "
                "or for varying periods of time during the year, including during the growing season."
            ),
            "wetland",
        ),
        (
            "lsi",
            ("Data come solely from either areas of land or areas of sea ice."),
            None,
        ),
        ("u", ("Unmasked; all areas of the Earth are included."), None),
    ):
        id = drs_name.lower()
        content = {
            "@context": "000_context.jsonld",
            "id": id,
            "type": "area_label",
            "description": description,
            "drs_name": drs_name,
            "cf_area_type": cf_area_type,
        }

        out_file = f"area_label/{id}.json"
        with open(out_file, "w") as fh:
            json.dump(content, fh, indent=4)
            fh.write("\n")

        print(f"Wrote {out_file}")


if __name__ == "__main__":
    main()
