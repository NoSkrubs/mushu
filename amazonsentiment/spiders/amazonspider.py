# -*- coding: utf-8 -*-
import scrapy


class AmazonspiderSpider(scrapy.Spider):
    name = "amazonspider"
    allowed_domains = ["amazon.com"]
    start_urls = ['http://amazon.com/']

    def parse(self, response):
        pass
