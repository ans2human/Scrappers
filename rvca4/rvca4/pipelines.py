#import pymongo
import csv
from scrapy.conf import settings
from scrapy.exceptions import DropItem
from scrapy import log


# class Rvca4Pipeline(object):

#     def __init__(self):
#         connection = pymongo.MongoClient(
#             settings['MONGODB_SERVER'],
#             settings['MONGODB_PORT']
#         )
#         db = connection[settings['MONGODB_DB']]
#         self.collection = db[settings['MONGODB_COLLECTION']]

#     def process_item(self, item, spider):
#         valid = True
#         for data in item:
#             if not data:
#                 valid = False
#                 raise DropItem("Missing {0}!".format(data))
#         if valid:
#             self.collection.insert(dict(item))
#             log.msg("Product added to MongoDB database!",
#                     level=log.DEBUG, spider=spider)
#         return item



class CsvWriterPipeline(object):
    @classmethod
    def from_crawler(cls, crawler):
        settings = crawler.settings
        file_name = settings.get("FILE_NAME")
        return cls(file_name)

    def __init__(self, file_name):
        header = ["URL"]
        self.csvwriter = csv.writer(open(file_name, 'w+'))
        self.csvwriter.writerow(header)

    def process_item(self, item, internallinkspider):
        # build your row to export, then export the row
        row = [item['url']]
        self.csvwriter.writerow(row)
        return item