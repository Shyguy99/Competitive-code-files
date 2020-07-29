for _ in range(int(input())):
    n=int(input())
    a1=list(map(int,input().split()))
    a2 = list(map(int, input().split()))
    a1.sort()
    a2.sort()
    j=0
    i=0
    c=0
    while i<n and j<n:
        if a2[i]<a1[j]:
            c+=1
            i+=1
            j+=1
        else:
            j+=1
    print(c)

