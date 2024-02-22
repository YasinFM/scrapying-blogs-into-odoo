import requests
from bs4 import BeautifulSoup
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # Add the parent directory to the sys.path
import config

def get_html_inside_div(html_path, div_class=None, div_id=None):
    # Read HTML file
    with open(html_path, 'r') as f:
        html_content = f.read()

    # Parse HTML
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find the div element with the specified class and/or id
    if div_class and div_id:
        div = soup.find('div', class_=div_class, id=div_id)
    elif div_class:
        div = soup.find('div', class_=div_class)
    elif div_id:
        div = soup.find('div', id=div_id)
    else:
        raise ValueError("Please provide either a div class, div id, or both.")

    # Return the HTML inside the div
    if div:
        return str(div)
    else:
        return ""

def get_html_title(html_path):
    title = ""
    div_class = 'w3-container'
    div_id = 'div-header'
    title = get_html_inside_div(html_path,div_class,div_id)
    
    return title

def get_html_content(html_path):
    content = ""
    div_class = 'main-content'
    div_id = ''
    content = get_html_inside_div(html_path,div_class,div_id)
    
    return content

def reformat_html(html_path):
    '''
    The main module to strip, clean and overall reformat our html to then upload it.
    '''
    title = get_html_title(html_path)
    content = get_html_content(html_path)
    reformated_html = title +  "\n" + content
    with open(html_path,"w") as html:
        html.write(reformated_html)
    
    return reformated_html
    

def html_file():
    '''
    The main module that gets the html from our site
    '''
    blog_id_file = open(config.file_id_path,"r")
    
    for id_file in blog_id_file:
        html_id = id_file[:len(id_file)-1]
        
        url = config.start_url[0] + "page/" + html_id
        r = requests.get(url=url)
        with open(config.HTML_file,"w") as file:
            file.write(r.text)
        reformat_html(config.HTML_file)
        
