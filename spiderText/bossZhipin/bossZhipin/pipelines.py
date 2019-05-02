# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

class BosszhipinPipeline(object):
    def __init__(self):
        self.filename = open('bossData.json','wb')
    def process_item(self, item, spider):
        # 将获取到的数据保存为json格式
        print('====================================')
        print(item)
        text = json.dumps(dict(item),ensure_ascii=False) + '\n'
        self.filename.write(text.encode('utf-8'))
        return item

    def close_spider(self,spider):
        print('爬虫关闭')
        self.filename.close()