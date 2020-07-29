b,l,d=list(map(int,input().split()))
s=list(map(int,input().split()))
p=[]
Dict={}
for i in range(l):
    su=0
    n,t,m=list(map(int,input().split()))
    ni=list(map(int,input().split()))
    p.append([n,t,m,ni])
    su=d-t
    no=su*m
    if no>n:
        no=n
    c=[]    
    for j in ni:
        c.append(s[j])
    c.sort()
    c=c[::-1]
    suum=0
    for q in range(no):
        suum=suum+c[q]
    Dict[i]=suum
ld=len(Dict)    
nof=0
fin=[]
sett=set()
for i in range(ld):
    max_key = max(Dict, key=Dict.get)
    k=p[max_key]
    d=d-k[1]
    if d<=0 or len(sett)>=b:
        break
    nof+=1
    no=d*k[2]
    if no>k[0]:
        no=k[0]
    c=[]
       
    for j in k[3]:
        c.append(s[j])
    c.sort()
    c=c[::-1]
    suum=0
    fin2=[]
    for i in range(no):
        if s.index(c[i]) not in sett:
          fin2.append(s.index(c[i]))
          sett.add(s.index(c[i]))     
    fin1=[max_key,len(fin2)]  
    fin.append([fin1,fin2])
    del Dict[max_key]
print(nof)
for o in range(nof):
     print(*fin[o][0])
     tt=fin[o][1]
     print(*tt)
        
          