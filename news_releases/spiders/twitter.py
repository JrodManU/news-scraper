# -*- coding: utf-8 -*-
import scrapy
from items import NewsRelease

class TwitterSpider(scrapy.Spider):
    name = 'twitter'
    start_urls = ['https://twitter.com/whitehouse',
                  'https://twitter.com/realDonaldTrump',
                  'https://twitter.com/potus']

    def parse(self, response):
        items = []
        for element in response.css('ol#stream-items-id li div div div p'):
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = element.css('a.twitter-timeline-link::attr(href)').extract_first()
            items.append(item)
        return items
