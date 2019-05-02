# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BosszhipinItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # company公司名字
    company = scrapy.Field()
    # 公司信息
    company_link = scrapy.Field()
    # 职位
    position = scrapy.Field()
    # 工资
    wages = scrapy.Field()
    # 工作地点
    place = scrapy.Field()
    # 工作经验
    experience = scrapy.Field()

    # 二级页面 公司简介，在招职位数量
    company_info = scrapy.Field()
    position_num = scrapy.Field()
