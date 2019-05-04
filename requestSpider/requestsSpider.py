"""
__author__ = "championYang"
功能：简单使用requests实现拉勾网 关于python 职位的爬虫
并且将信息保存
难点：解决post和相关的cookie 和 requeses.Session的使用 
完成情况：暂时完成一页数据的爬取，成功保存至LaGou2.txt 文件中

"""

import requests
import time
import json
import pandas
import csv
import codecs

def getGoalData(data):
    for i in range(15): # 一页中的15条数据
        info={
            'positionName': data[i]['positionName'],    #职位简称
            'companyShortName': data[i]['companyShortName'],    #平台简称
            'salary': data[i]['salary'],    #职位薪水
            'createTime': data[i]['createTime'],    #发布时间
            'companyId':data[i]['companyId'],   #公司ID
            'companyFullName':data[i]['companyFullName'],   #公司全称
            'companySize': data[i]['companySize'],  #公司规模
            'financeStage': data[i]['financeStage'],    #融资情况
            'industryField': data[i]['industryField'],  #所在行业
            'education': data[i]['education'],  #教育背景
            'district': data[i]['district'],    #公司所在区域
            'businessZones':data[i]['businessZones']    #区域详细地
        }
        data[i]=info
    return data
'''
#保存data至csv文件   ----> 失败0.0
def saveData(data):
    table = pandas.DataFrame(data,index=[0])
    table.to_csv(r'/Users/champion/Desktop/LaGou1.csv',index=True, mode='a+')

#  将数据写入新文件  ----> 失败0.0
def data_write(file_path, datas):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet(u'sheet1',cell_overwrite_ok=True) #创建sheet
    #将数据写入第 i 行，第 j 列
    i = 0
    for data in datas:
        for j in range(len(data)):
            sheet1.write(i,j,data[j])
        i = i + 1
    f.save(file_path) #保存文件

def data_write_csv(file_name, datas):#file_name为写入CSV文件的路径，datas为要写入数据列表  ----> 失败0.0
    file_csv = codecs.open(file_name,'w+','utf-8')#追加
    writer = csv.writer(file_csv, delimiter=' ', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
    for data in datas:
        writer.writerow(data)
    print("保存文件成功，处理结束")
'''
def text_save(filename, data):#filename为写入txt文件的路径，data为要写入数据列表.  ----> 成功
    file = open(filename,'a')
    for i in range(len(data)):
        s = str(data[i]).replace('[','').replace(']','')  +'\n'#去除[]
        # s = s.replace("'",'').replace(',','') +'\n'   #去除单引号，逗号，每行末尾追加换行符
        file.write(s)
    file.close()
    print("保存文件成功") 

def main():
    url_start = "https://www.lagou.com/jobs/list_Python?city=%E5%8C%97%E4%BA%AC&cl=false&fromSearch=true&labelWords=&suginput="
    url_parse = "https://www.lagou.com/jobs/positionAjax.json?city=北京&needAddtionalResult=false"
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://www.lagou.com/jobs/list_%E8%BF%90%E7%BB%B4?city=%E6%88%90%E9%83%BD&cl=false&fromSearch=true&labelWords=&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    for x in range(1, 2):
        data = {
            'first': 'true',
            'pn': str(x),
            'kd': 'Python'
                }
        s = requests.Session()  # 返回一个session对象 这个对象代表一次用户会话：从客户端浏览器连接服务器开始，到客户端浏览器与服务器断开。会话能让我们在跨请求时候保持某些参数，比如在同一个 Session 实例发出的所有请求之间保持 cookie 。
        s.get(url_start, headers=headers, timeout=3)  # 请求首页获取cookies 返回一个响应 
        cookie = s.cookies  # 为此次获取的cookies
        # print(cookie)
        response = s.post(url_parse, data=data, headers=headers, cookies=cookie, timeout=3)  # 获取此次文本
        time.sleep(5)
        # response.encoding = response.apparent_encoding
        text = json.loads(response.text)
        info = text["content"]["positionResult"]["result"] # 返回结果在preview中的具体返回值, 到此，终于拿到了拉勾网的招聘信息了
        print("==============================")
        print(type(info))
        globalData = getGoalData(info)
        print(globalData)
        text_save(r'/Users/champion/Desktop/LaGou2.txt',globalData)

if __name__ == '__main__':
	main()

