# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class QuotesjsspiderSpider(scrapy.Spider):
    name = 'quotesjs'
    allowed_domains = ['toscrape.com']
    srape_url = 'http://quotes.toscrape.com/js'

    def start_requests(self):
        yield SplashRequest(url=self.srape_url, callback=self.parse)

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                'text': quote.css("span.text::text").extract_first(),
                'author': quote.css("small.author::text").extract_first(),
                'tags': quote.css("div.tags > a.tag::text").extract(),
            }

