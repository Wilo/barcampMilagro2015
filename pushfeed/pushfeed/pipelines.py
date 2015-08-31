# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging

from scrapy.conf import settings
from scrapy.exceptions import DropItem

import rethinkdb as r


#class PushfeedPipeline(object):
#    def process_item(self, item, spider):
#        return item

class RethinkdbPipeline(object):
    """docstring for RethinkdbPipeline"""
    def __init__(self):
        r.connect(settings['RETHINKDB_SERVER'], settings['RETHINKDB_PORT']).repl()
        self.db = r.db(settings['RETHINKDB_DB']).table(settings['RETHINKDB_TABLE'])

    def process_item(self, item, spider):
        for data in item:
            if not data:
                raise DropItem
        data = dict(title=item['title'][0], description=item['description'][0],
                    date=item['date'][0], link=item['link'][0], img=item['img'][0])
        self.db.insert(data).run()
        logging.log(logging.INFO,"Feed added to rethinkdb database!")
        return item
