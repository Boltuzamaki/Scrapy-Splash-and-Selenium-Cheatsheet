import logging
import urllib
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymongo
import sqlite3

class MongodbPipeline:

    collection_name  = "best_movies"

    # @classmethod
    # def from_crawler(cls, crawler):
    #     logging.warning(crawler.settings.get("MONGO_URI"))

    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb+srv://boltuzamaki:"+ urllib.parse.quote("Naruto23@#$") + "@cluster0.px2oj.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        self.db = self.client["IMDB"]

    # def open_spider(self, spider):
    #     logging.warning("SPIDER OPENED")

    # def close_spider(self, spider):
    #     logging.warning("SPIDER CLOSED FROM PIPELINE")

    
    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert(item)
        return item

class SQLLitePipeline(object):

    def open_spider(self, spider):
        self.connection = sqlite3.connect("imdb.db")
        self.c = self.connection.cursor()
        try:
            self.c.execute('''
                CREATE TABLE best_movies(
                    title VARCHAR(100),
                    year VARCHAR(100),
                    duration VARCHAR(100),
                    genre VARCHAR(100),
                    rating VARCHAR(100)
                )
            ''')
        except:
            pass
        self.connection.commit()

    def close_spider(self, spider):
        self.connection.close()

    def process_item(self, item, spider):
        self.c.execute('''
            INSERT INTO best_movies(title, year, duration, genre, rating) 
            VALUES(?,?,?,?,?)''',
            (
                item.get("title"),
                item.get("year"),
                item.get("duration"),
                item.get("genre"),
                item.get("rating")
            )
        )
        self.connection.commit()
        return item
