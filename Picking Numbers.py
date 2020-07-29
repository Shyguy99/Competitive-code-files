a=list(map(int,input().split()))
a.sort()
fi = 0
for i in a:
    t = 0
    for j in a:
        if (i - j) ==-1 or i-j==0:
            t += 1
    if fi < t:
        fi = t
print(fi)