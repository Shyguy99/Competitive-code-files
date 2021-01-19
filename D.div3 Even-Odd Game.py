for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    def f(n,a):
        ev_c=[]
        od_c=[]
        for i in a:
            if i%2==0:
                ev_c.append(i)
            else:
               od_c.append(i)
        if len(ev_c)==0 and len(od_c)>1:
            return("Bob")
        if len(od_c)==0:
            return("Alice")
        ev_c.sort()
        od_c.sort()
        ce=0
        co=0
        chance=1
        for j in range(n):
            if chance:
               if len(ev_c)!=0 and len(od_c)!=0 and ev_c[-1]>=od_c[-1]:
                   ce+=ev_c.pop()
                   chance=0
               elif len(od_c)!=0:
                   od_c.pop()
                   chance=0
               else:
                   ce+=ev_c.pop()
                   chance=0
            else:
                  if len(ev_c)!=0 and len(od_c)!=0 and od_c[-1]>=ev_c[-1]:
                      co+=od_c.pop()
                      chance=1
                  elif len(ev_c)!=0:
                      ev_c.pop()
                      chance = 1
                  else:
                      co += od_c.pop()
                      chance = 1

        if ce>co:
            return("Alice")
        elif co>ce:
            return("Bob")
        else:
            return("Tie")
    print(f(n,a))