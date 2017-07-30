# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy.utils.project import get_project_settings

import logging
import os

class JulyspiderSpider(scrapy.Spider):
    name = 'julyspider'
    allowed_domains = ['sfbay.craigslist.org']
    start_urls = ['https://sfbay.craigslist.org/search/bik']

    searchURL = 'https://sfbay.craigslist.org/search/bik'
    baseURL = 'https://sfbay.craigslist.org'

    def start_requests(self):
        #like print
        logging.info("bikespider start request")
        #what you are sending in and what to do when you get it back
        yield scrapy.Request(url=self.searchURL, callback=self.scrapePostsPage)

    def scrapePostsPage(self, page):
        html = BeautifulSoup(page.body, 'html.parser')
        postLinks= html.find_all('a', attrs={'class':'result-title hdrlnk'})
        for link in postLinks:
            logging.info(link.get_text())
            hyperlink = str(link['href'])
            postURL = self.baseURL + hyperlink
            yield scrapy.Request(url = postURL, callback=self.scrapePost)


    def scrapePost(self, post):
        soup = BeautifulSoup(post.body, 'html.parser')
        descriptionSection = soup.find('section', attrs = {'id':'postingbody'})
        logging.info(descriptionSection.get_text())


    #def parse(self, response):
        #pass
