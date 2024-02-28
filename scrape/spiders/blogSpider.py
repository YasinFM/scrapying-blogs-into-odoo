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

    handle_httpstatus_list = [404]  # Handle 404 errors
    
    def start_requests(self):
        base_url = "https://7tooti.com/wb/blog/?_px_p="
        for id in range(1, 132):
            url = base_url + str(id)
            if id != 1:
                yield scrapy.Request(url=url, callback=self.parse)
            else:
                yield scrapy.Request(url=config.start_url, callback=self.parse)
    
    
    
    def parse(self, response):
        if response.status == 404:
            self.logger.error("Page not found: %s", response.url)
            return

        # Your parsing logic continues here
        
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
        '''
        next_page = response.css(config.next_page_identifier).get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        '''
