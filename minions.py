def merge_the_tools(l, k):
    print(len(l))
    for i in range(0,len(l),k):
        print(i)
        a=l[i:i+k]
        s=""
        for j in range(len(a)):
            if a[j] not in s:
                s=s+a[j]
        print(s)
l=input()
k=int(input())
merge_the_tools(l,k)        