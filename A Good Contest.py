# link: https://codeforces.com/problemset/problem/681/A
t = int(input())
flag = False
while t > 0:
    user = input().split()
    before, after = int(user[1]), int(user[-1])

    if before == after or before < 2400 or before > after:
        t -= 1
    else:
        flag =  True
        break
if flag:
    print('YES')
else:
    print('NO')

