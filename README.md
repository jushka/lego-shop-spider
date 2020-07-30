# Lego.com shop spider

This is a spider built with Scrapy framework that scrapes product info from https://www.lego.com/ shop.

Spider scrapes product's name, id, category, age group, pieces count and price.

I've made it only for learning purposes and because I love what Lego does!

# How to use it

Insert links of the categories you're interested in into `urls` variable in `lego_shop_spider/spiders/lego_shop.py` like that:
```
urls = [
  'https://www.lego.com/en-lt/themes/star-wars',
  'https://www.lego.com/en-lt/themes/city'
]
```
Run a spider by using `scrapy crawl` command like that:
```
$ scrapy crawl lego_shop
```
Spider will go through all pages of specified categories and will collect links to products. Then it will follow those links to products pages and scrape info about them. Scraped data will be saved to `lego_products.csv` file. Data will look like that:
```
name,product_id,category,age_group,pieces,price
Millennium Falcon™,75192,Star Wars™,16+,7541,899.00
Sith TIE Fighter™,75272,Star Wars™,9+,470,84.99
First Order Stormtrooper™,40391,Star Wars™,8+,151,21.99
```
Now you can analyze your newly acquired data! For example, I've used this data to find currently sold Lego sets with lowest price per piece :)
