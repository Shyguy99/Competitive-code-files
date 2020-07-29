for z in range(1,int(input())+1):
    n=int(input())
    v=list(map(int,input().split()))

    def  TroubleSort(v):
       done = False
       while not done:
           done = True
           for i in range(len(v)-2):
             if v[i] > v[i+2]:
               done = False
               tt=v[i]
               v[i]=v[i+2]
               v[i+2]=tt
       return v
    v=TroubleSort(v)
    print(v)
    t=v[:]
    t.sort()
    if t==v:
        print("Case #{}: {}".format(z,"OK"))
    else:
       for i in range(len(t)):
          if v[i]!=t[i]:
              print("Case #{}: {}".format(z,i))
              break


