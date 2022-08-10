import bisect

rows, cols = (51, 100001)
bit = [[0] * cols] * rows


def convertToPermutation(arr, N):
    temp = [0 for i in range(N)]
    for i in range(0, N):
        temp[i] = arr[i]

    temp.sort()

    for i in range(0, N):
        res = bisect.bisect_left(temp, arr[i], 0, len(temp))
        arr[i] = (res - temp[i]) + 1


def update(l, i, val, n):
    while i <= n:
        bit[l][i] = bit[l][i] + val
        i = i + (i & (-i))


def FindSum(l, i):
    sum = 0
    while i > 0:
        sum = sum + bit[l][i]
        i = i - (i & (-i))

    return sum


def findInversionsCount(arr, n, k):
    for i in range(n - 1, 0, -1):
        curr = arr[i]
        update(1, curr, 1, n)
        for j in range(1, k):
            s = FindSum(j, curr - 1)
            update(j + 1, curr, s, n)

    return FindSum(k, n)


N = 5
arr = [8, 7, 1, 6, 2]
K = 3
convertToPermutation(arr, N)
inversionsCount = findInversionsCount(arr, N, K)
print("The count of inversions: ", inversionsCount)
