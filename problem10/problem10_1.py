"""10以下の素数の和は 2 + 3 + 5 + 7 = 17 である.

200万以下の全ての素数の和を求めよ."""

#200万 2000000

#素数判定関数

def isprime(n):
    result=True
    for k in range(2, n):
        if n%k==0:
            result=False
            break
        else:
            result=True
    return result

desired_num=0

"""
for z in range(2000000):
    if isprime(z)==True:
        desired_num+=z
    else:
        pass

print(desired_num)
#処理に時間がかかりすぎる．無理．
"""

for z in range(2000000):
    desired_num+=z

print(desired_num)
print(isprime(31))