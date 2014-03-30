from scrapy.spider import Spider
from scrapy.selector import HtmlXPathSelector
from ret import moviename


from dirbot.items import Website

wholeadd = 'http://thepiratebay.se/search/%s/0/70' % moviename

class DmozSpider(Spider):
    name = "tpbvar"
    allowed_domains = ["thepiratebay.se"]
    start_urls = [
        "%s" % wholeadd,
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
            item['url'] = site.select('a/@href').extract()
            items.append(item)
	    #dict(item)

	return items
	#item2 = Website(items.pop(1))
	#item3 = item2['url']
	#s = item3[0]
	#return s.encode('utf')
