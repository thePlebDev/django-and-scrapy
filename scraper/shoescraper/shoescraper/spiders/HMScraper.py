# -*- coding: utf-8 -*-
import scrapy


class HmscraperSpider(scrapy.Spider):
    name = 'HMScraper'
    allowed_domains = ['hm.com']
    start_urls = ['http://hm.com/']

    def parse(self, response):
        pass
