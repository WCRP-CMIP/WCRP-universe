import cmipld
import os
from cmipld.utils.ldparse import *
from cmipld.utils.checksum import version

me = __file__.split('/')[-1].replace('.py','')

def run(whoami, path, name, url, io):
    
    os.popen(f"ld2graph {me}").read()
    
    url = f'{whoami}:organisation/graph.jsonld'
    
    data = cmipld.get(url,depth=1)['@graph']
    
    summary = name_extract(data,['acronyms', 'ui-label','url','ror'])
    
    location = f'{path}/{name}_{me}.json'
    return location, me, summary