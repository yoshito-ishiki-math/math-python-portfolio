"""By listing the first six prime numbers: , and , we can see that the th prime is .

What is the st prime number?"""

"""素数を小さい方から6つ並べると 2, 3, 5, 7, 11, 13 であり, 6番目の素数は 13 である.

10 001 番目の素数を求めよ."""

def isprime(n):
    result=True
    for k in range(2, n):
        if n%k==0:
            result=False
            break
        else:
            result=True
    return result


count=1
num=2
desired_prime=2
while count<=10001:
    if isprime(num)==True:
        desired_prime=num
        num+=1
        count+=1
    else:
        num+=1

print(desired_prime)

#ちょっと遅い． 改良の余地あり．
