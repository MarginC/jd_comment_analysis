#coding=utf-8

import os

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
	with open(filename) as f:
		for line in f.readlines():
			strs = line.split(' ')
			if len(strs) > 1:
				rules.append(strs)
	return rules

def load():
	fieldList = {}
	for filename in os.listdir(os.path.abspath('.')):
		#need skip '.svn'
		if filename.startswith('.') or filename.startswith('_') or filename.endswith('.pyc'):
			continue
		#1.field.rules
		ret, name = __getFieldName(filename)
		if ret:
			fieldList[name] = __loadRules(filename)
	return fieldList

if __name__ == '__main__':
	print(load())
