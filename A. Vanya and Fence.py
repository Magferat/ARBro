# link: https://codeforces.com/problemset/problem/677/A

n,h = [int(i) for i in input().split()]
heights = [int(i) for i in input().split()]
s = 0
for e in heights:
    if e>h:
        s += 2
    else:
        s += 1
print(s)