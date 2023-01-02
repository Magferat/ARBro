# link : https://codeforces.com/problemset/problem/734/B

s = [int(i) for i in input().split()]
num256 = [s[0], s[2], s[3]]
x = min(num256)
num32 = [s[0]-x, s[1]]
y = min(num32)
print(256*x+32*y)
