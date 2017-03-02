# -*- coding:UTF-8 -*-

import urllib
import httplib
import json

comment='8.5公斤，后来买了大脚象的移动底座～很静音～商品没问题，但是，坐标山西介休，最无语的是送货的，洗衣机下面有个部件根本没管（第二张图），还是我收拾箱子的时候才发现没给盖上，两人想了不伤洗衣机的办法才给盖上了～'

postData = {'api':'12','body_data':{'content':comment}}
dataEncode = urllib.urlencode(postData)

requrl = 'http://nlp.qq.com/public/wenzhi/api/common_api1469449716.php'
headers = {
"Host" : " nlp.qq.com",
"Connection" : " keep-alive",
"Content-Length" : " 948",
"Accept" : " application/json, text/javascript, */*; q=0.01",
"Origin" : " http://nlp.qq.com",
"X-Requested-With" : " XMLHttpRequest",
"User-Agent" : " Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
"Content-Type" : " application/x-www-form-urlencoded; charset=UTF-8",
"Referer" : " http://nlp.qq.com/semantic.cgi",
"Accept-Encoding" : " gzip, deflate",
"Accept-Language" : " zh-CN,zh;q=0.8,en;q=0.6",
"Cookie" : " eas_sid=x1e4d8S6R8j1D408Z5s8H2x8U8; tvfe_boss_uuid=a7b0d4fb332d6613; qz_gdt=flskmwblamamx5xkhe6q; pt2gguin=o1028519445; uin=o1028519445; ptisp=cm; RK=3UVz9odqWl; ptcz=756fd3bd99ad9fa6d9c6a26f0cc726d793c2effa93c89e898930cee1cbc3926d; o_cookie=1028519445; pgv_info=pgvReferrer=&ssid=s4962614764; pgv_pvid=9763118144; pgv_pvi=9291804672; pgv_si=s9926327296",
}

conn = httplib.HTTPConnection("nlp.qq.com")
conn.request(method="POST",url=requrl,body=dataEncode,headers = headers) 
response = conn.getresponse()
_html = response.read().decode(encoding='utf-8', errors='strict')

_json = json.loads(_html, encoding='utf-8')

print(_json)


