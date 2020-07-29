import scrapy

class LegoShopSpider(scrapy.Spider):
  name = 'lego_shop'

  def start_requests(self):
    urls = [
      'https://www.lego.com/en-lt/themes/star-wars?page=1&sort.key=PRICE&sort.direction=ASC'
    ]
    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse_category)

  def parse_category(self, response):
    products_urls = response.xpath('//a[contains(@class, "ProductImagestyles__ProductImageLink")]/@href').getall()
    print(products_urls)