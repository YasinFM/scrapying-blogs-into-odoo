import os
import config
import xmlrpc.client
import base64
import make_logs

# Connect to Odoo through JSON-RPC
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(config.odoo_url))
uid = common.authenticate(config.odoo_db, config.odoo_username, config.odoo_password, {})

models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(config.odoo_url))

# Directory containing HTML files
html_files_directory = 'html-files'

def create_blog():
    # Check if the blog already exists
    existing_blog_ids = models.execute_kw(config.odoo_db, uid, config.odoo_password, 'blog.blog', 'search', [[('name', '=', 'Blog')]])
    if existing_blog_ids:
        print("Blog already exists.")
        return existing_blog_ids[0]

    # If the blog doesn't exist, create it
    blog_data = {
        'name': 'Blog',
    }
    blog_id = models.execute_kw(config.odoo_db, uid, config.odoo_password, 'blog.blog', 'create', [blog_data])
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
    post_id = models.execute_kw(config.odoo_db, uid, config.odoo_password, 'blog.post', 'create', [post_data])

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
                log = make_logs.log_type.POST_HTML
                make_logs.make_log(log)
                print("Blog post created with ID:", post_id, "for file:", filename)
    print("\nPosting blogs completed.")

def main():
    upload_html_files_as_blogs(html_files_directory)

#if __name__ == '__main__':
#    main()
