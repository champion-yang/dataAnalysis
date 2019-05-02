# -*- coding: utf-8 -*-
import scrapy

from bossZhipin.items import BosszhipinItem

class BossSpider(scrapy.Spider):
    name = 'boss'
    allowed_domains = ['zhipin.com']

    offset = 1
    url = 'https://www.zhipin.com/c101010100-p100109/?page='
    start_urls = [ url + str(offset)]
    url1 = 'https://www.zhipin.com'
    def parse(self, response):
        for each in response.xpath("//div[@class='job-primary']"):
            item = BosszhipinItem()
            item['company'] = each.xpath("./div[@class='info-company']/div/h3/a/text()").extract()[0]
            item['company_link'] = self.url1 + each.xpath("./div[@class='info-company']/div/h3/a/@href").extract()[0]
            item['position'] = each.xpath("./div[@class='info-primary']/h3/a/div[@class='job-title']/text()").extract()[0]
            item['wages'] = each.xpath("./div[@class='info-primary']/h3/a/span[@class]/text()").extract()[0]
            item['place'] = each.xpath("./div[@class='info-primary']/p/text()").extract()[0]
            item['experience'] = each.xpath("./div[@class='info-primary']/p/text()").extract()[1]
            yield scrapy.Request(item['company_link'],meta={'item':item},callback=self.get_company_info)
        if self.offset < 10:
            self.offset += 1
        yield scrapy.Request(self.url + str(self.offset) , callback=self.parse)
        
    def get_company_info(self,response):
        item = response.meta['item']
        company_link = item['company_link']
        company_infos = response.xpath("//div[@id='main']/div[3]/div/div[2]/div/div[1]/div/text()").extract()
        position_nums = response.xpath("//div[@id='main']/div[1]/div/div[1]/div[1]/span[1]/a/b/text()").extract()
        for position_num,company_info in zip(position_nums,company_infos):
            item['position_num'] = position_num
            item['company_info'] = company_info
            print(item['position_num'],item['company_info'])
            yield item
