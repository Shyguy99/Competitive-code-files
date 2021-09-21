for _ in range(int(input())):

    n=int(input())
    s=input()

    def solve(s,k):
        if len(s)==1:
            if s==k:
                return 0
            else:
                return 1

        a1=len(s)//2-s[:(len(s)//2)].count(k)
        a2=len(s)//2-s[(len(s)//2):].count(k)
        k=chr(ord(k)+1)

        p1=a1+ solve(s[(len(s)//2):],k)
        p2=a2+solve(s[:(len(s)//2)],k)
        return min(p1,p2)
    print(solve(s,'a'))