# Consortium Template Configuration

import cmipld
from cmipld.utils.ldparse import name_extract

TEMPLATE_CONFIG = {
    'name': 'Add/Modify: Consortium',
    'description': 'Add or modify a consortium (group of institutions) in WCRP Universe',
    'title': 'Add/Modify: Consortium',
    'labels': ['delta', 'organisation', 'consortium', 'Review', 'keep-open'],
    'issue_category': 'consortium'
}

# Data for this template
# The 'institutions' key uses a special prefix to fetch from the organisation collection
# filtering by type 'wcrp:institution'

org = name_extract(cmipld.get('universal:organisation/graph.jsonld', depth=0))
inst = [f"{k} : {v.get('ui_label','')}" for k,v in org.items() if 'ror' in v]

DATA = {
    'issue_kind': ['New', 'Modify'],
    'institutions': inst  # This tells the generator to fetch all institutions
}
