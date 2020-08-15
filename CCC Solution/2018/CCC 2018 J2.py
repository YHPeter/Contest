# Q2
n = int(input())
l1,l2 = input(),input()
ans = 0
for i in range(n):
    if l1[i]=='C' and l2[i]=='C': ans+=1
print(ans)
