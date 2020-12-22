for i in range(int(input())):
    s=input()
    if len(s)%2==0:
        one=s.count('1')
        zero=s.count('0')
        if one==len(s) or zero==len(s):
            print(-1)

        elif one==zero:
            print(0)
        else:
            k=min(one,zero)
            r=len(s)/2
            print(int(r-k))
    else:
        print(-1)