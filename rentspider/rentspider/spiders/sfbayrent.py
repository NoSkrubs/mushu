# -*- coding: utf-8 -*-
import scrapy
from pprint import pprint
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import logging
import csv
import os

class Listing(object):
    def __init__(self, resultHTML, baseURL):
        #Unique ID, repostID
        self.id = str(resultHTML['data-pid'])
        if 'data-repost-of' in resultHTML:
            self.repostId = str(resultHTML['data-repost-of'])
        else:
            self.repostId = None
        #Extract price
        priceSpan = resultHTML.find('span', class_ = 'result-price')
        if priceSpan is not None:
            priceText = priceSpan.get_text()
            cleanPrice = priceText.replace('$','')
            self.price = float(cleanPrice)
        else:
            self.price = None
        #Extract link and title
        postAnchor = resultHTML.find('a', class_ = 'result-title hdrlnk')
        self.link = baseURL + str(postAnchor['href'])
        self.title = postAnchor.get_text()
        #timestamp
        time = resultHTML.find('time', class_ = 'result-date')
        self.timestamp = str(time['datetime'])
        #housing
        housingSpan = resultHTML.find('span', class_='housing')
        if housingSpan is not None:
            self.housingInfo = housingSpan.get_text().lstrip()
        else:
            self.housingInfo = None
        #hood
        hoodSpan = resultHTML.find('span', class_ = 'result-hood')
        if hoodSpan is not None:
            self.hood = hoodSpan.get_text().lstrip()
        else:
            self.hood = None

class SfbayrentSpider(scrapy.Spider):
    name = "sfbayrent"
    allowed_domains = ["sfbay.craigslist.org"]
    start_urls = ['https://sfbay.craigslist.org/search/sfc/apa?min_price=3000&max_price=4700&min_bedrooms=3&min_bathrooms=2&availabilityMode=0']
    listings = []
    baseURL = 'https://sfbay.craigslist.org'

    def start_requests(self):
        logging.info('sfbayrentspider start request begin')
        yield scrapy.Request(url = self.start_urls[0], callback=self.scrapePage)

    def scrapePage(self, page):
        logging.info('start scrape page')
        soup = BeautifulSoup(page.body, 'html.parser')
        logging.info('retreived page: ' + soup.head.title.get_text())
        resultRows = soup.find_all('li', class_='result-row')

        #Extract total browsable posts for category
        rangeToSpan = soup.find('span', class_='rangeTo')
        if rangeToSpan is not None:
            rangeTo = int(rangeToSpan.get_text())
        else:
            rangeTo = 1000000

        totalCountSpan = soup.find('span', class_='totalcount')
        if totalCountSpan is not None:
            totalCount = int(totalCountSpan.get_text())
        else:
            totalCount = 0

        logging.info('Scraping search page for results ' + str(rangeTo) + ' of ' + str(totalCount))

        for result in resultRows:
            listing = Listing(result, self.baseURL)
            if listing not in self.listings:
                self.listings.append(listing)
                logging.info(str(listing.price) + ' hood: ' + str(listing.hood) + ' title: ' + listing.title)

        if rangeTo < totalCount:
            logging.info('grabbing next page')
            nextAnchor = soup.find('a', class_='button next')
            nextLink = str(nextAnchor['href'])
            if nextLink != page.url:
                yield scrapy.Request(url = self.baseURL + nextLink, callback = self.scrapePage)

    def closed(self, response):
        logging.info('closed spider')
        hoods = []
        for listing in self.listings:
            if listing.hood is not None and listing.hood not in hoods:
                hoods.append(listing.hood)
        for hood in hoods:
            prices = []
            for listing in self.listings:
                if listing.hood == hood and listing.price is not None:
                    prices.append(listing.price)
            # logging.info(str(hood) + ' ' + str(prices))
            average = sum(prices) / len(prices)
            logging.info(str(len(prices)) + ' listings in: ' + str(hood) + ' average price: ' + str(average))




    # def parse(self, response):
    #     pass
