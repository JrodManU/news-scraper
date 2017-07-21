# -*- coding: utf-8 -*-
import scrapy
from items import NewsRelease

class WhitehouseYoutubeSpider(scrapy.Spider):
    name = 'whitehouse_youtube'
    start_urls = ['https://www.youtube.com/user/whitehouse/videos']

    def parse(self, response):
        items = []
        for element in response.css('h3.yt-lockup-title a.yt-uix-tile-link'):
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.youtube.com" + element.css('::attr(href)').extract_first()
            items.append(item)
        return items
