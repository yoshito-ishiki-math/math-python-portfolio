"""フィボナッチ数列の項は前の2つの項の和である. 最初の2項を 1, 2 とすれば, 最初の10項は以下の通りである.

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
数列の項の値が400万以下のとき, 値が偶数の項の総和を求めよ."""
"""400万: 4000000"""


import functools



# デコレータfunctools.cacheを使用
@functools.cache
#再帰によってフィボナッチ数列を定義する．
def fib(n):
    if n<2:
        return n+1
    result=fib(n-1)+fib(n-2)
    return result

count=0
while fib(count)<=4000000:
    count+=1

total=0
for i in range(count):
    if fib(i)%2==0:
        total+=fib(i)
    else:
        pass

print(total)