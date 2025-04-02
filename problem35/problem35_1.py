"""197は巡回素数と呼ばれる. 桁を回転させたときに得られる数 197, 971, 719 が全て素数だからである.

100未満には巡回素数が13個ある: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, および97である.

100万未満の巡回素数はいくつあるか?"""

#100万 1000000

#これ無理
#篩法
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

def iscycprime(yo_list : list):
    result=[False]*(len(yo_list))
    for z in range(len(yo_list)):
        if not yo_list[z]:
            continue
        
        s = str(z)
        connect_num=s+s
        
        all_primes=True
        for k in range(len(s)):
            rot_num= int(connect_num[k:k+len(str(z))])
            #rotが素数かどうか判定
            if not yo_list[int(connect_num[k:k+len(str(z))])]:
                all_primes=False
        
        if all_primes:
            result[z]=True
    return result

a=10**6

yoyo_list=Era_frui(a)
desired_list=iscycprime(yoyo_list)

desired_count=desired_list.count(True)

print(desired_count)

#答え55．多分巡回した時に0が先頭にならないみたいな条件を厳密には追加するべきだが，答えがもとまってしまった．



