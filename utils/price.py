#!/usr/bin/python
# -*- coding:UTF-8 -*-

import codecs
import json
import os


PRICE_FILE = 'jd_price_list.json'


def load_price(filename):
	prices = {}
	directory = os.path.split(os.path.realpath(__file__))[0]
	filename = '{0}/{1}'.format(directory, filename)
	with codecs.open(filename) as f:
		for line in f.readlines():
			try:
				_json = json.loads(line)
			except Exception as e:
				print(line)
				raise e
			prices[_json['referenceId']] = _json['price']
	return prices


def get_price(id, prices):
	if id in prices:
		return prices[id]
	elif str(id) in prices:
		return prices[str(id)]
	raise IndexError


if __name__ == '__main__':
	prices = load_price('jd_price_list.json')
	print(json.dumps(prices, indent=2))
	print(get_price(2156601, prices))
