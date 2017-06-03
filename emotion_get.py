#!/usr/bin/python
# -*- coding:UTF-8 -*-

import codecs
import cProfile
import pstats
import json
import time
import sys
from optparse import OptionParser
from utils import emotion3 as emotion


def init_parser():
	parser = OptionParser()
	parser.add_option('-i', '--input', action='store', dest='input',
		help='set the input filename', metavar='FILE')
	parser.add_option('--encoding', action='store', dest='encoding',
		default='utf-8', help='set the encoding of input filename')
	parser.add_option('--count', action='store', dest='max_count',
		default=sys.maxsize, help='set the max count to process')
	parser.add_option('--emotion', action='store', dest='emotion',
		default='./output/emotion/emotion.txt', help='set the emotion filename', metavar='FILE')
	parser.add_option('--log', action='store', dest='logfile',
		default='./output/emotion/failed.json', help='set the log file')
	parser.add_option('--statistics', action='store', dest='statistics',
		default='./output/emotion/statistic', help='set the statistics file')
	return parser.parse_args()


def main():
	(options, args) = init_parser()
	deduplication = {}
	statistic = {}
	count = 0

	input_file = codecs.open(options.input, 'r', encoding=options.encoding, errors='strict')
	failed_file = codecs.open(options.logfile, 'w', encoding='utf-8')
	statistics_file = codecs.open(options.statistics, 'w', encoding='utf-8')
	emotion_file = codecs.open(options.emotion, 'w', encoding='utf-8')

	for line in input_file.readlines():
		try:
			_json = json.loads(line)
			if 'id' in _json:
				id = _json['id']
			elif 'commentId' in _json:
				id = _json['commentId']
			else:
				raise IndexError
			comment = _json['content']
		except:
			failed_file.write(line)
			continue

		if id in deduplication:
			continue
		deduplication[id] = True
		if len(comment) < 10:
			continue

		if divmod(count, 100)[1] == 0:
			print('process {0} comments, {1}'.format(count, time.process_time()))
		try:
			emotion_ret = emotion.nlpirEmotionPost(comment)
		except:
			failed_file.write(line)
			continue

		ret = {id: emotion_ret}
		emotion_file.write(json.dumps(ret, ensure_ascii=True, sort_keys=True) + '\n')

		count += 1
		if count == int(options.max_count):
			break


if __name__ == '__main__':
	cProfile.run('main()', 'timeit')
	p = pstats.Stats('timeit')
	p.sort_stats('time').print_stats(8)
