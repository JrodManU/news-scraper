# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import io
import os
import time

class JsonPipeline(object):

    def open_spider(self, spider):
        self.file = io.open(os.path.join(os.path.dirname(__file__), "results/" + spider.name + '.json'), 'a', encoding='utf-8')
        self.items = []

    def process_item(self, item, spider):
        self.items.append(dict(item))
        return item

    def close_spider(self, spider):
        #TODO: this is a really hacky way of fixing youtube, maybe find a better solution
        if(len(self.items) != 0 and not (spider.name == 'youtube' and len(self.items) != 9)):
            self.file.seek(0,0)
            self.file.truncate()
            self.file.seek(0,0)
            self.file.write(json.dumps(self.items, ensure_ascii=False))
            self.file.close()
       
