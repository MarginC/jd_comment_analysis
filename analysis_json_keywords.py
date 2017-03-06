#!/usr/bin/python
# -*- coding:UTF-8 -*-

import sys
import json
from itertools import islice
import jieba
import jieba.analyse
from comment import comment

jieba.initialize()
#jieba.enable_parallel(8)
jieba.analyse.set_stop_words('./stopwords/stop_words.txt')
jieba.load_userdict('./userdict.txt')

def analysis(comment):
	seg_list = jieba.analyse.extract_tags(comment)
	if len(seg_list) > 0:
		return True, seg_list
	else:
		return False, []


if __name__ == '__main__':
	with open('./jd_comment_spider/1773994', encoding='gbk', errors='ignore') as f:
		print(','.join(comment.FIELDS))
		for line in f.readlines():
			_json = json.loads(line)
			ret, seg_list = analysis(_json['content'])
			if ret:
				c = comment.Comment()
				_json['keywords'] = "|".join(seg_list)
				c.fill(_json)
				c.matchRules(seg_list)
				print(c)

