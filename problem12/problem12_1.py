"""三角数の数列は自然数の和で表わされ, 7番目の三角数は 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28 である. 三角数の最初の10項は:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
となる.

最初の7項について, その約数を列挙すると, 以下のとおり.

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

これから, 7番目の三角数である28は, 5個より多く約数をもつ最初の三角数であることが分かる.

では, 500個より多く約数をもつ最初の三角数はいくつか."""



#nの約数の個数を(a+1)(b+1)....とし，aは2の冪とする
#三角数のn(n+1)/2を考えると，nとn+1は互いに素なのでn+1にはnにはない素因数が含まれる．
#よってn(n+1)/2の約数の下限は2a(b+1)(c+1)...となりこれが500をこえるものが
#nのupper boundとして使える．つまりa(b+1)(c+1)...が250を超えるnである．



#est_upper=2**6 * 3**6 *5*6

#print(est_upper)=1399680
#print(6*7**2)=294


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




#素因数分解をするアルゴリズムをかく
def pfactor(n, m, yoyo_list):
    #yo_listには素数判定のやつを入れる．
    result=[]
    num=n
    for z in range(2, m):
        if yoyo_list[z]==False:
            continue
        elif yoyo_list[z]==True and num%z==0:
            count=0
            while num%z==0:
                num//=z
                count+=1
            result.append([z, count])
            if num==1:
                break
    return result



#上記リストから(a+1)(b+1)．．．を返す関数を作る．
def sigma(yo_list):
    result=1
    num=len(yo_list)
    for z in range(num):
        result*=yo_list[z][1]+1
    return result



def de_func(n, m, l):
    num=(n*(n+1))//2
    return sigma(pfactor(num, m, l))


def find_first(m, l, bound):
    n=1
    #de_funcがboundを超えるまで繰り返す
    while de_func(n, m, l)<bound:
        n+=1
    return n




est_upper=2**6 * 3**6 *5*6

yoyo=Era_frui(est_upper)

bound=500

answer=find_first(est_upper, yoyo, bound)

print(answer)
print((answer*(answer+1)//2))
"""
a=12375
s=pfactor((a*(a+1))//2, est_upper, yoyo)
print(s)
print(sigma(s))
"""

"""
s=pfactor(24, est_upper, yoyo)
print(s)
print(sigma(s))
"""

"""
for z in range(est_upper):
    num=(z*(z+1))//2
    factor=pfactor(num, eses, yoyo)
    s=sigma(factor)
    if s>=500:
        break

print(num)
"""


"""
desired_num=0
for z in range(est_upper):
    kosu=0
    num_left=z
    num_right=z+1
    pfactor_right=pfactor(num_left, est_upper, yoyo)
    kosu_tri=sigma(pfactor_right)
    if kosu<kosu_tri:
        desired_num=z

print(desired_num)


"""
