suf=0
for _ in range(int(input())):
    n=int(input())
    a=[0]*4
    b=[0]*4
    c=[0]*4
    d=[0]*4
    for i in range(n):
        le,ti=list(map(str,input().split()))
        if le=='A':
            if ti=='3':
                a[0]+=1
            elif ti=='6':
                a[1]+=1
            elif ti=='9':
                a[2]+=1
            elif ti=='12':
                a[3]+=1    
        elif le=='B':
            if ti=='3':
                b[0]+=1
            elif ti=='6':
                b[1]+=1
            elif ti=='9':
                b[2]+=1
            elif ti=='12':
                b[3]+=1  
        elif le=='C':
            if ti=='3':
                c[0]+=1
            elif ti=='6':
                c[1]+=1
            elif ti=='9':
                c[2]+=1
            elif ti=='12':
                c[3]+=1    
        elif le=='D':
            if ti=='3':
                d[0]+=1
            elif ti=='6':
                d[1]+=1
            elif ti=='9':
                d[2]+=1
            elif ti=='12':
                d[3]+=1  
    p=['a','b','c','d']  
    mon=[100,75,50,25]
    su=0          
    for i in range(4):
        k=0
        for j in p:
            if j=='a':
               mm=max(a)
               t=j
               ti=a.index(mm)
            elif j=='b':
               mm=max(b)
               t=j
               ti=b.index(mm)
            elif j=='c':
                mm=max(c)
                t=j
                ti=c.index(mm)
            elif j=='d':
                mm=max(d)
                t=j
                ti=d.index(mm)
            if mm>=k:
                k=mm
                t1=t
                ti1=ti
              
                
        if k==0:
            su=su-100
        else:
            su+=mon[i]*k
        p.remove(t1)
        a[ti1]=0
        b[ti1]=0
        c[ti1]=0
        d[ti1]=0
    suf=suf+su
    print(su)
print(suf)        
                
#####################partial correct
