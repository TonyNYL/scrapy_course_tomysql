# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field


# class ScrapyCourseItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     pass

class CourseItem(Item):
    #课程标题 /初识HTML + CSS
    title = Field()
    #课程URL
    # url = Field()
    #课程标题图片
    image_url = Field()
    #课程描述
    introduction = Field()
    #课程等级
    grade = Field()
    #学习人数
    student = Field()

#定义一个Item
course = CourseItem()
#赋值
course['title'] ="语文"
#取值
course['title']
course.get('title')
#获取全部键
course.keys()
#获取全部值
course.items()

