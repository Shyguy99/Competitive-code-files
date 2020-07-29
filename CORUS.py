for _ in range(int(input())):
    n,q=list(map(int,input().split()))
    s=list(input())
    s.sort()
    a=[0]*26
    l=97
    for i in range(26):
        a[i]=s.count(chr(l))
        l+=1
    a.sort()
    a=a[::-1]
    for j in range(q):
        c=int(input())
        fin=0
        for x in a:
            if x>c:
                fin+=x-c
            else:
                break
        print(fin)

