from scrapy import Spider,Request
import re
class Udacity(Spider):
	name = 'udacity'
	udacity_link = 'https://www.udacity.com'
	start_urls = [
		'https://www.udacity.com/courses/all'
	]

	def start_requests(self):
		for url in self.start_urls:
			if url == 'https://www.udacity.com/courses/all':
				yield Request(url,callback=self.parse_courses)

	def parse_courses(self,response):
		courses = response.css('div.card')

		for course in courses:
			name = course.css('.card-heading a::text').extract_first()
			category = course.css('.category::text').extract_first()
			difficulty = course.css('.level .capitalize::text').extract_first()
			course_type = course.css('.card.ng-star-inserted::text').extract_first()
			background_image = course.css('.image-container::attr(style)')
			if background_image:

				image = background_image.re('background-image:url(.*)')[0].strip('()')
				image = image if image else None
			link = self.udacity_link + course.css('.card-heading a::attr(href)').extract_first()
			yield {'name':name,'category':category,'difficulty':difficulty,'type':course_type,'image':image,'link':link}