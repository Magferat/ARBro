# link: https://codeforces.com/problemset/problem/595/A

n,m = [int(i) for i in input().split()]
s= 0
while n > 0:
    array = [int(i) for i in input().split()]
    i = 0
    while i < 2*m:
        temp = array[i:i+2:]
        if 1 in temp:
            s += 1
        i += 2
    n -= 1

print(s)

