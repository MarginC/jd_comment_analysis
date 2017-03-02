#!/usr/bin/python
# -*- coding:UTF-8 -*-

import csv
from itertools import islice
import jieba
import jieba.analyse
import jieba.posseg as pseg
from gensim import corpora, models, similarities

jieba.initialize()
jieba.enable_parallel(8)
jieba.analyse.set_stop_words('./stopwords/stop_words.txt')
jieba.load_userdict('./userdict.txt')

def test2():
	stopkey=[line.strip().decode('utf-8') for line in open('./stopwords/stop_words.txt').readlines()]
	with open('./jd_comment_spider/1309864.csv') as f:
		reader = csv.reader(f)
		for row in islice(reader, 1, None):
			comment = row[11]
			#seg_list = jieba.cut(comment)
			#print("|".join(list(set(seg_list)-set(stopkey))))
			seg_list = jieba.analyse.extract_tags(comment)
			#print('|'.join(seg_list[0]))
			print("|".join(seg_list))

if __name__ == '__main__':
	test2()
