import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_DOMAIN


class PepSpider(scrapy.Spider):
    """Парсер PEP."""

    name = 'pep'
    allowed_domains = [PEP_DOMAIN]
    start_urls = [f'https://{PEP_DOMAIN}/']

    def parse(self, response):
        """
        Собирает ссылки на все PEP,
        вызывает переход на каждую из страниц.
        """
        all_peps = response.css('#numerical-index a[href^="pep-"]::attr(href)')
        for pep_link in all_peps:
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        """Собирает данные со страницы PEP."""
        header = ''.join(response.xpath('//article//h1//text()').getall())
        number, name = header.split(' – ', 1)
        yield PepParseItem(
            {
                'number': int(number.split()[-1]),
                'name': name,
                'status': response.css(
                    'dt:contains("Status") + dd abbr::text').get(),

            }
        )
