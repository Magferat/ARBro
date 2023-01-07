# link: https://codeforces.com/problemset/problem/581/A

red, blue = [int(i) for i in input().split()]
hip = min(red,blue)
m =max(red,blue)-hip
print(hip, m//2)