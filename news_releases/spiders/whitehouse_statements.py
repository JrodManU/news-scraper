# -*- coding: utf-8 -*-
import scrapy
from items import NewsRelease

class WhitehouseStatementsSpider(scrapy.Spider):
    name = 'whitehouse_statements'
    start_urls = ['https://www.whitehouse.gov/briefing-room/statements-and-releases',
                  'https://www.whitehouse.gov/blog',
                  'https://www.whitehouse.gov/briefing-room/press-briefings',
                  'https://www.whitehouse.gov/briefing-room/speeches-and-remarks']

    def parse(self, response):
        items = []
        for element in response.css('div.views-field-title h3.field-content a'):
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.whitehouse.gov" + element.css('::attr(href)').extract_first()
            items.append(item)
        return items
