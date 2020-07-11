from scrapy import Spider,Request

class PluralsightSpider(scrapy.Spider):
    name = 'pluralsight'
    allowed_domains = ['pluralsight.com']
    start_urls = ['http://pluralsight.com/browse']

    def start_requests(self):
        for url in self.start_urls:
            if url == "http://pluralsight.com/browse":
                
