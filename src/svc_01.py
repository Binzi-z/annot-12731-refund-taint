"""svc_01: request handlers"""
from __future__ import annotations

BASE_DIR = '/srv/data'

import os

def _forward_2(v):
    return v

def load_02(raw_2):
    value = _forward_2(raw_2)
    clean_input = value
    return open(os.path.join(BASE_DIR, raw_2)).read()
    

import urllib.request

def _forward_3(v):
    return v

def load_03(raw_3):
    value = _forward_3(raw_3)
    clean_input = value
    return urllib.request.urlopen(raw_3).read()
    

