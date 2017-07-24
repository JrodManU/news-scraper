# -*- coding: utf-8 -*-
from news_releases.spider_runner import SpiderRunner
import logging
import praw

spider_runner = SpiderRunner()
previous_data = spider_runner.get_data()
spider_runner.run_spiders()
new_data = spider_runner.get_data()

data_to_post = []
for spider in spider_runner.get_spider_list():
    for link in new_data[spider.name]:
        if link not in previous_data[spider.name]:
            data_to_post.append(link)
for link in data_to_post:
    logging.info("posting " + link['title'])
