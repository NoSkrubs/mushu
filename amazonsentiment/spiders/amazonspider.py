# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
import logging
import csv
import os
import re
import html

class review(object):
    def __init__(self, text, rating):
        self.text = text
        self.rating = rating

class AmazonspiderSpider(scrapy.Spider):
    name = "amazonspider"
    allowed_domains = ["amazon.com"]
    start_urls = ['https://www.amazon.com/product-reviews/B0714QRG4Z/']
    reviewList = []

    def start_requests(self):
        logging.info('amazon spider start_requests begin')
        yield scrapy.Request(url=self.start_urls[0], callback=self.scrapePage)

    def scrapePage(self, page):
        logging.info('start scrape page')
        soup = BeautifulSoup(page.body, 'html.parser')
        logging.info('retrieved page: ' + soup.head.title.get_text())
        reviewDivs = soup.find_all('div', class_='a-section review')
        for reviewDiv in reviewDivs:
            reviewSpan = soup.find('span', class_='a-size-base review-text')
            rawtext = reviewSpan.get_text()
            # cleantext = rawtext.replace("\\","")
            reviewHook = soup.find('i', attr={'data-hook':'review-star-rating'})
            ratingText = reviewHook.span.get_text()
            rating = float(ratingText.replace(' out of 5 stars', ''))



        for span in spanList:
            rawtext = span.get_text()
            cleantext = rawtext.replace("\\","")
            self.reviewList.append(cleantext)
        logging.info('Review: '+ str(self.reviewList))

    def closed(self, response):
        self.sentimentAnalysis(self.textList)

    def sentimentAnalysis(self, textList):
        logging.info('begin sentimentAnalysis')
