n=int(input())
w=input()
fis=""
for i in range(n-1):
        s=""
        if w[i]==w[i+1]:
            l=i
            k=i+1
            while l>=0 and k<=n-1:
                if w[l]==w[k]:
                    s=w[l]+s+w[k]
                else:
                    break
                l-=1
                k+=1
        s1=""
        if n!=0 and w[i-1]==w[i+1]:
            s1=w[i-1]+w[i]+w[i+1]

            l=i-2
            k=i+2
            while l>=0 and k<=n-1:
                if w[l]==w[k]:
                    s1=w[l]+s1+w[k]
                else:
                    break
                l-=1
                k+=1

        if len(s)>len(fis):
            fis=s
        if len(s1)>len(fis):
            fis=s1
print(len(fis))
print(fis)



