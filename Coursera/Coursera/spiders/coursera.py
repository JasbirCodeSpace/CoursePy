from scrapy import Spider,Request
from urllib.parse import urlparse
from urllib.parse import parse_qs

class Coursera(Spider):
	name = 'coursera'
	start_urls=[
			'https://www.coursera.org/courses'
	]

	def start_requests(self):
		for url in self.start_urls:
			if url == 'https://www.coursera.org/courses':
				yield Request(url,callback=self.parse_courses)

	def parse_courses(self,response):
		names = response.css('.headline-1-text::text').extract()
		images = response.css('.product-photo::attr(src)').extract()
		category= response.css('.product-type-row ._1d8rgfy3::text').extract()
		rating = response.css('.ratings-text::text').extract()
		enrollment = response.css('.enrollment-number::text').extract()
		university = response.css('.m-b-1s::text').extract()
		difficulty = response.css('span.difficulty::text').extract()
		link = response.css('.rc-DesktopSearchCard::attr(href)').extract()
		yield {'names':names,'images':images,'category':category,'rating':rating,'enrollment':enrollment,'university':university,'difficulty':difficulty,'link':link}