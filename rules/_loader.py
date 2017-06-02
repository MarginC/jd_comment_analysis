#!/usr/bin/python
# coding=utf-8

import os
import json
import codecs
import re
import sys


def __get_field_name(filename):
	idx = filename.find('.')
	if idx >= 0:
		name = filename[idx + 1:]
		idx = name.find('.')
		if idx >= 0:
			name = name[0:idx]
			return True, name
	return False, ''


def __load_rules(filename):
	_rules = []
	with codecs.open(filename, encoding='utf-8', errors='ignore') as f:
		for line in f.readlines():
			strs = line.split(' ')
			if len(strs) > 1:
				_rules.append(strs)
	return _rules


def __load_regexes(filename):
	regexes = []
	with codecs.open(filename, encoding='utf-8', errors='strict') as f:
		line_number = 0
		for line in f.readlines():
			line_number += 1
			strs = line.split(' ')
			if len(strs) > 1:
				rule = dict()
				rule['score'] = strs[0]
				rule['patterns'] = []
				for str in strs[1:]:
					try:
						p = re.compile(str.rstrip())
						rule['patterns'].append(p)
					except Exception as e:
						print('Exception: {0}, Filename: {1}, Line: {2}'.format(e, filename, line_number))
						exit()
				regexes.append(rule)
	return regexes


def load_rules():
	rules = {}
	directory = os.path.split(os.path.realpath(__file__))[0]
	for filename in os.listdir(directory):
		# need skip '.svn'
		if filename.startswith('.') or filename.startswith('_') or filename.endswith('.pyc'):
			continue
		# 1.field.rules
		ret, name = __get_field_name(filename)
		if ret:
			rules[name] = __load_rules(directory + '\\' + filename)
	return rules


def load_regexes():
	regexes = {}
	directory = os.path.split(os.path.realpath(__file__))[0]
	for filename in os.listdir(directory):
		# need skip '.svn'
		if filename.startswith('.') or filename.startswith('_') or filename.endswith('.pyc'):
			continue
		# 1.field.rules
		ret, name = __get_field_name(filename)
		if ret:
			regexes[name] = __load_regexes(directory + '\\' + filename)
	return regexes


if __name__ == '__main__':
	rules = load_rules()
	json.dumps(rules, indent=2, ensure_ascii=False)
	if len(sys.argv) <= 1:
		comment = u'发货神速，送货速度快，并且马上安装，已使用几次，感觉还不错，给满分。客服服务态度尤其好。'
	else:
		comment = sys.argv[1]
	fields = load_regexes()
	for field in fields:
		regexes = fields[field]
		for regex in regexes:
			patterns = regex['patterns']
			unmatched = False
			for pattern in patterns:
				if not re.search(pattern, comment):
					unmatched = True
					break
			if not unmatched:
				print('{0}: {1} {2}'.format(field, regex['score'], patterns))
