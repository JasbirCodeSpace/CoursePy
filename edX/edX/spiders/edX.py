from scrapy import Spider,Request

class EDX(Spider):
	name = 'edx'
	edx_link = 'https://www.edx.org/'
	start_urls = [
		'https://www.edx.org/search?tab=course'
	]

	def start_requests(self):
		for url in self.start_urls:
			if url == 'https://www.edx.org/search?tab=course':
				yield Request(url,callback=self.parse_courses)

	def parse_courses(self,response):
		courses = response.css('.d-card-wrapper')
		for course in courses:
			name = course.css('.d-card-body h3::text').extract_first()
			print(course.css('.d-card-body h3 span span::text').extract_first())
			university = course.css('.provider span::text').extract_first()
			category = course.css('.card-type span::text').extract_first()
			image = course.css('.d-card-hero img::attr(src)').extract_first()

			yield{'name':name,'university':university,'category':category,'image':image}


