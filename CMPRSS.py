for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.append(0)
    k=a[0]
    c=0
    s=""
    for i in range(len(a)-1):
        if a[i+1]==a[i]+1:
            b=a[i+1]
            c+=1
        else:
            if c>=2:
                s=s+","+str(k)+"..."+str(b)
            elif c==1:
                s=s+","+str(k)+","+str(b)
            elif c==0:
                s=s+","+str(k)
            c=0
            k=a[i+1]
    s=s[1:]
    print(s)
