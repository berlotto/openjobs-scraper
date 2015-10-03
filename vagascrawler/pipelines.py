# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import rethinkdb as r


class RethinkdbPipeline(object):

    table_name = "vagas"

    def __init__(self, rdb_host, rdb_database, rdb_port):
        #Init Database connection
        self.rdb_host = rdb_host
        self.rdb_database = rdb_database
        self.rdb_port = rdb_port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            rdb_host=crawler.settings.get('RDB_HOST', 'localhost'),
            rdb_database=crawler.settings.get('RDB_DATABASE', 'vagascrawler'),
            rdb_port=crawler.settings.get('RDB_PORT', 28015)
        )

    def open_spider(self, spider):
        r.connect(self.rdb_host, self.rdb_port).repl()

    def process_item(self, item, spider):
        r.db(self.rdb_database).table(self.table_name).insert(dict(item)).run()
        return item
