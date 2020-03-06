# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 13:46:04 2020

Boyer-Moore法

力任せ法は1文字ずつずらしていたので、末尾から比較して一気にずらす。
検索対象文字列’SHOEISHA SESHOP’
一致する文字パターン’SHA’

┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐┌─┐
│S││H││O││E││I││S││H││A││ ││S││E││S││H││O││P│
└─┘└─┘└─┘└─┘└─┘└─┘└─┘└─┘└─┘└─┘└─┘└─┘└─┘└─┘└─┘
 ↓  ｜ ｜
┌─┐　｜　｜
│S│　｜　｜
└─┘　↓　 ｜
┌─┐┌─┐　｜　　　一致している場合は1文字ずつ伸ばしながら比較する
│S││H│　｜
└─┘└─┘　↓
┌─┐┌─┐┌─┐
│S││H││A│
└─┘└─┘└─┘
         ┌─┐
         │S│　　一致しない場合は、その部分を一気にずらして高速化する
         └─┘

@author: 81909
"""

text = list('SHOEISHA SESHOP') # 1文字ずつのリストに変換
pattern = list('SHA')

skip = {}
for i in range(len(pattern) - 1):
    skip[pattern[i]] = len(pattern) - i - 1 # ずらす数をカウント
    
i = len(pattern) - 1
while i < len(text):
    match = True
    for j in range(len(pattern)):
        if text[i - j] != pattern[len(pattern) - 1 - j]:
            match = False
            break
        
    if match:
        print(i - len(pattern) + 1)
        break
    if text[i] in skip:
        i += skip[text[i]]  # 用意した数だけ位置をずらす
    else:
        i += len(pattern)  # パターンの文字数だけ位置をずらす