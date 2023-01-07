# link : https://codeforces.com/problemset/problem/981/B

def makeDict(n):
    x = {}
    while n > 0:
        name, price = input().split()
        x[name] = int(price)
        n -= 1
    return x
chem = int(input())
chemForces= makeDict(chem)
topch = int(input())
topChemist = makeDict(topch)

s = 0
for key, value in chemForces.items():
    if key in topChemist.keys():
        if value > topChemist[key]:
            topChemist[key] = 0
            s += value
    else:
        s += value

s += sum(topChemist.values())
print(s)