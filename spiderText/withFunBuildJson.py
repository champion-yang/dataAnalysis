import json,os
import requests
from bs4 import BeautifulSoup
import time

# 获取所有的章节名和章节地址
if __name__ == '__main__':
    # 拿到url地址
    target = 'http://www.biquw.com/book/7627/'
    req = requests.get(url=target)
    # 拿到html文档
    html = req.text
    # 解析html文档信息
    div_bf = BeautifulSoup(html)  # 创建bf对象来存储html信息
    div = div_bf.find_all('div',class_='book_list')
    a_list = div_bf.select('div>ul>li>a')
    titleList1 = []
    titleList2 = []
    for each in a_list:
        # 拿到每一章的标题和连接
        str1 = each.string
        str2 = target+each.get('href')
        titleList1.append(str1)
        titleList2.append(str2)
        d = dict(zip(titleList1,titleList2))
    # print(d)
    jsonObj = json.dumps(d).encode()
    print(type(jsonObj))
    with open('build.json','wb') as f:
        f.write(jsonObj)
        