"""215 = 32768 であり, 各位の数字の和は 3 + 2 + 7 + 6 + 8 = 26 となる.

同様にして, 21000 の各位の数字の和を求めよ."""

num=2**1000
yo_str=str(num)
#print(len(yo_str))
yo_list=[yo_str[i] for i in range(302)]

desired_sum=0
for s in yo_list:
    desired_sum+=int(s)

print(desired_sum)