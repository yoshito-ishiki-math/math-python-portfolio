"""ピタゴラス数(ピタゴラスの定理を満たす自然数)とは a < b < c で以下の式を満たす数の組である.

a2 + b2 = c2
例えば, 32 + 42 = 9 + 16 = 25 = 52 である.

a + b + c = 1000 となるピタゴラスの三つ組が一つだけ存在する.
これらの積 abc を計算しなさい."""

#c=1000-a-bでa<bなので，bを動かして探索する

desired_num_a=1
desired_num_b=1
for b in range(1, 1000):
    for a in range(1, b):
        if (a**2) + (b**2) ==(1000-a-b)**2 and a+b<1000:
            desired_num_a=a
            desired_num_b=b
        else:
            pass

desired_num_c=1000-desired_num_a-desired_num_b
print(desired_num_a * desired_num_b * desired_num_c)
