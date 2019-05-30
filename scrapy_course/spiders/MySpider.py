# -*- coding:utf8-*-
import scrapy
import sys
import time
reload(sys)
sys.setdefaultencoding('utf-8')
from scrapy_course.items import  CourseItem
from scrapy.selector import Selector
sys.stdout = open('output.txt', 'w')
pageIndex = 0

class MySpider(scrapy.Spider):
    # 用于区别Spider
    name = "MySpider"
    # 允许访问的区域
    allowed_domains = ['imooc.com']
    # 爬取的地址
    start_urls = ["http://www.imooc.com/course/list"]
    # 爬取的方法
    def parse(self, response):
        # pass

        # 实例一个容器保存爬取的信息
        item = CourseItem()
        # 这部分是爬取部分，使用xpath的方式选择信息，具体方法根据网页结构而定
        # 先获取每个课程的div
        sel = Selector(response)
        title = sel.xpath('/html/head/title/text()').extract()  # 标题
        print title[0]
        sels = sel.xpath('//div[@class="course-card-content"]')
        # sels = sel.xpath('//div[@class="course-card"]')
        pictures = sel.xpath('//div[@class="course-card-top"]')
        index = 0
        global pageIndex
        pageIndex += 1
        print u'%s' % (time.strftime('%Y-%m-%d %H-%M-%S'))
        print '第' + str(pageIndex) + '页 '
        print '----------------------------------------------------'
        for box in sels:
            print ' '
            # 获取div中的课程标题
            item['title'] = box.xpath('.//h3[@class="course-card-name"]/text()').extract()[0].strip()
            print '课程标题：' + item['title']

            # 获取div中的课程简介
            item['introduction'] = box.xpath('.//p/text()').extract()[0].strip()
            print '课程简介：' + item['introduction']

            # 获取每个div中的课程路径
            # item['url'] = 'http://www.imooc.com' + box.xpath('.//@href').extract()[0]
            # print  '路径：' + item['url']

            # 获取div中课程的等级
            item['grade'] = box.xpath('.//div[@class="course-card-info"]/span[1]/text()').extract()[0].strip()
            print '课程等级：' + item['grade']

            #获取div中的学生人数
            item['student'] = box.xpath('.//div[@class="course-card-info"]/span[2]/text()').extract()[0].strip()
            print '观看人数：' + item['student']

            # 获取div中的标题图片地址
            item['image_url'] = 'http:' + pictures[index].xpath('.//img/@src').extract()[0]
            print '图片地址：' + item['image_url']
            index += 1
            yield item

        time.sleep(1)
        print u'%s' % (time.strftime('%Y-%m-%d %H-%M-%S'))
        next =u'下一页'
        url = response.xpath("//a[contains(text(),'" + next + "')]/@href").extract()
        if url:
            # 将信息组合成下一页的url
            page = 'http://www.imooc.com' + url[0]
            # 返回url
            yield scrapy.Request(page, callback=self.parse)