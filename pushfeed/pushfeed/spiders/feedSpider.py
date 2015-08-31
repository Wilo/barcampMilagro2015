# -*- coding: utf-8 -*-
from scrapy import Spider
from scrapy.selector import Selector
from pushfeed.items import PushfeedItem

class FeedspiderSpider(Spider):
    name = "feedSpider"
    allowed_domains = ["elcomercio.com"]
    start_urls = (
        'http://www.elcomercio.com/rss',
        'http://actualidad.rt.com/feeds/all.rss',
        'http://www.eluniverso.com/rss/all.xml',
    )

    def parse(self, response):
        selector = Selector(response)
        site = selector.xpath('//channel/item')
        items = []

        for feed in site:
            pushfeed =  PushfeedItem()
            pushfeed['title'] = feed.xpath('title/text()').extract()
            pushfeed['description'] = feed.xpath('description/text()').extract()
            pushfeed['date'] = feed.xpath('pubDate/text()').extract()
            pushfeed['link'] = feed.xpath('link/text()').extract()
            pushfeed['img'] = feed.xpath('enclosure/@url').extract()
            items.append(pushfeed)
        return items
