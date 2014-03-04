from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector

from dirbot.items import Website


class DmozSpider(Spider):
    name = "tpb"
    allowed_domains = ["thepiratebay.se"]
    start_urls = [
        "http://thepiratebay.se/search/mad%20max/0/7/0",
    ]

    def parse(self, response):
        """
        The lines below is a spider contract. For more info see:
        http://doc.scrapy.org/en/latest/topics/contracts.html

        @url http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/
        @scrapes name
        """
        hxs = HtmlXPathSelector(response)
        sites = hxs.select('//div[@id="main-content"]//td')        
        items = []

        for site in sites:
            item = Website()
            item['name'] = site.select('a/text()').extract()
            item['url'] = site.select('a/@href').extract()
            item['description'] = site.select('text()').re('-\s([^\n]*?)\\n')
            items.append(item)

        return items
