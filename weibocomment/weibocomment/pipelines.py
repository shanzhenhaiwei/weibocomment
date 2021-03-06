# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
import pymongo

class MongoPipeline(object):
    def __init__(self,mongo_uri,mongo_db,mongo_co):
        self.mongo_uri=mongo_uri
        self.mongo_db=mongo_db
        self.mongo_co=mongo_co

    @classmethod
    def from_crawler(cls,crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB'),
            mongo_co=crawler.settings.get('MONGO_CO'),
        )

    def open_spider(self,spider):
        self.client=pymongo.MongoClient(self.mongo_uri)
        self.db=self.client[self.mongo_db]
        self.co=self.db[self.mongo_co]

    def process_item(self,item,spider):
        self.co.create_index([('id',pymongo.ASCENDING)],unique=True)
        try:
            self.co.insert_one(dict(item))
        except:
            print('2-key error')
        return item

    def close_spider(self,spider):
        self.client.close()



