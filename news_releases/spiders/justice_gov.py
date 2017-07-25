# -*- coding: utf-8 -*-
import scrapy
from news_releases.items import NewsRelease

class JusticeGovSpider(scrapy.Spider):
    name = 'justice_gov'
    start_urls = ['https://www.justice.gov/blogs']

    def parse(self, response):
        items = []
        for element in response.css('article.node--blog-entry header h2 a')[:self.settings.attributes['SCRAPE_LIMIT'].value]:
            item = NewsRelease()
            item['title'] = element.css('::text').extract_first()
            item['link'] = "https://www.justice.gov" + element.css('::attr(href)').extract_first()
            items.append(item)
        return items