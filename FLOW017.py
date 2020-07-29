for _ in range(int(input())):
    li=list(map(int,input().split()))
    for x in range(len(li)):
        if li[x]==max(li):
            li.pop(x)
            break
    print(max(li))