import requests,json

url = "http://xsxxgk.huaibei.gov.cn/site/label/8888?IsAjax=1&dataType=html&_=0.27182235250895626"
data ={
    "siteId":"4704161",
    "pageSize":"15",
    "pageIndex":"4",
    "action":"list",
    "isDate":"true",
    "dateFormat":"yyyy-MM-dd",
    "length":"46",
    "organId":"33",
    "type":"4",
    "catId":"3827899",
    "cId":"",
    "result":"暂无相关信息",
    "labelName":"publicInfoList",
    "file":"/xsxxgk/publicInfoList-xs"
}
headers = {
    "Accept":"text/html, */*; q=0.01","Accept-Encoding":"gzip, deflate",
    "Accept-Language":"zh-CN,zh;q=0.9,en;q=0.8",
    "Connection":"keep-alive",
    "Content-Length":"253",
    "Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie":"SHIROJSESSIONID=f30feb26-6495-4287-a5a6-27bbd76bf960",
    "Host":"xsxxgk.huaibei.gov.cn",
    "Origin":"http",
    "Referer":"http",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36",
    "X-Requested-With":"XMLHttpRequest"
}
response = requests.post(url=url,data =data,headers=headers)
# response = requests.post(url=url,data =json.dumps(data),headers=headers) # 注意請求的方式是json还是text
print(response.text)