from bs4 import BeautifulSoup

def get_html_inside_div(html_file, div_class=None, div_id=None):
    # Read HTML file
    with open(html_file, 'r') as f:
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
        return None

# Usage example
html_file = '/home/yasin/Desktop/Work/scrape/scrape/html_file.html'
div_class = 'main-content'
div_id = ''
html_inside_div = get_html_inside_div(html_file, div_class, div_id)
if html_inside_div:
    file = open("/home/yasin/Desktop/Work/scrape/scrape/test2.html","w")
    file.write(html_inside_div)
    print(html_inside_div)
else:
    print("No div with the specified class and/or id found.")

#html_file = '/home/yasin/Desktop/Work/scrape/scrape/html_file.html'
#json_file = '/home/yasin/Desktop/Work/scrape/scrape/test.json'
