import scrapy


class PepParseItem(scrapy.Item):
    """Класс, описывающий item-объекты для PEP."""

    number = scrapy.Field()
    name = scrapy.Field()
    status = scrapy.Field()
