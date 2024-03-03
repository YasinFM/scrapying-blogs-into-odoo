import json
import datetime
import config
from enum import Enum

class log_type(Enum):
    GET_IDS = "GET_IDS"
    GET_HTML = "GET_HTML"
    POST_HTML = "POST_HTML"
    DELETE_HTMLS = "DELETE_HTMLS"

def get_id_log(type):
    with open(config.log_path, 'r') as file:
        existing_data = json.load(file)
        
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    
    if type == 0 :
        title = "get html ids via spider"
        descriptions = "get the html ids from " + config.start_url + " via scrapy spider at " + time
        
    elif type == 1:
        title = "get html ids via curl"
        descriptions = "get the html ids from " + config.content_url + " via curl at " + time
    else:
        return -1
        
    new_data = {
        "log_number": existing_data["counts"],
        "time": time,
        "request": "GET",
        "info":[
            {"title": title,
            "descriptions": descriptions
            }
            ]
    }
    existing_data["counts"] += 1
    existing_data["logs"].append(new_data)
    with open(config.log_path, 'w') as file:
        json.dump(existing_data, file, indent=4)
    
def get_html_log():
    pass
def post_html_log():
    pass
def delete_html_log():
    pass
def make_log(
    log, type = None
    ):
    
    if log == log_type.GET_IDS:
        get_id_log(type)
    elif log == log_type.GET_HTML:
        get_html_log()
    elif log == log_type.POST_HTML:
        post_html_log()
    elif log == log_type.DELETE_HTMLS:
        delete_html_log()
    else:
        print("Invalid log type")

#########################################################################

def error_get_id_log(type):
    pass
def error_get_html_log():
    pass
def error_post_html_log():
    pass
def error_delete_html_log():
    pass

def make_error_log(
    log, type = None
    ):
    
    if log == log_type.GET_IDS:
        error_get_id_log(type)
    elif log == log_type.GET_HTML:
        error_get_html_log()
    elif log == log_type.POST_HTML:
        error_post_html_log()
    elif log == log_type.DELETE_HTMLS:
        error_delete_html_log()
    else:
        print("Invalid log type")
    
