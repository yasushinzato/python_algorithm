# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 10:18:00 2020

1950年から2050年までの「うるう年」を出力する

- 4で割り切れる年はうるう年
- ただし、100で割り切れて400で割り切れない年はうるう年ではない
@author: 81909
"""

def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        else:
            return True
    else:
        return False
    
for i in range(1950, 2051):
    if is_leap_year(i) == True:
        print(str(i) + ' はうるう年です')
#    print(str(i) + ' ' + str(is_leap_year(i)))

    