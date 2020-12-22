for i in range(int(input())):
    n=int(input())
    s=input()
    a=s.count('1')
    r=120-len(s)+a
    if r/120*100>75:
        print("YES")
    else:
        print("NO")