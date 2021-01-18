import sys


def inp():
    temp = input()
    return (int(temp))


def inlt():
    temp = input()
    return (list(map(int, temp.split())))


def insr():
    s = input()
    return (list(s[:len(s) - 1]))


def invr():
    return (map(int, input().split()))


def solve(x, array):
    maxSum = sum([(number + x - 1) // x for number in array])
    minSum = (sum(array) + x - 1) // x
    print(minSum, maxSum)


n = inp()
for i in range(n):
    xn = inlt()
    x = xn[0]
    n = xn[1]
    array = inlt()
    solve(x, array)
