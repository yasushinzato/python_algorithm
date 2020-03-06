# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:42:40 2020

西暦を和暦に変換する
@author: 81909
"""
def japanease_ad(year):
    if year < 1868:
        ''
    elif year < 1912:
        return '明治' + str(year - 1867) + '年'
    elif year < 1926:
        return '大正' + str(year - 1911) + '年'
    elif year < 1989:
        return '昭和' + str(year - 1925) + '年'
    elif year < 2019:
        return '平成' + str(year - 1988) + '年'
    else:
        return '令和' + str(year - 2018) + '年'
for i in range(1868, 2020):
    print(japanease_ad(i))
