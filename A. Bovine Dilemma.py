for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    fin=set()
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            ar1=a[i]/2
            ar2=a[j]/2
            ar3=ar2-ar1
            if ar3 not in fin:
                fin.add(ar3)
    print(len(fin))