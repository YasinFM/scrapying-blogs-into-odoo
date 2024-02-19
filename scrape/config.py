
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


####################################################################
#   Storing the information
####################################################################

