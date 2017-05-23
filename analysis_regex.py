#!/usr/bin/python
# -*- coding:UTF-8 -*-

import codecs
import json
import time
import threading
import queue
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


class Worker(threading.Thread):
	def __init__(self):
		super(Worker, self).__init__()
		self.stop = False
		self.in_queue = queue.Queue(1000)
		self.out_queue = queue.Queue(2000)
		self.log_queue = queue.Queue(2000)
		self.statistics = {}
		pass

	def stop_work(self):
		self.stop = True

	def get_statistics(self):
		return self.statistics

	def is_full(self):
		return self.in_queue.full()

	def enqueue_task(self, line):
		self.in_queue.put(line)

	def file_output(self, file):
		while not self.out_queue.empty():
			out_line = self.out_queue.get()
			file.write(out_line + '\n')
		pass

	def file_log(self, file):
		while not self.log_queue.empty():
			out_line = self.log_queue.get()
			file.write(out_line + '\n')

	def run(self):
		while True:
			try:
				line = self.in_queue.get(True, 1)
				line = self.in_queue.get(True, 1)
			except:
				if self.stop:
					return
				else:
					continue
			try:
				_json = json.loads(line)
				c = comment.Comment(_json)
				match_count = c.match(_json['content'], comment.matchRegex)
			except:
				self.log_queue.put(line, True)
				continue

			try:
				self.statistics[match_count] += match_count
			except:
				self.statistics[match_count] = match_count
			self.out_queue.put(str(c), True)
			try:
				self.statistics['count'] += 1
			except:
				self.statistics['count'] = 1
		pass


if __name__ == '__main__':
	(options, args) = init_parser()
	input = codecs.open(options.input, 'r', encoding='utf-8', errors='strict')
	output = codecs.open(options.output, 'w', encoding='utf-8')
	log = codecs.open(options.logfile, 'w', encoding='utf-8')
	output.write((','.join(comment.OUT_HEADERS) + '\n'))

	workers = []
	for i in range(int(options.thread)):
		workers.append(Worker())

	for worker in workers:
		worker.start()

	while True:
		count = 0
		for worker in workers:
			# 先将工作队列填满
			while not worker.is_full():
				line = input.readline()
				if line:
					worker.enqueue_task(line)
					count += 1
				else:
					break
			# 输出结果
			worker.file_output(output)
			# 输出错误日志
			worker.file_output(log)
		if count == 0:
			break

	for worker in workers:
		worker.stop_work()
		# 输出结果
		worker.file_output(output)
		# 输出错误日志
		worker.file_output(log)

	for worker in workers:
		worker.join()
		print(worker.get_statistics())

	print('process time {0}'.format(time.process_time()))