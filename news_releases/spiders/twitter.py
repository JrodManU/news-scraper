# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class TwitterSpider(scrapy.Spider):
    name = 'twitter'
    start_urls = ['https://twitter.com/potus']

    def parse(self, response):
        items = []
        for element in response.css('ol#stream-items-id li div.tweet'):
            item = NewsRelease()
            text = element.css('div.content div.js-tweet-text-container p::text').extract()
            good_text = ""
            for part in text:
                if "pic.twitter.com/" not in part:
                    good_text += part
            item['title'] = good_text
            item['link'] = 'https://twitter.com' + element.css('::attr(data-permalink-path)').extract_first()
            items.append(item)
        return items
