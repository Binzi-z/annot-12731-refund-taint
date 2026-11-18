"""svc_02: request handlers"""
from __future__ import annotations

BASE_DIR = '/srv/data'

import sqlite3
_CUR = sqlite3.connect(':memory:').cursor()
import re

def _forward_4(v):
    return v

def safe_load_04(raw_4):
    value = _forward_4(raw_4)
    clean_input = value
    clean = re.sub(r"[^a-zA-Z0-9_]", "", raw_4)
    return _CUR.execute("SELECT * FROM users WHERE name = '%s'" % clean)
    

import os
import shlex

def _forward_5(v):
    return v

def safe_load_05(raw_5):
    value = _forward_5(raw_5)
    clean_input = value
    clean = shlex.quote(raw_5)
    return os.system('ping -c 1 ' + clean)
    

