def rmax(a : int):
    desired_r=2
    for n in range(1, a, 2):
        tmp_r=(2 * a * n) % (a**2)
        desired_r=max(desired_r, tmp_r)
    return desired_r


def rmax_2(a):
    return a*(a - (2- a%2))


def print_residue(a):
    for n in range(1, a):
        print(f"{n}; desired value={((a+1)**n + (a-1)**n) % (a**2)}, rmax_2={rmax_2(a)}")
    return


print_residue(5)