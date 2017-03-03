# -*- coding:UTF-8 -*-

import urllib
import urllib2
import httplib
import json

headers = {
"Host" : "ictclas.nlpir.org",
"Connection" : "keep-alive",
"Content-Length" : "4919",
"Accept" : "*/*",
"Origin" : "http://ictclas.nlpir.org",
"X-Requested-With" : "XMLHttpRequest",
"User-Agent" : "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36",
"Content-Type" : "application/x-www-form-urlencoded",
"Referer" : "http://ictclas.nlpir.org/nlpir/",
"Accept-Encoding" : "gzip, deflate",
"Accept-Language" : "zh-CN,zh;q=0.8,en;q=0.6",
"Cookie" : "JSESSIONID=B055020729EF702E7810C27A7A22B190; JSESSIONID=5A30C46272A0E4FC35C8685D3C07C650",
}

def nlpirEmotion(comment):
	postData = {'content': comment}
	dataEncode = urllib.urlencode(postData)

	requrl = 'http://ictclas.nlpir.org/nlpir/index4/getEmotionResult.do'

	conn = httplib.HTTPConnection("ictclas.nlpir.org")
	conn.request(method="POST",url=requrl,body=dataEncode,headers = headers) 
	response = conn.getresponse()
	_html = response.read().decode(encoding='utf-8', errors='strict')

	return json.loads(_html, encoding='utf-8')

def nlpirEmotionGet(comment):
	requrl = 'http://ictclas.nlpir.org/nlpir/index4/getEmotionResult.do'
	params = urllib.urlencode({'content': comment})
	req = urllib2.Request(requrl, data=params)
	res_data = urllib2.urlopen(req).read().decode(encoding='gbk', errors='strict')
	_json = json.loads(res_data, encoding='gbk')
	return _json

if __name__ == "__main__":
	comment='8.5公斤，后来买了大脚象的移动底座～很静音～商品没问题，但是，坐标山西介休，最无语的是送货的，洗衣机下面有个部件根本没管（第二张图），还是我收拾箱子的时候才发现没给盖上，两人想了不伤洗衣机的办法才给盖上了～'
	print(nlpirEmotionGet(comment))


