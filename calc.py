# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 08:42:08 2020

逆ポーランド記法
逆ポーランド記法は「1 + 2」を「1 2 +」のように書く。日本語での「1と2を足す」の表現と似ている。
ポーランド記法は「+ 1 2」と書く。
数であればスタックに積み、演算子であればスタックから値を取り出して計算し、またスタックに積むという操作を繰り返す。
@author: 81909
"""
def calc(expression):
    stack = []
    for i in expression.split(' '):
        # 現在のスタックの内容を表示
        print(stack)
        if i == '+':
            # + のときはスタックから2つ取り出して加算し、再度格納する
            b, a = stack.pop(), stack.pop()
            stack.append(a + b)
        elif i == '-':
            # - のときはスタックから2つ取り出して減算し、再度格納する
            b, a = stack.pop(), stack.pop()
            stack.append(a - b)
        elif i == '*':
            # * のときはスタックから2つ取り出して乗算し、再度格納する
            b, a = stack.pop(), stack.pop()
            stack.append(a * b)
        elif i == '/':
            # / のときはスタックから2つ取り出して除算し、再度格納する
            b, a = stack.pop(), stack.pop()
            stack.append(a // b)
        else:
            # 演算子以外（数字）のときはその値を格納する
            stack.append(int(i))
    return stack[0]

print(calc('4 6 2 + * 3 1 - 5 * -'))
