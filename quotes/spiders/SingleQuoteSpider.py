# -*- coding: utf-8 -*-
import scrapy


class SinglequotespiderSpider(scrapy.Spider):
    name = 'single-quote'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://toscrape.com/']

    def parse(self, response):
        self.log('I just visited: ' + response.url)
        for quote in response.css('div.quote'):
            item = {
                'author_name': quote.css('small.author::text').extract_first(),
                'text': quote.css('span::text').extract_first(),
                'tags': quote.css('a.tag::text').extract()
            }
            yield item
