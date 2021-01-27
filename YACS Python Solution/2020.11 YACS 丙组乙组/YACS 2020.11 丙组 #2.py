a = input()
ans = 0
cur = 1
for i in a:
    if i=='Y':
        ans+=cur
        if cur<5: cur+=1
    elif i=='N':
        cur = 1
print(ans)