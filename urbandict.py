#!/bin/python3
import json
import urllib.parse, urllib.request

_URBANDICT_URL = "http://api.urbandictionary.com/v0/define?term="

def _run_urbandict(search):
    safe_search = ""
    words = ' '.join(search.split()).split(' ')
    for idx, word in enumerate(words):
        if len(words) == idx+1:
            safe_search += "%s" % urllib.parse.quote_plus(word)
        else:
            safe_search += "%s+" % urllib.parse.quote_plus(word)
    response = urllib.request.urlopen(_URBANDICT_URL + safe_search)
    return json.loads(response.read())

def urbandict(word):
    return _run_urbandict(word)