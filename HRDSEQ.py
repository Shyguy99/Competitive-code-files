for _ in range(int(input())):
    f=[0]
    for i in range(128):
        a=f[-1]
        ff=f[:-1]
        if a in ff:
            fff=ff[::-1]
            p=fff.index(a)+1
            f.append(p)
        else:
            f.append(0)
    n=int(input())
    k=f[:n]
    print(k.count(f[n-1]))

