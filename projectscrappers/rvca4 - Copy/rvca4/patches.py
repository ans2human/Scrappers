# import sys
# import MySQLdb
# import hashlib
# from scrapy.exceptions import DropItem
# from scrapy.http import Request
# from scrapy.item import Item, Field
# from scrapy import log
# from twisted.enterprise import adbapi
# import MySQLdb.cursors



# class MySQLStorePipeline(object):


#     def __init__(self):
#         self.dbpool = adbapi.ConnectionPool('MySQLdb', db='usalogic_testdb',
#                 user='root', passwd='1234', cursorclass=MySQLdb.cursors.DictCursor,
#                 charset='utf8', use_unicode=True)
 
#     def process_item(self, item, spider):
#         # run db query in thread pool
#         query = self.dbpool.runInteraction(self._conditional_insert, item)
#         query.addErrback(self.handle_error)
 
#         return item
 
#     def _conditional_insert(self, tx, item):
#         # create record if doesn't exist. 
#         # all this block run on it's own thread
#         tx.execute("select * from test where link = %s", (item['link'], ))
#         result = tx.fetchone()
#         if result:
#             log.msg("Item already stored in db: %s" % item, level=log.DEBUG)
#         else:
#             tx.execute(\
#                 "INSERT INTO test (link) "
#                 "values (%s)",
#                (item['link'].encode('utf-8'))
#             )
#             log.msg("Item stored in db: %s" % item, level=log.DEBUG)
 
#     def handle_error(self, e):
#         log.err(e)
 

    # def __init__(self, dbpool):
    #     self.dbpool = dbpool

    # @classmethod
    # def from_settings(cls, settings):
    #     dbargs = dict(
    #         host=settings['MYSQL_HOST'],
    #         db=settings['MYSQL_DBNAME'],
    #         user=settings['MYSQL_USER'],
    #         passwd=settings['MYSQL_PASSWD'],
    #         charset='utf8',
    #         use_unicode=True,
    #     )
    #     dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)
    #     return cls(dbpool)

    # def process_item(self, item, spider):
    #     d = self.dbpool.runInteraction(self._do_upsert, item, spider)
    #     d.addErrback(self._handle_error, item, spider)
    #     d.addBoth(lambda _: item)
      
    #     return d

    # def _do_upsert(self, conn, item, spider):
    #     """Perform an insert or update."""
    #     id = self._get_id(item)

    #     conn.execute("""SELECT EXISTS(
    #         SELECT 1 FROM products WHERE id = %s
    #     )""", (id,))
    #     ret = conn.fetchone()

    #     if ret:
    #         conn.execute("""
    #             UPDATE products
    #             productname=%s, price=%s, producturl=%s, productcolor=%s, invcount=%s, prodcategory=%s,
    #             WHERE id=%s
    #         """, (item['productname'], item['price'], item['producturl'], item['productcolor'], item['invcount'], item['prodcategory'], id))
    #         spider.log("Item updated in db: %s %r" % (id, item))
    #     else:
    #         conn.execute("""
    #             INSERT INTO products (id, productname, price, producturl, productcolor, invcount, prodcategory)
    #             VALUES (%s, %s, %s, %s %s, %s)
    #         """, (id, conn.escape_string(item['productname']), item['price'], item['producturl'], item['productcolor'], item['invcount'], item['prodcategory']))
    #         spider.log("Item stored in db: %s %r" % (id, item))

    # def _handle_error(self, failure, item, spider):
    #     """Handle occurred on db interaction."""
    #     log.err(failure)

    # def _get_id(self, item):
    #     """Generates an unique identifier for a given item."""
    #     return md5(item['producturl'].encode("utf8")).hexdigest()











#     from scrapy import log
# from twisted.enterprise import adbapi
# import time
# import sys; sys.path.append("/users/user/appdata/local/programs/python/python36-32/lib/site-packages")
# import MySQLdb.cursors

# class MySQLStorePipeline(object):

#     def __init__(self):
#         print ('init')
#         self.dbpool = adbapi.ConnectionPool('MySQLdb', db = 'usalogic_testdb', user='root', passwd='1234', cursorclass=MySQLdb.cursors.DictCursor, charset='utf8', use_unicode=True)



#     def process_item(self, item, spider):
#         print('process')
#         query = self.dbpool.runInteraction(self._conditional_insert, item)  #("""INSERT INTO Example_Movie (title, url, gross, release) VALUES (%s, %s, %s, %s)""", (item['title'].endcode('utf-8'), item['url'].encode('utf-8'), item['gross'].encode('utf-8'), item['release'].encode('utf-8')))
#         query.addErrback(self.handle_error)#self.conn.commit()

#         return item

#     def _conditional_insert(self, tx, item):
#         print ('conditional insert')
#         #Create record if doesn't exist
#         #all this block run on it's own thread

#         tx.execute("select * from test where url = %s", (item['url'], ))
#         result = tx.fetchone()
#         if result:
#             log.msg("Item already stored in db: %s" % item, level = log.DEBUG)
#         else:
#             tx.execute("insert into test (url) values (%s)", (item['url'].encode('utf-8')))
#             log.msg("Item stored in db: %s" %  item, level=log.DEBUG)

#     def handle_error(self, e):
#         print ('handle_error')
#         log.err(e)