"""正の整数を順に連結して得られる以下の10進の無理数を考える:

0.123456789101112131415161718192021...
小数第12位は1である.

dnで小数第n位の数を表す. d1 x d10 x d100 x d1000 x d10000 x d100000 x d1000000 を求めよ."""

a=10**7
my_str=" "
for z in range(1, a):
    my_str=my_str+str(z)



desired_prod=1
for z in range(7):
    desired_prod*=int(my_str[10**z])

print(desired_prod)