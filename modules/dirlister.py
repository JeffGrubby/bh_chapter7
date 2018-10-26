#!/usr/bin/python3
#-*- coding:utf8 -*-
# Power by Leaf 2018-10-26 02:34:26

import os

def run(**args):
    print('[*] In dirlister module.')
    files = os.listdir('.')
    return str(files)
