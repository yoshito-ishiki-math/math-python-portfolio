"""10以下の素数の和は 2 + 3 + 5 + 7 = 17 である.

200万以下の全ての素数の和を求めよ."""

#200万 2000000

#problem10_1では isprimeを使って処理に時間が掛かっちゃったけど，篩法を使ってみよう．

#Nが与えられた時にNまでのリストで，素数についてはa[p]=Trueとなるもの作れば良い．

#print([True]*3)

#えらとてネスの篩法
def Era_frui(N):
    yo_list=[True]*(N+1)
    #0と1は最初から飛ばす
    yo_list[0], yo_list[1]=False, False
    #ここから篩にかける
    for z in range(N+1):
        if yo_list[z]==False:
            continue
        q=z+z
        while q<=N:
            yo_list[q]=False
            q+=z
    return yo_list

input_num=2000000
desired_sum=0

isprime_E=Era_frui(input_num)

for z in range(input_num):
    if isprime_E[z]:
        desired_sum+=z

print(desired_sum)

#正解した！