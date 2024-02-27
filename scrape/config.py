
#scrapy crawl blogSpider


####################################################################
#   Getting the information
####################################################################
#   Allowed domains for scraping
#   example: allowed_domains = ["example.com"]
allowed_domains = ["7tooti.com"]

#   Start url for scraping
#   example: start_urls = ["https://example.com/blogs"]
start_url = ["https://7tooti.com/wb/blog/"]

#   File path to save blog's html ids
#   example: /home/user/blog_html_ids.txt
file_id_path = "/home/yasin/Desktop/Work/scrape/scrape/blog_html_ids.txt"

#   Next page button's identifier
#   example: "div.class#id::attr(href)"
#   ** bare in mind that the button isn't necessary a <div> and can have any type **
#   ** but it must contain a href attribute that contains the link to the next page. **
next_page_identifier = "a#load-more-link::attr(href)"

#   The information we get must be saved in a json file so we can work on it. 
#   example: /home/user/blogs.json
json_saver_file = "/home/yasin/Desktop/Work/scrape/scrape/blogs.json"

#   test HTML file
#   we use this file to store, clean and reformat the html we get from our site
#   example: /home/user/html_file.html
HTML_file = "/home/yasin/Desktop/Work/scrape/scrape/html_file.html"

####################################################################
#   Storing the information
####################################################################

#   Odoo url
#   example: http://odoo.com
url = "http://localhost:10015"

#   Database name
#   ** to find your data base name simple activate developer mode and **
#   ** you should see it next to the name of your account **
#   example: db_name
db = "odoo"

#   User nameusername
#   eample: username
username = "odoo"

#   Password
#   example: password
password = "odoo"

#   API key
#   follow this guide to generate an api key: "https://www.odoo.com/documentation/15.0/developer/reference/external_api.html#api-keys"
API_key = "8cecbf837aec01d68c2fd6d848fb8f60ac5085d6"


