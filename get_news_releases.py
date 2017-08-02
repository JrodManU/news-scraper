# -*- coding: utf-8 -*-
from news_releases.spider_runner import SpiderRunner
import logging
import praw
import sys
import time
import random

time.sleep(random.randint(15,100))

spider_runner = SpiderRunner()
previous_data = spider_runner.get_data()
spider_runner.run_spiders()
new_data = spider_runner.get_data()

data_to_post = []
for spider in spider_runner.get_spider_list():
    for link in new_data[spider.name]:
        if link not in previous_data[spider.name]:
            data_to_post.append(link)

post_data = True
if len(sys.argv) > 1:
    post_data = sys.argv[1].lower() == 'true'

if post_data and len(data_to_post) > 0:
    reddit = praw.Reddit(client_id='RHPMCaot0ItkNw',
                       client_secret='dOTc0gaTTmzgjLnfzFD7u0e60R0',
                       password='HGT@9iwgkuY#T*7ay28IHTpya;w3y93*Y%&T#',
                       user_agent='News Release Bot',
                       username='News_Release_Bot') #reddit data in theses parentheses
    for link in data_to_post:
        reddit.subreddit("trump").submit(link["title"], url=link["link"])
