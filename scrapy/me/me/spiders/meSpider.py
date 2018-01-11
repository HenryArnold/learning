from scrapy.spiders import Spider
from scrapy.selector import Selector
from ..items import MeItem

class meSpider(Spider):
    name = "me"

    allowed_domains = ["youzh.me"]
    start_urls = [
        "http://www.youzh.me"
    ]

    def parse(self,  response):
        content = Selector(response)
        imageUrl = content.xpath('//div[@id="post_content_75283192143"]/img/@class').extract()
        print ("the image url is" + imageUrl)
        items['url'] = item

        for pic in images:
            item['pic'] = images.('text()').extract()
            items.append(item)
        return items
