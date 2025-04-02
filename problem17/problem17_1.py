"""1 から 5 までの数字を英単語で書けば one, two, three, four, five であり, 全部で 3 + 3 + 5 + 4 + 4 = 19 の文字が使われている.

では 1 から 1000 (one thousand) までの数字をすべて英単語で書けば, 全部で何文字になるか.

注: 空白文字やハイフンを数えないこと. 例えば, 342 (three hundred and forty-two) は 23 文字, 115 (one hundred and fifteen) は20文字と数える. なお, "and" を使用するのは英国の慣習."""

def mojisu_1keta(n :int):
    result=0
    if len(str(n))==1:
        if n==1:
            #one
            result=3
        elif n==0:
            #zero
            result=0
        elif n==2:
            #two
            result=3
        elif n==3:
            #three
            result=5
        elif n==4:
            #four
            result=4
        elif n==5:
            #five
            result=4
        elif n==6:
            #six
            result=3
        elif n==7:
            #seven
            result=5
        elif n==8:
            #eight
            result=5
        elif n==9:
            #nine:
            result=4
    else:
        result="error"
    return result




def mojisu_2keta_10(n : int):
    result=0
    digit_1=int(str(n)[0])
    digit_2=int(str(n)[1])
    if len(str(n))==2:
        if digit_1==1:
            if digit_2==0:
                #ten
                result=3
            elif digit_2==1:
                #eleven
                result=6
            elif digit_2==2:
                #twelve
                result=6
            elif digit_2==3:
                #thirteen
                result=8
            elif digit_2==4:
                #fourteen
                result=8
            elif digit_2==5:
                #fifteen
                result=7
            elif digit_2==6:
                #sixteen
                result=7
            elif digit_2==7:
                #seventeen
                result=9
            elif digit_2==8:
                #eighteen
                result=8
            elif digit_2==9:
                #nineteen
                result=8
        else:
            result="error"
    else:
        result="error"
    return result



def mojisu_2keta_20ikou(n : int):
    result=0
    digit_1=int(str(n)[0])
    digit_2=int(str(n)[1])
    tmp_henkan=mojisu_1keta(digit_2)
    if len(str(n))==2 and 1<digit_1:
        if digit_1==2:
            #twenty-hoge
            result=6+tmp_henkan
        elif digit_1==3:
            #thirty-hoge
            result=6+tmp_henkan
        elif digit_1==4:
            #forty
            result=5+tmp_henkan
        elif digit_1==5:
            #fifty
            result=5+tmp_henkan
        elif digit_1==6:
            #sixty
            result=5+tmp_henkan
        elif digit_1==7:
            #seventy
            result=7+tmp_henkan
        elif digit_1==8:
            #eighty
            result=6+tmp_henkan
        elif digit_1==9:
            #ninety
            result=6+tmp_henkan
    else:
        result="error"
    return result


def mojisu_2keta(n : int):
    result=0
    digit_1=int(str(n)[0])
    digit_2=int(str(n)[1])
    if digit_1==1:
        result=mojisu_2keta_10(n)
    elif digit_1==0:
        result=0
    else:
        result=mojisu_2keta_20ikou(n)
    return result


def mojisu_3keta(n : int):
    result=0
    digit_1=int(str(n)[0])
    digit_2=int(str(n)[1])
    digit_3=int(str(n)[2])
    digit_23=int(str(n)[1:3])
    if len(str(n))==3:
        #hoge hundred and huga ちょうど100の時 and 入らないのでよう修正
        if n in {100, 200, 300, 400,500, 600, 700, 800, 900}:
            result=len("hundred")+mojisu_1keta(digit_1)
        elif digit_2==0:
            result=10+mojisu_1keta(digit_1)+mojisu_1keta(digit_3)
        else:
            result=10+mojisu_1keta(digit_1)+mojisu_2keta(digit_23)
    else:
        result="error"
    return result


def desired_mojisu(n : int):
    result=0
    if len(str(n))==1:
        result=mojisu_1keta(n)
    elif len(str(n))==2:
        result=mojisu_2keta(n)
    elif len(str(n))==3:
        result=mojisu_3keta(n)
    else:
        #n=1000
        result=len("onethousand")
    return result



a=1000
sum=0
for z in range(1, a+1):
    sum+=desired_mojisu(z)

print(sum)