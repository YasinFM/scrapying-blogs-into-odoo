import requests
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # Add the parent directory to the sys.path
import config


def save_json():
    blog_id_file = open(config.file_id_path,"r")
    blogs_file = config.json_saver_file

    for id_file in blog_id_file:
        id = id_file[:len(id_file)-1]
        url = "https://7tooti.com/api/v2/cms/contents/" + id + "/content"
        
        r = requests.get(url=url)
        if r == '':
            data = {id: r.json()}
            with open(blogs_file, 'w') as file:
                json.dump(data, file, indent=4)
        

    blog_id_file.close()