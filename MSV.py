for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    fi=[]
    c=0
    for i in a:
        coun = fi.count(i)
        if coun > c:
            c = coun
        l = 1
        while l * l <= i:
            if i % l == 0:
                fi.append(l)
                if i// l != l:
                    fi.append(i//l)
            l += 1
    print(c)

