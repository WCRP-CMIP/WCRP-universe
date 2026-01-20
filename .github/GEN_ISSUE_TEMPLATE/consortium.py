# Consortium Template Configuration

TEMPLATE_CONFIG = {
    'name': 'Add/Modify: Consortium',
    'description': 'Add or modify a consortium (group of institutions) in WCRP Universe',
    'title': 'Add/Modify: Consortium: <Type consortium name here>',
    'labels': ['delta', 'organisation', 'consortium', 'Review', 'keep-open'],
    'issue_category': 'consortium'
}

# Data for this template
# The 'institutions' key uses a special prefix to fetch from the organisation collection
# filtering by type 'wcrp:institution'
DATA = {
    'issue_kind': ['New', 'Modify'],
    'institutions': 'wcrp:institution'  # This tells the generator to fetch all institutions
}
