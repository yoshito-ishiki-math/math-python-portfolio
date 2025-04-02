"""次の式は, 1 + 22 + 33 + ... + 1010 = 10405071317 である.

では, 11 + 22 + 33 + ... + 10001000 の最後の10桁を求めよ."""

desired_sum=0
for z in range(1, 1000):
    desired_sum+=pow(z, z, 10**10)

print(desired_sum%10**10)