
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
    
    # Helper functions for ROR v2 data extraction
    def get_display_name(names):
        """Get the ror_display name from names array"""
        for name in names:
            if 'ror_display' in name.get('types', []):
                return name['value']
        return names[0]['value'] if names else None
    
    def get_names_by_type(names, name_type):
        """Extract names by type (label, acronym, alias)"""
        return [n['value'] for n in names if name_type in n.get('types', [])]
    
    def get_labels(names):
        """Get label names (excluding ror_display and acronyms)"""
        return [n['value'] for n in names 
                if 'label' in n.get('types', []) and 'ror_display' not in n.get('types', [])]
    
    def get_links(links):
        """Extract website URLs from links array"""
        return [link['value'] for link in links if link.get('type') == 'website']
    
    # Extract location from v2 format
    location_data = ror_data.get('locations', [{}])[0].get('geonames_details', {})
    
    result = {
        "@context": "_context",
        "@id": f"{cmip_acronym.lower()}",
        "@type": ['wcrp:organisation', f'wcrp:{mytype}'],
        "ror": ror_data['id'].split('/')[-1],
        "ui_label": get_display_name(ror_data.get('names', [])),
        "url": get_links(ror_data.get('links', [])),
        "established": ror_data.get('established'),
        "kind": ror_data.get('types', [])[0] if ror_data.get('types') else None,
        "labels": get_labels(ror_data.get('names', [])),
        "aliases": get_names_by_type(ror_data.get('names', []), 'alias'),
        "acronyms": get_names_by_type(ror_data.get('names', []), 'acronym'),
        "location": {
            "@id": f"location/{ror_data['id'].split('/')[-1]}",
            "@type": "wcrp:location",
            "lat": location_data.get('lat'),
            "lon": location_data.get('lng'),
            "city": location_data.get('name'),
            "country": [location_data.get('country_code'), location_data.get('country_name')] if location_data.get('country_name') else None
        }         
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
                data = get_institution(data['ror'], data['@id'])
                    
            case {"@type": ldtypes} if 'wcrp:consortium' in ldtypes:
                errors = []
                return errors
                
        with open(file,'w') as f:
            json.dump(data, f, indent=4) 
        
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
