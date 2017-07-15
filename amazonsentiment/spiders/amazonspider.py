# -*- coding: utf-8 -*-
import scrapy
from bs4 import BeautifulSoup
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize
from textblob import TextBlob
import logging
import csv
import os
import re
import html


class Review(object):
    def __init__(self, text, rating, pageTitle, url):
        self.text = text
        self.rating = rating
        self.pageTitle = pageTitle
        self.pageURL = url

    def storeSentiment(self, vader, textblob):
        self.vader = vader
        self.textblob = textblob

class AmazonspiderSpider(scrapy.Spider):
    name = "amazonspider"
    allowed_domains = ["amazon.com"]
    start_urls = ['https://www.amazon.com/product-reviews/B0714QRG4Z/ref=cm_cr_getr_d_show_all?pageNumber=1&reviewerType=all_reviews']
    reviewList = []

    def start_requests(self):
        logging.info('amazon spider start_requests begin')
        yield scrapy.Request(url=self.start_urls[0], callback=self.scrapePage)

    def scrapePage(self, page):
        logging.info('start scrape page')
        soup = BeautifulSoup(page.body, 'html.parser')
        pageTitle = soup.head.title.get_text()
        pageURL = soup.url
        logging.info('retrieved page: ' + pageTitle)
        reviewDivs = soup.find_all('div', class_='a-section review')
        for reviewDiv in reviewDivs:
            reviewSpan = reviewDiv.find('span', class_='a-size-base review-text')
            rawtext = reviewSpan.get_text()
            # cleantext = rawtext.replace("\\","")
            reviewHook = reviewDiv.find('i', attrs={'data-hook':'review-star-rating'})
            ratingText = reviewHook.span.get_text()
            rawRating = float(ratingText.replace(' out of 5 stars', ''))
            rating = (((rawRating - 1) / 4) * 2) - 1
            review = Review(rawtext, rating, pageTitle, pageURL)
            # logging.info('rating ' + str(review.rating) + ' review:' + review.text)
            self.reviewList.append(review)
        nextPageLink = soup.find('li', class_='a-last')
        if nextPageLink is not None:
            if nextPageLink.a is not None:
                link = nextPageLink.a['href']
                yield scrapy.Request(url="https://www.amazon.com" + str(link), callback=self.scrapePage)


    def closed(self, response):
        self.sentimentAnalysis(self.reviewList)

    def sentimentAnalysis(self, reviewList):
        logging.info('begin sentimentAnalysis')
        sid = SentimentIntensityAnalyzer()
        for review in reviewList:
            vaderScoreList = []
            textblobScoreList = []
            sentences = tokenize.sent_tokenize(review.text)
            # logging.info('Scoring sentences')
            for sentence in sentences:
                if len(sentence) > 1:
                    vaderScoring = sid.polarity_scores(sentence)
                    # logging.info(scoring)
                    # if review.rating < 0:
                    #     score = float(scoring["neg"]) * -1.0
                    # elif review.rating > 0:
                    #     score = float(scoring["pos"])
                    # else:
                    vaderScore = float(vaderScoring["compound"])
                    vaderScoreList.append(vaderScore)
                    textblobScore = TextBlob(str(sentence)).sentiment.polarity
                    textblobScoreList.append(textblobScore)
            averageVader = sum(vaderScoreList) / len(vaderScoreList)
            averageTextblob = sum(textblobScoreList) / len(textblobScoreList)
            review.storeSentiment(averageVader, averageTextblob)
            logging.info('review: ' + review.text[:15] + ' rating: ' + str(review.rating) + ' vader: ' + str(review.vader)[:4] + ' textblob: ' + str(review.textblob)[:4] + str(review.pageURL))
            # if review.rating < 0:
            #     logging.info('Review rating: ' + str(review.rating) + ' sentiment: ' + str(averageSentiment))
            #     logging.info(review.text)
                    # logging.info('sentence score: ' + str(compound) + " " + str(sentence))
