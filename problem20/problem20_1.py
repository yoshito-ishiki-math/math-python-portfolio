"""n × (n - 1) × ... × 3 × 2 × 1 を n! と表す.

例えば, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800 となる.
この数の各桁の合計は 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27 である.

では, 100! の各位の数字の和を求めよ.

注: Problem 16 も各位の数字の和に関する問題です。解いていない方は解いてみてください。"""


import math
import numpy as np
#import matplotlib.pyplot as plt



#print(len(str(math.factorial(100))))
yo_str=str(math.factorial(100))
yo_list=[int(yo_str[i]) for i in range(158)]

desired_sum=sum(yo_list)

print(desired_sum)
