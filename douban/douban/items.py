# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html


from scrapy import Field, Item


# class DoubanItem(Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     name = Field()
#     cover = Field()
#     author = Field()


class PopularBooks(Item):
    name = Field()
    title = Field()
    cover = Field()
    author = Field()


