for _ in range(int(input())):
    a=input()
    b=input()

    maxx=0
    for i in range(len(a)):
        for j in range(i,len(a)):
            if a[i:j+1] in b:
                maxx=max(maxx,j-i+1)
    fin=0
    fin+=len(a)-maxx
    fin+=len(b)-maxx
    print(fin)