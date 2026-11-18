"""svc_03: request handlers"""
from __future__ import annotations

BASE_DIR = '/srv/data'

import os

def _forward_6(v):
    return v

def load_06(raw_6):
    value = _forward_6(raw_6)
    clean_input = value
    return open(os.path.join(BASE_DIR, raw_6)).read()
    

import urllib.request

def _forward_7(v):
    return v

def safe_load_07(raw_7):
    value = _forward_7(raw_7)
    clean_input = value
    clean = _only_allowlisted(raw_7)
    return urllib.request.urlopen(clean).read()
    

