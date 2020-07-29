for z in range(1,int(input())+1):
    n=int(input())
    l=list(map(int,input().split()))
    print("Case #{}:".format(z),end=" ")
    for j in range(n):
        s=l[:j+1]
        s.sort(reverse=True)
        for i in range(1,len(s)+1):
            t=len(s)-i
            if s[t]>=t+1:
                print(t+1,end=" ")
                break
    print()

#TEST CASE 1 ONLY