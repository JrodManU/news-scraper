# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class YoutubeSpider(scrapy.Spider):
    name = 'youtube'
    custom_settings = {'EXPECTED': 9}
    start_urls = ['https://www.youtube.com/user/whitehouse/videos',
                  'https://www.youtube.com/user/statevideo/videos',
                  'https://www.youtube.com/user/DODvClips/videos']

    def parse(self, response):
        items = []
        for element in response.css('h3.yt-lockup-title a.yt-uix-tile-link')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.youtube.com" + element.css('::attr(href)').extract_first()
            items.append(item)
        return items
