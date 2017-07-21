# -*- coding: utf-8 -*-
import scrapy
from items import NewsRelease

class WhitehouseYoutubeSpider(scrapy.Spider):
    name = 'whitehouse_youtube'
    start_urls = ['https://www.youtube.com/user/whitehouse/videos']

    def parse(self, response):
        items = []
        for statement in response.css('h3.yt-lockup-title a.yt-uix-tile-link'):
            item = NewsRelease()
            item['title'] = statement.css('::text').extract_first()
            item['link'] = "https://www.youtube.com" + statement.css('::attr(href)').extract_first()
            items.append(item)
        return items
