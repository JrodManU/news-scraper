# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import io
import pdb

class JsonPipeline(object):

    def open_spider(self, spider):
        self.file = io.open("news_releases/results/" + spider.name + '.json', 'r+', encoding='utf-8')
        self.items = []

    def process_item(self, item, spider):
        self.items.append(dict(item))
        return item

    def close_spider(self, spider):
        self.file.write(json.dumps(self.items, ensure_ascii=False))
        self.file.close()
