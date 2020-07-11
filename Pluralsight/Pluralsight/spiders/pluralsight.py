from scrapy import Spider, Request
import numpy as np

class PluralsightSpider(Spider):
    name = 'pluralsight'
    allowed_domains = ['pluralsight.com']
    start_urls = ['http://pluralsight.com/browse']
    base_url = 'http://pluralsight.com'

    def start_requests(self):
        for url in self.start_urls:
            if url == "http://pluralsight.com/browse":
                yield Request(url, callback=self.parse_home)
    
    def parse_home(self, response):
        urls = np.array(response.xpath("//a/@href").extract())
        category_urls = [item for i, item in enumerate(urls) if '/browse/' in item]
        for category_url in category_urls:
            url = self.base_url+category_url 
            yield Request(url, callback=self.parse_category)
    
    def parse_category(self, response):
        course_title = response.css('#tab-courses .course-item__title').getall()
        yield {'courses':course_title}

