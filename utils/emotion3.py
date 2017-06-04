# -*- coding:UTF-8 -*-

import codecs
import requests
import json

nlpir_url = 'http://ictclas.nlpir.org/nlpir/index4/getEmotionResult.do'


def nlpirEmotionPost(comment):
	r = requests.post(nlpir_url, data={'content': comment}, timeout=1)
	return json.loads(r.text, encoding='gbk')


def emotionCompute(emotion):
	stnResult = json.loads(emotion['stnResult'])
	json0 = stnResult['json0']
	negativepoint = float(json0['negativepoint'])
	positivepoint = float(json0['positivepoint'])
	ret = int(negativepoint / (positivepoint + 1) * 50)
	a, b = divmod(abs(ret), 10)
	if b > 4:
		a += 1
	if a > 5:
		a = 5
	return a


def emotionLoad(filename):
	emotions = {}
	with codecs.open(filename, 'r', encoding='utf-8') as f:
		for line in f.readlines():
			_json = json.loads(line)
			for id in _json:
				emotions[id] = emotionCompute(_json[id])
	return emotions


if __name__ == "__main__":
	comment='8.5公斤，后来买了大脚象的移动底座～很静音～商品没问题，但是，坐标山西介休，最无语的是送货的，洗衣机下面有个部件根本没管（第二张图），还是我收拾箱子的时候才发现没给盖上，两人想了不伤洗衣机的办法才给盖上了～'
	ret = nlpirEmotionPost(comment)
	print(json.dumps(ret, indent=2))

	emotions = emotionLoad('../output/emotion/emotion.txt')
