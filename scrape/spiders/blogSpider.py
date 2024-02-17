import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

#scrapy crawl blogSpider
class BlogspiderSpider(scrapy.Spider):
    name = "blogSpider"
    allowed_domains = ["7tooti.com"]
    start_urls = ["https://7tooti.com/wb/blog/"]
    
    def parse(self, response):
        
        blogs = response.css('div.w3-card-4.w3-margin.w3-white').getall()
        #blogs = response.css('div#pages-collection').get()
        
        file = open("/home/yasin/Desktop/Work/Scrapy_7tooti_to_odoo15/scrape/scrape/spiders/blog_ids.txt","a")
        
        for blog in blogs:
            stripped = blog.strip("<div itemscope=\"true\" itemtype=\"https://schema.org/BlogPosting\" id=\"")
            id = ""
            for char in stripped:
                if char.isnumeric():
                    id += char
                else:
                    break
            if id != "":
                file.write(id + '\n')
                yield{
                    'id' : id
                }
        
        next_page = response.css('a#load-more-link::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
            
