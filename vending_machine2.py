# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 14:12:37 2020

@author: 81909
"""

input_price = input('insert: ')
product_price = input('product: ')
change = int(input_price) - int(product_price)
print(change)

coin = [5000, 1000, 500, 100, 50, 10, 5, 1]  # 紙幣・硬貨のリスト

for i in coin:
    r = change // i
    change %= i
    print(str(i) + ': ' + str(r))
