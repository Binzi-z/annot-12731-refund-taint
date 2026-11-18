"""svc_00: request handlers"""
from __future__ import annotations

BASE_DIR = '/srv/data'

import sqlite3
_CUR = sqlite3.connect(':memory:').cursor()

def _forward_0(v):
    return v

def load_00(raw_0):
    value = _forward_0(raw_0)
    clean_input = value
    return _CUR.execute("SELECT * FROM users WHERE name = '%s'" % raw_0)
    

import os

def _forward_1(v):
    return v

def load_01(raw_1):
    value = _forward_1(raw_1)
    clean_input = value
    return os.system('ping -c 1 ' + raw_1)
    

