for _ in range(int(input())):
    s=input()
    if len(s)%2==0:
        a=int((len(s)/2))
        s1=s[:a]
        s2=s[a:]
    else:
        a=(int(len(s)/2))
        s1=s[:a]
        s2 = s[a+1:]
    s1=list(s1)
    s2=list(s2)
    s1.sort()
    s2.sort()
    if s1==s2:
            print("YES")
    else:
            print("NO")