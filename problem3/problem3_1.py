"""13195 の素因数は 5, 7, 13, 29 である.

600851475143 の素因数のうち最大のものを求めよ."""

#ものすごく素朴に素数判定をする．
def isprime(n):
    for k in range(2, n):
        if n%k==0:
            result=False
            break
        else:
            result=True
    return result


given_value=600851475143
est_above=int(given_value**(0.5))+1
desired_prime=1
#desired_primeを更新して最大の素因数を見つける．試し割り法
for z in range(3, est_above):
    if given_value%z==0 and isprime(z)==True:
        desired_prime=z
    else:
        pass


print(desired_prime)