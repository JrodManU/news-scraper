# -*- coding: utf-8 -*-
import sys
import logging
import traceback
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from spiders.whitehouse_statements import WhitehouseStatementsSpider
from spiders.whitehouse_youtube import WhitehouseYoutubeSpider
from spiders.donaldjtrump import DonaldjtrumpSpider
from spiders.twitter import TwitterSpider
from spiders.dhs_gov import DHSGovSpider

import io
import json

class SpiderRunner():
    def __init__(self):
        self.SPIDER_LIST = [
            WhitehouseStatementsSpider, WhitehouseYoutubeSpider, DonaldjtrumpSpider, TwitterSpider, DHSGovSpider
        ]

    def run_spiders(self):
        try:
            ## set up the crawler and start to crawl one spider at a time
            process = CrawlerProcess(get_project_settings())
            for spider in self.SPIDER_LIST:
                process.crawl(spider)
            process.start()
        except Exception:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            logging.info('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
            logging.info("Exception: %s" % str(traceback.format_exc()))

    def get_data(self):
        data = {}
        for spider in self.SPIDER_LIST:
            data_file = None
            data[spider.name] = []
            try:
                data_file = io.open("news_releases/results/" + spider.name + '.json', 'r', encoding='utf-8')
                line = data_file.readline()
                if not line == u'':
                    data[spider.name] = json.loads(line)
            except Exception:
                data_file = io.open("news_releases/results/" + spider.name + '.json', 'w', encoding='utf-8')
            data_file.close()
        return data

    def get_spider_list(self):
        return self.SPIDER_LIST
