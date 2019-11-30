# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader


from shoescraper.items import ShoeItem


class HmscraperSpider(scrapy.Spider):
    name = 'HMScraper'
    allowed_domains = ['nastygal.com']
    start_urls = ['https://www.nastygal.com/ca/womens/sale/shoes']

    def parse(self, response):
        '''gets called whenever a URL, you can use beautiful soup and extraction code in here'''
        l = ItemLoader(item = ShoeItem(), response= response)
        l.add_xpath('price','//span[@class="product-sales-price"]/text()')
        return l.load_item()
