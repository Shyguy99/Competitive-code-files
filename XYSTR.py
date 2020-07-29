for _ in range(int(input())):
    s=input()
    n=len(s)
    i=0
    pair=0
    while i<n-1:
        if s[i]!=s[i+1]:
            pair+=1
            i+=2
        else:
            i+=1
    print(pair)


