
import scrapy

class ralphlaurenspider(scrapy.Spider):
	name = 'ralphlaurenspider'
	start_urls = ["http://www.ralphlauren.com/family/index.jsp?categoryId=2004212&cp=1760781&ab=ln_men_cs_dressshirts",
	"http://www.ralphlauren.com/shop/index.jsp?categoryId=1760782&ab=global_women",
	"http://www.ralphlauren.com/shop/index.jsp?categoryId=105240616&ab=global_boys",
	"http://www.ralphlauren.com/shop/index.jsp?categoryId=105243666&ab=global_girls",
	"http://www.ralphlauren.com/shop/index.jsp?categoryId=2048081&ab=global_baby",
	"http://www.ralphlauren.com/shop/index.jsp?categoryId=1760785&ab=global_home",
	"http://www.ralphlauren.com/shop/index.jsp?categoryId=81751386&ab=global_personalization",
	]

	def parse(self,response):
		for s in response.css('div.nav a::attr(href)'):
			print s.extract()
			yield scrapy.Request(response.urljoin(s.extract()),callback=self.parse1)
		
	def parse1(self,response):
		for li in response.css('li.product'):
			yield{
				'name':li.css('a.prodtitle::text').extract_first(),
				'price':li.css('div.money a.prodtitle::text').extract_first(),
				'image':li.css('a.photo img::attr(src)').extract_first(),

			}
		next_page = response.css('a.results::attr(href)').extract_first()
		if next_page:
			yield scrapy.Request(response.urljoin(next_page),callback=self.parse1)		


# To run scrapy runspider ralphlaurenspider.py -o file.csv -t csv
					