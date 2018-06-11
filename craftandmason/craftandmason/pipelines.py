from scrapy import log
from twisted.enterprise import adbapi
import time
import sys; sys.path.append("/users/user/appdata/local/programs/python/python36-32/lib/site-packages")
import MySQLdb.cursors
from craftandmason.items import CraftandmasonItem
 
class MySQLStorePipeline(object):

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

        tx.execute("select * from test where producturl = %s", (item['producturl'], ))
        result = tx.fetchone()
        if result:
            log.msg("Item already stored in db: %s" % item, level = log.DEBUG)
        else:
            tx.execute("insert into test (producturl, prodprice, prodname) values (%s, %s, %s)", [item['producturl'], item['prodprice'], item['prodname']])
            log.msg("Item stored in db: %s" %  item, level=log.DEBUG)

    def handle_error(self, e):
        print ('handle_error')
        log.err(e)