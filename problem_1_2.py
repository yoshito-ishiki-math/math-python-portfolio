#if文とelifで頑張る
total=0
for z in range (1000):
    if z%15==00:
        total+=z
    elif z%3==0:
        total+=z
    elif z%5==0:
        total+=z
    else:
        pass

print(total)