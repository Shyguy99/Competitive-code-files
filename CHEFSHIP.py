for _ in range(int(input())):
    s=input()
    n=len(s)
    r = int(n / 2)

    if s.count(str(s[0]))==n:
        print(r-1)
    else:
        cout=0
        for i in range(1,r):
            z=2*i
            zl=n-z
            zh=int(z/2)
            zhl=int(zl/2)
            if s[:zh]==s[zh:zh+zh] and s[zh+zh:zh+zh+zhl]==s[zh+zh+zhl:]:
                cout+=1
        if cout>0:
            print(cout)
        else:
            print(0)
