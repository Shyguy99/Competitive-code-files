for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    if a.count(max(a))>1:
        print("NO")
    else:
        aset1=set()
        aset3=[]
        for i in a:
            if i not in aset1:
                aset1.add(i)
            else:
                aset3.append(i)
        aset1=list(aset1)
        aset1.sort()
        aset3.sort()
        aset3=aset3[::-1]
        chk = 0
        for j in range(len(aset3)-1):
            if aset3[j]==aset3[j+1]:
                print("NO")
                chk=1
                break
        if chk==0:
            fin = aset1 + aset3
            print("YES")
            print(*fin)


        #aset1=list(set(a))
        #if len(aset)==len(a):
            #print("YES")
            #t=a[:]
            #t.sort()
            #print(*t)
        #else:
            #aset2 = a[:]
            #for i in aset:
                #aset2.remove(i)
            #aset3=list(set(aset2))
            #if len(aset3)==len(aset2):
                #aset2.sort()
                #aset2=aset2[::-1]
                #aset.sort()
                #print("YES")
                #print(*(aset+aset2))
            #else:
                #print("NO")
