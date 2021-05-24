## Read input as specified in the question.
## Print output as specified in the question.
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    m = input()
    b = list(map(int, input().split()))

    fin = []
    b.sort()
    for i in a:

        low = 0
        high = len(b) - 1
        ans = -1
        while low <= high:
            mid = (low + high) // 2

            if b[mid] <= i:
                ans = mid
                low = mid + 1
            else:
               high=mid-1
        if ans == -1:
            fin.append(0)
        else:
            fin.append(ans + 1)
    print(*fin)