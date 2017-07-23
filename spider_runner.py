# -*- coding: utf-8 -*-
import sys
import logging
import traceback
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from news_releases.spiders.whitehouse_statements import WhitehouseStatementsSpider
from news_releases.spiders.whitehouse_youtube import WhitehouseYoutubeSpider
from news_releases.spiders.donaldjtrump import DonaldjtrumpSpider
from news_releases.spiders.twitter import TwitterSpider

import pdb
import io
import json
import time
import logging

SPIDER_LIST = [
    WhitehouseStatementsSpider, WhitehouseYoutubeSpider, DonaldjtrumpSpider, TwitterSpider
]
class OldSpiderRunner():
    def run_spiders(self):
        try:
            ## set up the crawler and start to crawl one spider at a time
            process = CrawlerProcess(get_project_settings())
            for spider in SPIDER_LIST:
                process.crawl(spider)
            process.start()
        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            logging.info('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
            logging.info("Exception: %s" % str(traceback.format_exc()))

    def get_data(self):
        data = {}
        for spider in SPIDER_LIST:
            data_file = io.open("news_releases/results/" + spider.name + '.json', 'r+', encoding='utf-8')
            data[spider.name] = json.loads(data_file.readline())
            data_file.close()
        return data

#TODO: move this to a different file maybe? it also needs spider list as of rn
spider_runner = SpiderRunner()
previous_data = spider_runner.get_data()
spider_runner.run_spiders()
new_data = spider_runner.get_data()

data_to_post = []
for spider in SPIDER_LIST:
    for link in new_data[spider.name]:
        if link not in previous_data[spider.name]:
            data_to_post.append(link)
pdb.set_trace()
for link in data_to_post:
    logging.info("posting " + link['title'])
