# -*- coding: utf-8 -*-
import json
import scrapy


class QuotesinfinitescrollspiderSpider(scrapy.Spider):
    name = "quotes-infinite-scroll"
    api_url = 'http://quotes.toscrape.com/api/quotes?page={}'
    start_urls = [api_url.format(1)]

    def parse(self, response):
        data = json.loads(response.text)
        for quote in data.get('quotes'):
            yield {
                'author_name': quote['author']['name'],
                'text': quote.get('text'),
                'tags': quote.get('tags')
            }

        if data.get('has_next'):
            next_page = data.get('page') + 1
            yield scrapy.Request(url=self.api_url.format(next_page), callback=self.parse)
