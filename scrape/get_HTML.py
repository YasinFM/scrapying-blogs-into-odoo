import json
import requests
from bs4 import BeautifulSoup
import os
import config
import make_logs
from enum import Enum

class get_type(Enum):
    ORIGINAL_FILES = "ORIGINAL_FILES"
    REFOMATED_FILES = "REFORMATED_FILES"

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
        return str(div), div.text, ''.join(map(str, div.contents))
    else:
        return "", "", ""

def get_html_title(html_path):
    
    #   Get title from HTML tag
    title = ""
    title_name = ""
    div_class = 'w3-container'
    div_id = 'div-header'
    title, title_name, title_div = get_html_inside_div(html_path,div_class,div_id)
    
    return title, title_name

def get_html_content(html_path):
    
    #   Remove extra contents of div  
    content = ""
    content_text = ""
    div_class = 'main-content'
    div_id = ''
    content, content_text, content_div = get_html_inside_div(html_path,div_class,div_id)
    
    return content_div

def save_old_html(name, html_path):
    with open(html_path, 'r') as f:
        old_content = f.read()
    
    # Create the data folder if it doesn't already exist 
    if not os.path.exists('html-files/old-html-files'): 
        os.mkdir('html-files/old-html-files')
    
    with open('html-files/old-html-files/' + name + '-old.html', 'w') as f: 
            f.write(old_content)
            log = make_logs.log_type.GET_HTML
            make_logs.make_log(log)

def save_new_html(name, content):
    # Create the data folder if it doesn't already exist 
    if not os.path.exists('html-files'): 
        os.mkdir('html-files')
        
    with open('html-files/' + name + '.html', 'w') as f: 
            f.write(content)
            log = make_logs.log_type.GET_HTML
            make_logs.make_log(log)

def reformat_html(html_path):
    #   The main module to strip, clean and overall reformats our html
    
    title, name = get_html_title(html_path)
    content = get_html_content(html_path)

    if title != '':
        save_old_html(name, html_path)
        save_new_html(name, content)

def html_file():
    #   The main module that gets the html files, reformats them
    #   and saves them for uploadinglater 
    with open(config.file_id_path, 'r') as f:
        blog_id_file = json.load(f) 
    
    for id_file in blog_id_file["items"]:
        html_id = id_file["name"]
        url = config.start_url + "page/" + html_id
        r = requests.get(url=url)
        with open(config.HTML_file,"w") as file:
            file.write(r.text)
        reformat_html(config.HTML_file)
    print("\nGetting html files completed.")
        
def main():
    html_file()

if __name__ == '__main__':
    main()
