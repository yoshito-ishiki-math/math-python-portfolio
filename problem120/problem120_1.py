"""(a-1)n+(a+1)n を a2 で割った余りを r と定義する.

例えば, a=7, n=3 の時, r=42 である: 63+83=728≡ 42 mod 49. n が変われば r も変わるが, 
a=7 の時 r の最大値 rmax は 42 であることがわかる.

3 ≤ a ≤ 1000 において, Σ rmax を求めよ."""

def rmax(a : int):
    desired_r=2
    for n in range(1, 2*a, 2):
        tmp_r=(2 * a * n) % (a**2)
        desired_r=max(desired_r, tmp_r)
    return desired_r


def rmax_2(a):
    return a*(a - (2- a%2))



desired_sum=sum([rmax(z) for z in range(3, 1001)])

desired_sum_2=sum([a*(a - (2- a%2)) for a in range(3, 1001)])


print(desired_sum)
print(desired_sum_2)



#print(rmax(5))=10
#print(rmax_2(5))=20


#なんか違うっぽいわかんない．
#なんか問題と想定解が間違っている気がする．4n+1型の整数を考慮していない想定解になっている．
#想定解が正しい．3*a/2までの範囲で探索すればrmaxとrmax_2は等しくなる．
