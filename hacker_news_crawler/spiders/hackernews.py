# -*- coding: utf-8 -*-
import scrapy


class HackernewsSpider(scrapy.Spider):
    name = 'hackernews'
    allowed_domains = ['https://news.ycombinator.com/']
    start_urls = ['https://news.ycombinator.com/']

    def start_requests(self):
        url = 'https://news.ycombinator.com/'
        yield scrapy.Request(url, self.parse_post)

    def parse_page(self, response):

        for item in response.xpath('//tr[@class="athing"]'):
            topic_id = item.xpath('@id').extract_first()
            topic = item.xpath('.//a[@class="storylink"]/text()').extract_first()
            orig_link = item.xpath('.//a[@class="storylink"]/@href').extract_first()

            yield response.follow()
        
        pass

    def parse_post(self, response):
        pass