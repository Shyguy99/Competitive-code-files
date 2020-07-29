#FAILED
for _ in range(int(input())):
    r,c=list(map(int,input().split()))
    a=[]
    for i in range(1,r+1):
        for j in range(1,c+1):
            a.append([i,j])
    print(a)
    m=a[0]
    mm=[m]
    for k in range((r*c)-1):
        i = 0
        while i<len(a):
            if m[0]!=a[i][0] and m[1]!=a[i][1] and m[0]-m[1]!=a[i][0]-a[i][1] and m[0]+m[1]!=a[i][0]+a[i][1]:
                c=a[i]
                a.remove(m)
                m=c
                mm.append(m)
                print(m)
                print(a)
                break
            if i==len(a)-1:
                c=0
            i+=1
        if c==0:
            print("IMPOSSIBLE")
            break
    if len(a)==1:
        mm.append(a[0])
        print("POSSIBLE")
        for s in mm:
            print(*s)
