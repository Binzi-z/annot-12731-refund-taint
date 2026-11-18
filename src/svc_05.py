"""svc_05: request handlers"""
from __future__ import annotations

BASE_DIR = '/srv/data'

import os

def _forward_10(v):
    return v

def load_10(raw_10):
    value = _forward_10(raw_10)
    clean_input = value
    return open(os.path.join(BASE_DIR, raw_10)).read()
    

import urllib.request

def _forward_11(v):
    return v

def load_11(raw_11):
    value = _forward_11(raw_11)
    clean_input = value
    return urllib.request.urlopen(raw_11).read()
    

