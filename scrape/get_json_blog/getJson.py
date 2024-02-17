import requests
import tools

blog_id_file = open("/home/yasin/Desktop/Work/Scrapy_7tooti_to_odoo15/scrape/scrape/spiders/blog_ids.txt","r")

blogs_file = "/home/yasin/Desktop/Work/Scrapy_7tooti_to_odoo15/scrape/scrape/get_json_blog/blogs.json"

for id_file in blog_id_file:
    id = id_file[:len(id_file)-1]
    url = "https://7tooti.com/api/v2/cms/contents/" + id + "/content"
    
    r = requests.get(url=url)
    data = r.json()
    tools.add_to_json(data,blogs_file)
    

blog_id_file.close()