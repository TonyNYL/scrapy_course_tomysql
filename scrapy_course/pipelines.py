# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import codecs
import json

from twisted.enterprise import adbapi
import pymysql.cursors
# import MySQLdb.cursors
from scrapy.crawler import Settings as settings
# class TutorialPipeline(object):

class ScrapyCoursePipeline(object):
    # def process_item(self, item, spider):
    #     return item
    # def __init__(self):
    #     # self.file = open('data.json', 'wb')
    #     # self.file = codecs.open(
    #     #     'spider.txt', 'w', encoding='utf-8')
    #     self.file = codecs.open(
    #         'spider.json', 'w', encoding='utf-8')
    #
    # def process_item(self, item, spider):
    #     line = json.dumps(dict(item), ensure_ascii=False) + "\n"
    #     self.file.write(line)
    #     return item
    #
    # def spider_closed(self, spider):
    #     self.file.close()


    def __init__(self):
        self.connect = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            db='scrapy',
            user='root',  # replace with you user name
            passwd='admin',  # replace with you password
            charset='utf8',
            # cursorclass=MySQLdb.cursors.DictCursor,
            use_unicode=True
        )
        # 通过cursor执行增删查改
        self.cursor = self.connect.cursor();
        # self.dbpool = adbapi.ConnectionPool('MySQLdb', **dbargs)

    # '''
    # The default pipeline invoke function
    # '''

    def process_item(self, item, spider):
        # res = self.dbpool.runInteraction(self.insert_into_table, item)
        # return item

        self.cursor.execute(
            """insert into scrapy_course_1(title, introduction, grade, student, image_url)
            value (%s, %s, %s, %s, %s)""",  # 纯属python操作mysql知识，不熟悉请恶补
            (item['title'],  # item里面定义的字段和表字段对应
             item['introduction'],
             item['grade'],
             item['student'],
             item['image_url']))

        # 提交sql语句
        self.connect.commit()
        return item  # 必须实现返回


    # def insert_into_table(self, conn, item):
    #     conn.execute(
    #         'insert into scrapy_source(title,introduction,grade,student,image_url) values(%s,%s,%s,%s,%s)', (
    #         item['title'], item['introduction'], item['grade'], item['student'], item['image_url']
    #         ))