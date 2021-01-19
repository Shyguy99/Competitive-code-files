for _ in range(int(input())):
    s=list(input())
    c=0
    for i in range(len(s)):
        if i!=0:

            r1=[]
            r=[]
            if i>1:
                r1.append(s[i-1])
                r1.append(s[i-2])
                r.append(s[i - 1])
                r.append(s[i - 2])
            else:
                   r1.append(s[0])

            if i<len(s)-2:
                r.append(s[i+1])
                r.append(s[i+2])
            else:
                if i==len(s)-2:
                    r.append(s[i+1])
            if s[i] in r1:
                  for j in range(97,97+26):
                        if chr(j) not in r:
                            s[i]=chr(j)
                            c+=1
                            break
    print(c)
