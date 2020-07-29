for _ in range(int(input())):
    n,k=list(map(int,input().split()))
    a=list(input())
    if '1' in a:
        cout=1
        minn = 0
        for i in range(len(a) - 1):
            if a[i] == '1' and a[i + 1] == '1':
                cout += 1
            else:
                if cout > minn:
                    minn = cout
                    l=i
                cout = 1
        if i+1-minn>=k or len(a)-i+1>=k:
            print(minn+k)
        else:
            m=max(i+1-minn,len(a)-i-1)
            print(minn+m)
    else:
        if k<=len(a):
            print(k)
        else:
            print(len(a))

    #wrong ans

