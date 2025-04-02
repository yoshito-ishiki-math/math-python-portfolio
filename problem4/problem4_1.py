"""左右どちらから読んでも同じ値になる数を回文数という. 2桁の数の積で表される回文数のうち, 最大のものは 9009 = 91 × 99 である.

では, 3桁の数の積で表される回文数の最大値を求めよ."""

est_below=100*100
est_above=999*999

#print(est_below)=10000
#print(est_above)=998001

#素朴にest_belowとest_aboveの間の数でやろうとすると間違える．２つの３桁の数の席でかけるとは限らないからだ．

#というわけで二つの積でかける数を探索する
desired_num=0
for fac_a in range(100, 1000):
    for fac_b in range(100, 1000):
        z=fac_a * fac_b
        yo_list=[str(z)[i] for i in range(len(str(z)))]
        if yo_list==list(reversed(yo_list)) and desired_num<z: #このfor文で最大のものが得られるかわからなかったので，大きかったら更新するようにした．
            desired_num=z

print(desired_num)