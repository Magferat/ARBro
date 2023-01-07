# link : https://codeforces.com/problemset/problem/991/B

n = int(input())
marks = [int(i) for i in input().split()]
marks.sort()
avg = sum(marks)/n
def checkAvg(i,avg):
    if avg >= 4.5:
        return i
    marks[i] = 5
    avg = sum(marks) / n
    return checkAvg(i+1,avg)
print(checkAvg(0,avg))

