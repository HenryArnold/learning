import scrapy
from douban.items import DoubanItem

class Movie250Spider(scrapy.Spideer):
    """docstring for Movie250Spider"""
    name = 'movie250'
    allowed_domain = ["douban.com"]
    start_urls = [
      "http://movie.doubancom/top250/"
    ]
    def parse(self, response):
        for info in response.xpath('//div[@class="item"]'):
            item = DoubanItem()
            item['rank'] = info.xpath('div[@class="pic"]')
