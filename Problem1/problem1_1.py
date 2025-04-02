"""10未満の自然数のうち, 3 もしくは 5 の倍数になっているものは 3, 5, 6, 9 の4つがあり, これらの合計は 23 になる.

同じようにして, 1000 未満の 3 か 5 の倍数になっている数字の合計を求めよ."""

#与えられた数ceiling未満のmの倍数になっている数の総和を出す関数
def yo_souwa(ceiling, m):
    total=0
    for z in range(ceiling):
        if z%m==0:
            total+=z
    return total

#この関数を使って包徐原理で答えを出す．
print(yo_souwa(1000, 3)+yo_souwa(1000, 5)-yo_souwa(1000, 15))