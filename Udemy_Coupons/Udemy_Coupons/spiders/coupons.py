from scrapy import Spider,Request
import urllib.parse as urlparse
from urllib.parse import parse_qs

from ..items import UdemyCouponsItem

class Coupons(Spider):
	name = 'coupons'
	start_urls = [
					'https://smartybro.com/category/udemy-coupon-100-off/',
					'https://comidoc.net/coupons',
					# 'https://udemycoupon.learnviral.com/',
					# 'https://www.real.discount/store/udemy/'
					]
	def start_requests(self):
		for url in self.start_urls:
			if url == 'https://smartybro.com/category/udemy-coupon-100-off/':
				yield Request(url , callback=self.parse_smartybro)
			elif url == 'https://comidoc.net/coupons':
				yield Request(url , callback=self.parse_comidoc)
			# elif url == 'https://udemycoupon.learnviral.com/':
			# 	yield Request(url , callback=self.parse_learnviral)
			# else :
			# 	yield Request(url , callback=self.parse_realdiscount)

	def parse_smartybro(self,response):
		all_items = response.css('div.item')

		for href in all_items.xpath('//a[@class="more-link"]/@href'):
			url = response.urljoin(href.extract())
			yield Request(url, callback = self.parse_smartybro_each_page)

		# not running pagination because the old posts contains expired coupons
		# next_page = response.css('a.next::attr(href)').get()
		# if next_page is not None:
		# 	yield response.follow(next_page,callback = self.parse_smartybro)

	def parse_smartybro_each_page(self,response):
		items = UdemyCouponsItem()
		items['site'] = 'SmartyBro'
		items['link'] = response.css('a.fasc-type-flat::attr(href)').extract_first()
		items['name'] = response.css('span.entry-title::text').extract_first()
		items['tags'] = response.xpath('//a[@rel="tag"]/text()').extract()
		parameters = parse_qs(urlparse.urlparse(items['link']).query)
		items['code'] = parameters['couponCode'][0] if 'couponCode' in parameters else "N/A"

		return items

		
	def parse_comidoc(self,response):
		all_items = response.css('div.Coupons__List-sc-181j6ri-1 a::attr(href)').extract()
		for href in all_items:
			url = response.urljoin(href)
			yield Request(url , callback= self.parse_comidoc_each_page)
			
	def parse_comidoc_each_page(self,response):
		items = UdemyCouponsItem()
		items['site'] = 'Comidoc'
		items['name'] = response.css('h2.selectorgadget_selected').extract_first()
		items['tags'] = response.css('div.hvbkPj+ div p::text').extract()
		temp  = response.xpath('//script[@id="__NEXT_DATA__"]/text()').extract_first().split(',')
		items['code'] = [s for s in temp if "code" in s][0].split(':')[1].strip('"')
		items['link'] = "https://www.udemy.com/course/"+[s for s in temp if "cleanUrl" in s][0].split(':')[-1].strip('"').strip('}')+"?couponCode="+items['code']
		print("comidoc",items)
		return items



	# def parse_learnviral(self,response):
	# 	print(3)
	# def parse_realdiscount(self,response):
	# 	print(4)

