# link: https://codeforces.com/problemset/problem/1176/A

t = int(input())
while t >0:
    n = int(input())
    move = 0
    while n > 1:
        if n%2 == 0:
            move += 1
            n = n // 2
        elif n % 3 == 0:
            move += 1
            n = 2 * n // 3
        elif n % 5 == 0:
            move += 1
            n = 4 * n // 5
        else:
            n = 0
            move = -1
    print(move)
    t -= 1
