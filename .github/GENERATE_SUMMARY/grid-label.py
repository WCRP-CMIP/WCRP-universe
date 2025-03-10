import cmipld
from cmipld.utils.ldparse import *
from cmipld.utils.checksum import version

me = __file__.split('/')[-1].replace('.py','')

def run(localhost,whoami,repopath,reponame):

    url = f'{localhost}/{whoami}/{me}/graph.jsonld'
    ctx = f'{localhost}/{whoami}/{me}/_context_'
    
    data = cmipld.jsonld.frame(url,ctx)["@graph"]
    
    summary = name_extract(data)
    
    location = f'{repopath}/{reponame}_{me}.json'
    summary = version(summary, me, location.split("/")[-1])
    cmipld.utils.io.wjsn(summary,location)