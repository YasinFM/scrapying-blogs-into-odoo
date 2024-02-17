import json
from os import path

def add_to_json(data,destination):
    
    # Check if file exists
    if path.isfile(destination) is False:
        raise Exception("File not found")
    
    # Read JSON file
    listObj = []
    with open(destination) as fp:
        listObj = json.load(fp)
        
    with open(destination, 'w') as json_file:
        json.dump(
            listObj, json_file,
            indent=4, separators=(',',': ')
            )
