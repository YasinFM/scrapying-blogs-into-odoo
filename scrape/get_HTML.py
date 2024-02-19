import requests
import json
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # Add the parent directory to the sys.path
import config


def get_html_id():
    blog_id_file = open(config.file_id_path,"r")
    
    for id_file in blog_id_file:
        html_id = id_file[:len(id_file)-1]
        file  = open("/home/yasin/Desktop/Work/scrape/scrape/html_file.html","w")
        url = "https://7tooti.com/wb/blog/page/" + html_id
        r = requests.get(url=url)
        print(r.text)
        file.write(r.text)
    
get_html_id()