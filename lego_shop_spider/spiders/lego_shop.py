import scrapy

class LegoShopSpider(scrapy.Spider):
  name = 'lego_shop'

  def start_requests(self):
    urls = [
      'https://www.lego.com/en-lt/themes/star-wars'
    ]
    for url in urls:
      yield scrapy.Request(url=url, callback=self.parse_category)

  def parse_category(self, response):
    products_urls = response.xpath('//a[contains(@class, "ProductImagestyles__ProductImageLink")]/@href').getall()

    for url in products_urls:
      yield response.follow(url=url, callback=self.parse_product)

    next_page = response.xpath('//a[contains(@class, "Paginationstyles__NextLink")]/@href').get()
    if next_page:
      yield scrapy.Request(url=response.urljoin(next_page), callback=self.parse_category)

  def parse_product(self, response):
    name_elements = response.xpath('//h1[@data-test="product-overview-name"]/span//text()').getall()
    name = ''.join(name_elements)
        
    product_id = response.xpath('//span[@itemprop="productID"]/text()').get()

    product = {
      'name': name,
      'product_id': product_id
    }

    yield product