# -*- coding:UTF-8 -*-

from urllib import request, parse
import requests
import json

nlpir_url = 'http://ictclas.nlpir.org/nlpir/index4/getEmotionResult.do'

nlpir_headers = {
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
}


def nlpirEmotionPost(comment):
	try:
		r = requests.post(nlpir_url, data={'content': comment}, timeout=1)
		return json.loads(r.text, encoding='gbk')
	except:
		return None


if __name__ == "__main__":
	comment='8.5公斤，后来买了大脚象的移动底座～很静音～商品没问题，但是，坐标山西介休，最无语的是送货的，洗衣机下面有个部件根本没管（第二张图），还是我收拾箱子的时候才发现没给盖上，两人想了不伤洗衣机的办法才给盖上了～'
	ret = nlpirEmotionPost(comment)
	print(json.dumps(ret, indent=2))


