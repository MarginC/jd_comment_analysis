# -*- coding:utf8 -*-
import urllib
import json

def ltp(text):
    url_get_base = "http://api.ltp-cloud.com/analysis/"
    args = {
        'api_key' : 'I1o081O3m0aX7ixaqVAD7tRZ6JEQiI6jHliJUJcK',
        'text' : text,
        'pattern' : 'ws',
        'format' : 'json'
    }
    result = urllib.urlopen(url_get_base, urllib.urlencode(args)) # POST method
    content = result.read().strip()
    return json.loads(content)
