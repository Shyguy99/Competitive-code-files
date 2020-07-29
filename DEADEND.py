for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    cout=0
    j=1
    a.sort()
    a.insert(0,0)
    a.insert(len(a),0)
    for i in range(1,len(a)-1):
         if a[j]-a[j-1]!=1 and a[j]-a[j+1]!=-1:
                a.insert(j+1,a[j]+1)
                cout+=1
                j+=2
         else:
             j+=1
    print(cout)

