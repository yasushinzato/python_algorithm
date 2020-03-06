# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 13:58:39 2020

ファイル検索
深さ優先検索
@author: 81909
"""
import os

def search(dir, name):
    for i in os.listdir(dir):
        if i == name:
            print(dir + i)
        if os.path.isdir(dir + i):
            if os.access(dir + i, os.R_OK):  # 読み込み可能だったら、フォルダの中を更に調べる
                search(dir + i + '/', name)
search('d:/pg/', 'book')
