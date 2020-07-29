for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    oc=[]
    do=[]
    tmpo=1
    chk=0
    a.append(-1)
    for i in range(len(a)-1):
        if a[i] in do:
            chk=1
            print("NO")
            break
        else:
            if a[i]==a[i+1]:
              tmpo+=1
            else:
              if tmpo in oc:
                  chk=1
                  print("NO")
                  break
              else:
                  oc.append(tmpo)
                  tmpo=1
                  do.append(a[i])
    if chk==0:
        print("YES")

