n = int(input())
line = list(map(int,input().split()))
total = sum(line)
cur = 0
minnum = 999999
for i in line:
    cur+=i
    minnum = min(abs(total-cur*2), minnum)
print(minnum)