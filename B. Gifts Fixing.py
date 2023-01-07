t = int(input())
while t > 0:
    gifts = int(input())
    candy = [int(i) for i in input().split()]
    orange = [int(i) for i in input().split()]
    x = min(candy)
    y = min(orange)
    newCandy = [i-x for i in candy]
    newOrange = [i-y for i in orange]
    final = 0
    for i in range(gifts):
        final += max(newCandy[i], newOrange[i])
    print(final)
    t -= 1


# link: https://codeforces.com/problemset/problem/1399/B