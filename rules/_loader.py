#coding=utf-8

import os
import json
import codecs
import re
from pprint import pprint

def __getFieldName(filename):
	idx = filename.find('.')
	if idx >= 0:
		name = filename[idx + 1 : ]
		idx = name.find('.')
		if idx >= 0:
			name = name[0 : idx]
			return True, name
	return False, ''

def __loadRules(filename):
	rules = []
	with codecs.open(filename, encoding='utf-8', errors='ignore') as f:
		for line in f.readlines():
			strs = line.split(' ')
			if len(strs) > 1:
				rules.append(strs)
	return rules

def __loadRegexes(filename):
	rules = []
	with codecs.open(filename, encoding='utf-8', errors='ignore') as f:
		for line in f.readlines():
			strs = line.split(' ')
			if len(strs) > 1:
				rule = dict()
				rule['score'] = strs[0]
				rule['patterns'] = []
				for str in strs[1:]:
					p = re.compile(str.rstrip(), re.IGNORECASE)
					rule['patterns'].append(p)
				rules.append(rule)
	return rules

def load_rules():
	rules = {}
	dir = os.path.split(os.path.realpath(__file__))[0]
	for filename in os.listdir(dir):
		#need skip '.svn'
		if filename.startswith('.') or filename.startswith('_') or filename.endswith('.pyc'):
			continue
		#1.field.rules
		ret, name = __getFieldName(filename)
		if ret:
			rules[name] = __loadRules(dir + '\\' + filename)
	return rules

def load_regexes():
	rules = {}
	dir = os.path.split(os.path.realpath(__file__))[0]
	for filename in os.listdir(dir):
		#need skip '.svn'
		if filename.startswith('.') or filename.startswith('_') or filename.endswith('.pyc'):
			continue
		#1.field.rules
		ret, name = __getFieldName(filename)
		if ret:
			rules[name] = __loadRegexes(dir + '\\' + filename)
	return rules

if __name__ == '__main__':
	print(json.dumps(load_rules(), indent=2, ensure_ascii=False))
	regexes = load_regexes()
	pprint(regexes)
