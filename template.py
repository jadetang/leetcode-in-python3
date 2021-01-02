import sys
def inp():
    temp = input()
    return(int(temp))

def inlt():
    temp = input()
    return(list(map(int,temp.split())))

def insr():
    s = input()
    return(list(s[:len(s) - 1]))

def invr():
    return(map(int,input().split()))

def solve(n, d, s):
    reach = [sys.maxsize] * n
    reach[0] = 0
    for i, c in enumerate(s):
        if c == '0':
            continue
        for j in range(i - 1, i - d - 1, -1):
            if reach[j] != sys.maxsize:
                reach[i] = min(reach[i], reach[j] + 1)
    #print(reach)
    return reach[-1] if reach[-1] != sys.maxsize else -1

n = inlt()
s = input()

print(solve(n[0], n[1], s))
