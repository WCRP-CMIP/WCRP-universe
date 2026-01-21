import cmipld
import json
from cmipld.utils.jsontools import sort_json_keys


repopath = './organisation/'


def get_institution(ror, acronym):

    mytype = 'institution'

    # ROR API v2 endpoint
    ror_template = 'https://api.ror.org/v2/organizations/{}'

    url = ror_template.format(ror)

    ror_data = cmipld.utils.read_url(url)

    assert ror_data, f"ROR data not found for {ror},{acronym} in {url}. Exiting Now."
    
    # ensure the acronym has no _
    cmip_acronym = acronym.replace('_','-')
    
    # v2 helper: get display name
    names = ror_data.get('names', [])
    display_name = next((n['value'] for n in names if 'ror_display' in n.get('types', [])), names[0]['value'] if names else None)
    
    # v2 helper: extract location - keep all geonames fields
    loc = ror_data.get('locations', [{}])[0].get('geonames_details', {})
    
    result = {
        "@id": f"{cmip_acronym.lower()}",
        "@type": ['wcrp:organisation', f'wcrp:{mytype}'],
        "validation_key": acronym,
        "ror": ror_data['id'].split('/')[-1],
        "ui_label": display_name,
        "url": [l['value'] for l in ror_data.get('links', [])],  # ALL links
        "established": ror_data.get('established'),
        "kind": ror_data.get('types', [None])[0],  # First type only
        "labels": [n['value'] for n in names if 'label' in n.get('types', [])],  # Just values
        "aliases": [n['value'] for n in names if 'alias' in n.get('types', [])],
        "acronyms": [n['value'] for n in names if 'acronym' in n.get('types', [])],
        "location": [
            {
                "@id": f"universal:location/{ror_data['id'].split('/')[-1]}",
                "@type": "wcrp:location",
                "lat": loc.get('lat'),
                "lng": loc.get('lng'),
                "name": loc.get('name'),
                "country_code": loc.get('country_code'),
                "country_name": loc.get('country_name'),
                "country_subdivision_code": loc.get('country_subdivision_code'),
                "country_subdivision_name": loc.get('country_subdivision_name'),
                "continent_code": loc.get('continent_code'),
                "continent_name": loc.get('continent_name'),
            }
        ],
        "@context": "_context",
    }
    
    return sort_json_keys(result)


if __name__ == '__main__':
    from p_tqdm import p_map
    import glob
    
    files = glob.glob(repopath+'*.json')
    
    def update(file):
        
        data = json.load(open(file))
        
        match data:
            case {"@type": ldtypes} if 'wcrp:institution' in ldtypes:
                # Use validation_key for correct case, fall back to @id
                acronym = data.get('validation_key', data.get('@id', ''))
                data = get_institution(data['ror'], acronym)
                    
            case {"@type": ldtypes} if 'wcrp:consortium' in ldtypes:
                errors = []
                return errors
                
        with open(file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False) 
        
    # run on all files
    errors = p_map(update, files)
    errors = [i for i in errors if i]
        
    if errors: 
        from rich.console import Console
        from rich.table import Table
        from rich.text import Text
        console = Console()
            
        console.print(Text("Validation Errors", style="bold red underline"))

        table = Table(show_header=True, header_style="bold white")
        
        table.add_column("Type", style="bold green")
        table.add_column("Item", style="bold blue")
        table.add_column("Warnings", style="red")

        for kind, ror, validation_key, err in errors:
            table.add_row(
                kind,
                f"{ror}: {validation_key}",
                f"[{err['loc'][0]}]:\n {err['msg']}"
            )

        console.print(table)
