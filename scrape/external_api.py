import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # Add the parent directory to the sys.path
import config
import xmlrpc.client
import base64

#filename[:len(filename) - 5]

# Odoo instance information
url = "http://localhost:10015"
db = "odoo"
username = "odoo"
password = "odoo"
API_key = "8cecbf837aec01d68c2fd6d848fb8f60ac5085d6"

# Connect to Odoo through JSON-RPC
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Directory containing HTML files
html_files_directory = '/home/yasin/Desktop/Work/scrape/html-files'

def create_blog():
    # Check if the blog already exists
    existing_blog_ids = models.execute_kw(db, uid, password, 'blog.blog', 'search', [[('name', '=', 'Blog')]])
    if existing_blog_ids:
        print("Blog already exists.")
        return existing_blog_ids[0]

    # If the blog doesn't exist, create it
    blog_data = {
        'name': 'Blog',
    }
    blog_id = models.execute_kw(db, uid, password, 'blog.blog', 'create', [blog_data])
    print("Blog created with ID:", blog_id)
    return blog_id

def create_blog_post(filename, html_content, blog_id):
    # Decode the HTML content
    decoded_html_content = base64.b64decode(html_content)

    # Define the blog post data
    post_data = {
        'name': filename[:len(filename) - 5],
        'content': decoded_html_content.decode('utf-8'),
        'blog_id': blog_id,
    }

    # Create the blog post
    post_id = models.execute_kw(db, uid, password, 'blog.post', 'create', [post_data])

    return post_id

def read_html_file(file_path):
    # Read the HTML file
    with open(file_path, 'rb') as file:
        html_content = file.read()
    return base64.b64encode(html_content).decode('utf-8')

def upload_html_files_as_blogs(directory):
    # Create the blog if it doesn't exist
    blog_id = create_blog()

    # Iterate over HTML files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.html'):
            html_file_path = os.path.join(directory, filename)
            html_content = read_html_file(html_file_path)
            post_id = create_blog_post(filename, html_content, blog_id)
            if post_id:
                print("Blog post created with ID:", post_id, "for file:", filename)

def main():
    upload_html_files_as_blogs(html_files_directory)

if __name__ == '__main__':
    main()
