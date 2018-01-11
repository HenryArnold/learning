import scrapy
from douban.items import DoubanItem

class Book250Spider(scrapy.Spider):
    name = 'book250'
    allowed_domain = ["douban.com"]
    start_urls = [
    "https://book.douban.com/top250/"
    ]

    def parse(self, response):
        for info in response.xpath('//div[]')
