import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # Add the parent directory to the sys.path
import config

def get_html_id(string):
        url_parts = string.split("/")
        id = url_parts[len(url_parts)-1]
        return id

class BlogspiderSpider(scrapy.Spider):
    name = "blogSpider"
    allowed_domains = config.allowed_domains
    start_urls = config.start_url
    
    
    
    def parse(self, response):
        
        blogs = response.css('div.w3-card-4.w3-margin.w3-white').getall()
        
        file = open(config.file_id_path,"a")
        
        for blog in blogs:
            stripped = blog.strip("<div itemscope=\"true\" itemtype=\"https://schema.org/BlogPosting\" id=\"")
            id = ""
            for char in stripped:
                if char.isnumeric():
                    id += char
                else:
                    break
            if id != "":
                id = "\"" + id + "\""
                address = '/html/body/div[1]/div[3]/div[1]/div[@id=' + id +']/div[5]/a/@href'
                html_address = response.xpath(address).extract_first()
                print(html_address)

                if html_address is not None:
                    html_id = get_html_id(html_address)
                    file.write(str(html_id) + '\n')
                
                '''
                yield{
                    'id' : html_address
                }
                '''
        
        next_page = response.css(config.next_page_identifier).get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
            
