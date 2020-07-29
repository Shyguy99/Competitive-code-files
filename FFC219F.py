for _ in range(int(input())):
    n,p=list(map(int,input().split()))
    a=list(map(int,input().split()))
    a.sort()
    coun=0
    for i in a:
        if p<i:
            break
        else:
            p=p-i
            coun+=1
    print(coun)