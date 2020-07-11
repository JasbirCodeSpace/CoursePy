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
        urls = np.unique(urls)
        category_urls = [item for i, item in enumerate(urls) if '/browse/' in item]
        for category_url in category_urls:
            url = self.base_url + category_url
            category = url.split('/')[-1]
            yield Request(url, callback=self.parse_category,meta={'category':category})
    
    def parse_category(self, response):
        urls = np.array(response.xpath("//a/@href").extract())
        course_urls = [item for i, item in enumerate(urls) if '/courses/' in item]
        category = response.meta.get('category')
        for course_url in course_urls:
            url = self.base_url + course_url
            yield Request(url,callback=self.parse_course,meta={'category':category})

    def parse_course(self, response):
        title = response.xpath("//h1//text()").get()
        author = response.css("div.author_image_mask']::text").get()
        difficulty = response.css("div.difficulty-level::text").get()
        duration = response.xpath("//div[@class='course-info__row--right']//text()").get()
        link = response.request.url
        category = response.meta.get('category')
        yield {'title':title,'author':author,'difficulty':difficulty,'duration':duration,'link':link,'category':category}

