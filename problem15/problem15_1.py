"""2×2 のマス目の左上からスタートした場合, 引き返しなしで右下にいくルートは 6 つある.


では, 20×20 のマス目ではいくつのルートがあるか."""

import math
a=math.factorial(40)
b=math.factorial(20)
print(a//(b*b))