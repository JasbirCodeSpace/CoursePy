from scrapy import Spider,Request
from urllib.parse import urlparse
from urllib.parse import parse_qs

class Coursera(Spider):
	name = 'coursera'
	coursera_link = 'https://www.coursera.org' 
	page_number = 1
	start_urls=[
			'https://www.coursera.org/courses?page=1&index=prod_all_products_term_optimization'
	]

	def start_requests(self):
		for url in self.start_urls:
			if url == 'https://www.coursera.org/courses?page=1&index=prod_all_products_term_optimization':
				yield Request(url,callback=self.parse_courses)

	def parse_courses(self,response):
		if self.page_number == 1:
			total_courses = response.css('.rc-NumberOfResultsSection span::text').extract_first()
			count = int([int(s) for s in total_courses.split() if s.isdigit()][0]/10)+1
			self.page_count = count
		courses = response.css('.anchor-wrapper')
		for course in courses:
			name = course.css('.headline-1-text::text').extract_first()
			image = course.css('.product-photo::attr(src)').extract_first()
			category= course.css('.product-type-row ._1d8rgfy3::text').extract_first()
			rating = course.css('.ratings-text::text').extract_first()
			enrollment = course.css('.enrollment-number::text').extract_first()
			university = course.css('.m-b-1s::text').extract_first()
			difficulty = course.css('span.difficulty::text').extract_first()
			link = self.coursera_link + course.css('.rc-DesktopSearchCard::attr(href)').extract_first()
			yield {'name':name,'image':image,'category':category,'rating':rating,'enrollment':enrollment,'university':university,'difficulty':difficulty,'link':link}

		if self.page_number <= self.page_count:
			self.page_number += 1
			next_page = 'https://www.coursera.org/courses?page={page}&index=prod_all_products_term_optimization'.format(page=self.page_number)
			yield response.follow(next_page,callback=self.parse_courses)
