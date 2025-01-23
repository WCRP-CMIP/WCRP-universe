from pathlib import Path
import os,json

from _pytest.pathlib import insert_missing_modules
from mip_cmor_tables.models.consortium import Consortium
from mip_cmor_tables.models.institution import Institution

institution_path = Path("institution")
consortia_path = Path("consortium")

save_dir = 'organisation/'

# Create the directory if it doesn't exist
os.makedirs(save_dir, exist_ok=True)

for file in institution_path.iterdir():
    if file.suffix==".json":
        with open(file) as f:
            insti_dict = json.load(f)
        inst = Institution(**insti_dict) # 
        print(inst.id)
        inst_data = {
            "@context":"000_context.jsonld",
            "id": "institution/"+inst.id,
            "type": inst.type
        } 
    

        file_path = os.path.join(save_dir, f"{inst.id.lower()}.json")
        with open(file_path, 'w') as f:
            json.dump(inst_data, f, indent=4)

for file in consortia_path.iterdir():
    if file.suffix==".json":
        with open(file) as f:
            cons_dict = json.load(f)
        cons = Consortium(**cons_dict) # 
        print(cons.id)
        inst_data = {
            "@context":"000_context.jsonld",
            "id": "consortium/"+cons.id,
            "type": cons.type
        } 
    

        file_path = os.path.join(save_dir, f"{file.stem}.json") # caution name is from the original file NOT the id
        with open(file_path, 'w') as f:
            json.dump(inst_data, f, indent=4)



print("SAVED")
