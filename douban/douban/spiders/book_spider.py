
import random
from os import name

from douban.items import PopularBooks
from douban.settings import USER_AGENT
from scrapy import Request, Spider


class DoubanBookSpider(Spider):
    name = "douban_book"
    allowed_domains = ["douban.com"]
    start_urls = ["https://book.douban.com"]

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url=url,  headers={"User-Agent": random.choice(USER_AGENT)})

    def parse(self, response):

        book = response.xpath('//div[@class="bd"]/ul/li')
        items = []

        for each in book:
            item = PopularBooks()
            name = each.xpath(
                './div[@class="cover"]/a/img/@alt').extract_first()
            cover = each.xpath(
                './div[@class="cover"]/a/img/@src').extract_first()
            title = each.xpath(
                './div[@class="info"]/h4/a/text()').extract_first()
            author = each.xpath(
                './div[@class="info"]/p[@class="author"]/text()').extract_first()

            if not all([name, cover, title, author]):
                continue

            item["name"] = name
            item["cover"] = cover
            item["title"] = title
            item["author"] = author.strip().lstrip("作者：")

            yield item

        return items
