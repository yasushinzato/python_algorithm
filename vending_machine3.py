# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:19:27 2020

@author: 81909
"""

import sys # エラー時に強制終了するためのモジュールを読み込む

input_price = input('insert: ')
if not input_price.isdecimal():
    print('整数を入力してください')
    sys.exit() # エラーなので、強制終了

product_price = input('product: ')
if not product_price.isdecimal():
    print('整数を入力してください')
    sys.exit()

change = int(input_price) - int(product_price)

if change < 0:
    print('金額が不足しています')
    sys.exit()

print(change)

coin = [5000, 1000, 500, 100, 50, 10, 5, 1] # 紙幣・硬貨のリスト

for i in coin:
#    r = change // i
#    change %= i
    # pythonではdivmod関数という商と余りを同時に求める関数がある。その関数で以下のように書ける
    r, change = divmod(change, i)
    print(str(i) + ': ' + str(r) )