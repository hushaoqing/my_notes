# !usr/bin/python
# coding=utf-8

import re
import os
import sys
import time
import json
import requests
import scrapy
reload(sys)
sys.setdefaultencoding('utf-8')

coo = {"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.104 Safari/537.36"}

class DoubanApi(scrapy.Spider):
    """docstring for DoubanApi"""
    name = "doubanApi"
    def start_requests(self):
        urls = ["https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=20"]
        for u in urls:
            yield scrapy.Request(url=u, headers=coo, callback=self.parse)

    def parse(self, response):
        self.log("my log:{}".format(dir(response)))
        time.sleep(5)
        self.start_requests()