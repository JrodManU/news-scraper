# -*- coding: utf-8 -*-
from news_releases.spider_runner import SpiderRunner
import logging
import praw
import sys

spider_runner = SpiderRunner()
previous_data = spider_runner.get_data()
spider_runner.run_spiders()
new_data = spider_runner.get_data()

data_to_post = []
for spider in spider_runner.get_spider_list():
    if(spider.name == "youtube"):
        continue
    for post in new_data[spider.name]:
        post_it = True
        for prev_post in previous_data[spider.name]:
            if post['link'] == prev_post['link']:
                post_it = False
        if(post_it):
            data_to_post.append(post)



post_data = True
if len(sys.argv) > 1:
    post_data = sys.argv[1].lower() == 'true'

if post_data and len(data_to_post) > 0:
    reddit = praw.Reddit() #reddit data in theses parentheses
    for link in data_to_post:
        reddit.subreddit("trump").submit(link["title"], url=link["link"])
