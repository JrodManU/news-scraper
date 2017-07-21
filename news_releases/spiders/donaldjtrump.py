# -*- coding: utf-8 -*-
import scrapy
from items import NewsRelease

class DonaldjtrumpSpider(scrapy.Spider):
    name = 'donaldjtrump'
    start_urls = ['https://www.donaldjtrump.com/media/']

    def parse(self, response):
        items = []
        for statement in response.css('article.press-post h3 a'):
            item = NewsRelease()
            item['title'] = statement.css('::text').extract_first()
            item['link'] = "https://www.donaldjtrump.com" + statement.css('::attr(href)').extract_first()
            items.append(item)
        return items
