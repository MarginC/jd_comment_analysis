#!/usr/bin/python
# -*- coding:UTF-8 -*-

import codecs
import json
import time
import threading
import sys
from optparse import OptionParser

from comment import comment


def init_parser():
	parser = OptionParser()
	parser.add_option('-i', '--input', action='store', dest='input',
		help='set the input filename', metavar='FILE')
	parser.add_option('-o', '--output', action='store', dest='output',
		help='set the output filename', metavar='FILE')
	parser.add_option('-c', '--count', action='store', dest='max_count',
		default=sys.maxsize, help='set the max count to process')
	parser.add_option('-t', '--thread', action='store', dest='thread',
		default=10, help='set the thread count')
	parser.add_option('-l', '--log', action='store', dest='logfile',
		help='set the log file')
	return parser.parse_args()


if __name__ == '__main__':
	(options, args) = init_parser()
	match_count = 0
	count = 0
	start_time = time.process_time()
	input = codecs.open(options.input, 'r', encoding='utf-8', errors='strict')
	output = codecs.open(options.output, 'w', encoding='utf-8')
	log = codecs.open(options.logfile, 'w', encoding='utf-8')
	output.write((','.join(comment.OUT_HEADERS) + '\n'))
	for line in input.readlines():
		try:
			_json = json.loads(line)
			if len(_json['content']) < 10:
				continue
			c = comment.Comment(_json)
			_match_count = c.match(_json['content'], comment.matchRegex)
		except:
			log.write(line)
			continue

		if _match_count:
			output.write(str(c) + '\n')
		match_count += _match_count
		count += 1
		if count == int(options.max_count):
			break
	print('process {0} count comments, match {1} rules. process {2}s'.format(count, match_count, time.process_time()))
