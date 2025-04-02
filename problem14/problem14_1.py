"""正の整数に以下の式で繰り返し生成する数列を定義する.

n → n/2 (n が偶数)

n → 3n + 1 (n が奇数)

13からはじめるとこの数列は以下のようになる.

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
13から1まで10個の項になる. この数列はどのような数字からはじめても最終的には 1 になると考えられているが, まだそのことは証明されていない(コラッツ問題)

さて, 100万未満の数字の中でどの数字からはじめれば最長の数列を生成するか.

注意: 数列の途中で100万以上になってもよい
"""

"""100まん  1000000"""

import functools

@functools.cache

def count_c(n):
    num=n
    count=1
    if num==1:
            return count
    else:
        while num>1:
            if num%2==0:
                count+=1
                num//=2
                continue
            else:
                count+=1
                num=3*num+1
                continue
    return count

desired_num=0
hikaku_num=0
for z in range(1000001):
    if hikaku_num<count_c(z):
        desired_num=z
        hikaku_num=count_c(z)
    else:
        pass

print(desired_num)