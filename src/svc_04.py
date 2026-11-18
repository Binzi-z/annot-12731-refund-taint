"""svc_04: request handlers"""
from __future__ import annotations

BASE_DIR = '/srv/data'

import sqlite3
_CUR = sqlite3.connect(':memory:').cursor()
import re

def _forward_8(v):
    return v

def safe_load_08(raw_8):
    value = _forward_8(raw_8)
    clean_input = value
    clean = re.sub(r"[^a-zA-Z0-9_]", "", raw_8)
    return _CUR.execute("SELECT * FROM users WHERE name = '%s'" % clean)
    

import os
import shlex

def _forward_9(v):
    return v

def safe_load_09(raw_9):
    value = _forward_9(raw_9)
    clean_input = value
    clean = shlex.quote(raw_9)
    return os.system('ping -c 1 ' + clean)
    

