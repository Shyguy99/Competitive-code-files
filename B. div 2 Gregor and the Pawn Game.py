for _ in range(int(input())):
    n=int(input())
    a=list(input())
    b=list(input())

    c=0
    for i in range(len(b)):
        if b[i]=='1':
            if i-1!=-1 and a[i-1]=='1':
                a[i-1]='-1'
                c+=1
            elif a[i]=='0':
                 a[i]='-1'
                 c+=1
            elif i+1!=n and a[i+1]=='1':
                c+=1
                a[i+1]='-1'
    print(c)