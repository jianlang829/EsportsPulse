'''
description: 不需要任何第三方库实现快速搜集电竞咨询
author: jianlang829
'''

import http.client, urllib, json

conn = http.client.HTTPSConnection('apis.tianapi.com')  #接口域名
params = urllib.parse.urlencode({'key':'@@@'}) # @@@替换为账号的key
headers = {'Content-type':'application/x-www-form-urlencoded'}
conn.request('POST','/esports/index',params,headers)
tianapi = conn.getresponse()

result = tianapi.read()
data = result.decode('utf-8')
dict_data = json.loads(data)
# print(dict_data)

# json格式可能改变可自行调整
if  dict_data['code'] == 200:
    for news in dict_data['result']['newslist']:
        print(news['title'])
        print(news['description'])
        print(news['url'])
        print('-' * 60)
