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

def test1():
	with open('./jd_comment_spider/1309864.csv') as f:
		reader = csv.reader(f)
		nwordall = []
		for row in islice(reader, 1, None):
			comment = row[11]
			words = pseg.cut(comment)
			nword = ['']
			for w in words:
				if (w.flag == 'n' or w.flag == 'v' or w.flag == 'a') and len(w.word) > 1:
					nword.append(w.word)
			nwordall.append(nword)

		dictionary = corpora.Dictionary(nwordall)
		corpus = [dictionary.doc2bow(text) for text in nwordall]
		tfidf = models.TfidfModel(corpus)
		corpus_tfidf = tfidf[corpus]

		lda = models.ldamodel.LdaModel(corpus=corpus_tfidf, id2word=dictionary, num_topics=100, update_every=0, passes=20)
#		for i in range(0, 100):
#			print(lda.print_topics(i)[0][1])

		model = models.word2vec.Word2Vec(nwordall, size=100, window=5, min_count=5, workers=8)
		model.save("./word2vecmodels")
		model = models.word2vec.Word2Vec.load("./word2vecmodels")

		sim = model.most_similar(positive=[u'动力'])
		for s in sim:
			print("word:%s,similar:%s " % (s[0], s[1]))

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
