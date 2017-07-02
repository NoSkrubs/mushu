# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

import logging
import csv
import os


class Missxnspider2Spider(scrapy.Spider):
    name = 'missxnspider2'
    allowed_domains = ["sfbay.craigslist.org"]
    start_urls = ['https://sfbay.craigslist.org/search/mis']
    searchURL = 'https://sfbay.craigslist.org/search/mis'
    baseURL = 'https://sfbay.craigslist.org/'
    # dataDir = './pages'
    # totalPages = 0
    # currentPage = 0
    # reviewPages = 0

    def start_requests(self):
        logging.info('Missxnspider2Spider start_requests begin')
        yield scrapy.Request(url=self.searchURL, callback=self.searchPageScrape)


    def searchPageScrape(self, response):
        firstPage = response
        self.saveToFile(firstPage)

        soup = BeautifulSoup(firstPage.body, 'html.parser')
        postLinks = soup.find_all('a', class_='result-title hdrlnk')

        if len(postLinks) > 0:
            logging.info('Number of posts on page:' + str(len(postLinks)))

        for postLink in postLinks:
            link = str(postLink['href'])
            if link != response.url:
                yield scrapy.Request(url = self.baseURL + link, callback = self.savePosts)

    def savePosts(self, response):
        post = response
        soup = BeautifulSoup(post.body, 'html.parser')
        logging.info('Scraping post: '+ soup.head.title.get_text())
        self.saveToFile(post)

    def saveToFile(self, response):
        logging.info('Missxnspider2Spiders saveToFile begin')
        logging.info('file url=' + response.url)
        path = self.validateDir(response.url)
        logging.info('File saved at path=' + path)
        with open(path, 'w') as target:
            target.write(str(response.body))
            logging.info('Saved page')


    def validateDir(self, url):
        # create directory path for URL
        base = './pages/'
        # dirPath = ''
        fileName = url[url.rfind('/') + 1:]
        if url[:6] == 'http:/':
            dirPath = url[7:url.rfind('/') + 1]
        elif url[:7] == 'https:/':
            dirPath = url[8:url.rfind('/') + 1]
        else:
            logging.info('URL Invalid')
            return

        if not os.path.exists(base + dirPath):
            os.makedirs(base + dirPath)

        return(str(base + dirPath) + str(fileName))
