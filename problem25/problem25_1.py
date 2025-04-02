"""フィボナッチ数列は以下の漸化式で定義される:

　　Fn = Fn-1 + Fn-2 , ただし F1 = 1, F2 = 1.

最初の12項は以下である.

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
12番目の項, F12 が3桁になる最初の項である.

1000桁になる最初の項の番号を答えよ."""



import functools
import math


# デコレータfunctools.cacheを使用
@functools.cache
#再帰によってフィボナッチ数列を定義する．
def fib(n):
    result=0
    if n<=2:
        return 1
    else:
        result=fib(n-1)+fib(n-2)
    return result

#print(math.log10(fib(100)))

count=1
while math.log10(fib(count))<999:
    count+=1

print(count)
