# -*- coding: utf-8 -*-
import sys
import logging
import traceback
from scrapy.crawler import CrawlerProcess
from scrapy.conf import settings
from scrapy.utils.project import get_project_settings
from spiders.whitehouse_statements import WhitehouseStatementsSpider
from spiders.whitehouse_youtube import WhitehouseYoutubeSpider
from spiders.donaldjtrump import DonaldjtrumpSpider
from spiders.twitter import TwitterSpider

SPIDER_LIST = [
    WhitehouseStatementsSpider, WhitehouseYoutubeSpider, DonaldjtrumpSpider, TwitterSpider
]

if __name__ == "__main__":
    try:
        ## set up the crawler and start to crawl one spider at a time
        process = CrawlerProcess(get_project_settings())
        for spider in SPIDER_LIST:
            process.crawl(spider)
        process.start()
    except Exception, e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        logging.info('Error on line {}'.format(sys.exc_info()[-1].tb_lineno))
        logging.info("Exception: %s" % str(traceback.format_exc()))
