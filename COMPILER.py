# cook your dish here
testcases = int(input())

for i in range(0,testcases):
    ans = 0
    n = input()
    count = 0
    for i in range(0,len(n)):
        if n[i] == "<":
            count += 1
        else:
            count -= 1
        if(count == 0):
            ans = i + 1
        elif(count < 0):
            break
    print(ans)