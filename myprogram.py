h=int(input())
holes=list(map(int,input().split()))
hcount=[0]*h     #balls in holes
b=int(input())
balls=list(map(int,input().split()))
l=[0]*b  #final list

for i in range(len(holes)):
    for j in range(len(balls)):
        if hcount[i] < i + 1:
            print(hcount[i])
            if balls[j]<=holes[i]:
                l[j]=i+1
                hcount[i]+=1
                print(l[j],hcount[i])

print(l)