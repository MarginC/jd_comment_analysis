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

from comment import comment


def init_parser():
	parser = OptionParser()
	parser.add_option('-i', '--result', action='store', dest='result',
		default='./output/result.csv', help='set the result filename', metavar='FILE')
	parser.add_option('--emotion', action='store', dest='emotion',
		default='./output/emotion/emotion.txt', help='set the emotion filename', metavar='FILE')
	parser.add_option('--output', action='store', dest='output',
		default='./output/combine_result.csv', help='set the combine result filename', metavar='FILE')
	parser.add_option('--count', action='store', dest='max_count',
		default=sys.maxsize, help='set the max count to process')
	parser.add_option('--threshold', action='store', dest='match_threshold',
		default=8, help='set the match threshold')
	return parser.parse_args()


def main():
	(options, args) = init_parser()
	statistic = {}
	count = 0

	emotions = emotion.emotionLoad(options.emotion)
	print('emotion process time {0}'.format(time.process_time()))

	result_file = codecs.open(options.result, 'r', encoding='utf-8', errors='strict')
	output_file = codecs.open(options.output, 'w', encoding='utf-8')

	output_file.write((','.join(comment.OUT_HEADERS) + '\n'))

	c = comment.Comment()
	for line in result_file.readlines():
		_json = json.loads(line)
		match = _json['match']
		if match > options.match_threshold:
			for k in _json:
				if k != 'match':
					id = k
					c.load(_json[id])
					if c.data['compilation'] == '':
						try:
							c.data['compilation'] = emotions[id]
						except:
							break
					output_file.write(str(c) + '\n')
					try:
						statistic[c.data['score']] += 1
					except:
						statistic[c.data['score']] = 1
					count += 1
					if count == int(options.max_count):
						break

		# log
		if divmod(count, 1000)[1] == 0:
			print('process {0} comments, {1}'.format(count, time.process_time()))
	strs = 'statistic {0}, \ncount {1}, process {2}s'.format(
		json.dumps(statistic, sort_keys=True), count, time.process_time())
	print(strs)


if __name__ == '__main__':
	cProfile.run('main()', 'timeit')
	p = pstats.Stats('timeit')
	p.sort_stats('time').print_stats(8)
