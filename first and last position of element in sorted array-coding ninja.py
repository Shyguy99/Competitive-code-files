from sys import stdin, stdout, setrecursionlimit

setrecursionlimit(10 ** 7)


def findFirstLastPosition(arr, N, X):
    def ser(arr, target):
        low = 0
        high = len(arr)
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return -1

    r = ser(arr, X)
    if r == -1:
        return (-1, -1)
    else:
        low = 0
        high = r

        ans1=-1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == X:
                high = mid - 1
            elif arr[mid] < X:
                low = mid + 1
                ans1 = mid
        if ans1==-1:
            ans1=-1
        low = r
        high = len(arr) - 1
        ans2=-1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == X:
                low = mid + 1
            elif arr[mid] >= X:
                ans2 = mid
                high = mid - 1
        if ans2==-1:
            ans2=len(arr)
        return (ans1 + 1, ans2 - 1)

    # Taking input using fast I/0


def takeInput():
    N = int(stdin.readline())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    X = int(stdin.readline())
    return N, arr, X


tc = int(input())
while tc > 0:
    N, arr, X = takeInput()
    ans = findFirstLastPosition(arr, N, X)
    stdout.write(str(ans[0]) + " " + str(ans[1]) + "\n")
    tc -= 1
