# -*- coding: utf-8 -*-
"""
Created on Thu Mar  5 13:29:48 2020

力任せ法

検索文字とパターン文字を1文字ずつ一致するか調べながら繰り返す。
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
  │S│　　一致しない場合は、1文字ずつずらして改めて比較
  └─┘

前から順に力任せで繰り返すので、「力任せ法」といわれる。

@author: 81909
"""
text = list('SHOEISHA SESHOP') # 1文字ずつのリストに変換
pattern = list('SHA')

for i in range(len(text)):
    match = True
    for j in range(len(pattern)):
        if text[i + j] != pattern[j]:
            match = False
            break
        
    if match:
        # すべての文字patternが一致していれば出力
        print(i)
        break
