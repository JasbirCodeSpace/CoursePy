from scrapy import Spider,Request

class Coupons(Spider):
	name = 'coupons'
	start_urls = [
					'https://smartybro.com/',
					'https://comidoc.net/coupons',
					'https://udemycoupon.learnviral.com/',
					'https://www.real.discount/store/udemy/'
					]
	def start_requests(self):
		for url in self.start_urls:
			if url == 'https://smartybro.com/':
				yield Request(url , callback=self.parse_smartybro)
			elif url == 'https://comidoc.net/coupons'
				yield Request(url , callback=self.parse_comidoc)
			elif url == 'https://udemycoupon.learnviral.com/'
				yield Request(url , callback=self.parse_learnviral)
			else
				yield Request(url , callback=self.parse_realdiscount)

	def parse_smartybro(self,response):
		print(1)
	def parse_comidoc(self,response):
		print(2)
	def parse_learnviral(self,response):
		print(3)
	def parse_realdiscount(self,response):
		print(4)

