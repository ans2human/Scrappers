# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy import log
from twisted.enterprise import adbapi
import time
import sys; sys.path.append("/users/user/appdata/local/programs/python/python36-32/lib/site-packages")
import MySQLdb.cursors
from rvca4.items import products
from scrapy.exceptions import DropItem


class CitiesocialPipeline(object):



    def __init__(self):
        print ('init')
        self.dbpool = adbapi.ConnectionPool('MySQLdb', db = 'usalogic_testdb', user='root', passwd='1234', cursorclass=MySQLdb.cursors.DictCursor, charset='utf8', use_unicode=True)



    def process_item(self, item, spider):
        print('process')
        query = self.dbpool.runInteraction(self._conditional_insert, item)  #("""INSERT INTO Example_Movie (title, url, gross, release) VALUES (%s, %s, %s, %s)""", (item['title'].endcode('utf-8'), item['url'].encode('utf-8'), item['gross'].encode('utf-8'), item['release'].encode('utf-8')))
        query.addErrback(self.handle_error)#self.conn.commit()

        return item

    def _conditional_insert(self, tx, item):
        print ('conditional insert')
        #Create record if doesn't exist
        #all this block run on it's own thread

        tx.execute("select * from products where producturl = %s", (item['producturl'], ))
        result = tx.fetchone()
        if result:
            log.msg("Item already stored in db: %s" % item, level = log.DEBUG)
        else:
            tx.execute("insert into products (producturl, invcount, productcolor, price, prodcategory, productname) values (%s, %s, %s, %s, %s, %s)", [item['producturl'], item['invcount'], item['productcolor'], item['price'], item['prodcategory'], item['productname']])
            log.msg("Item stored in db: %s" %  item, level=log.DEBUG)

    def handle_error(self, e):
        print ('handle_error')
        log.err(e)

class DuplicatesPipeline1(object):

    def __init__(self):
        self.ids_seen = set()

    def process_item(self, item, spider):
        if item['prodname'] in self.ids_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.ids_seen.add(item['prodname'])
            return item