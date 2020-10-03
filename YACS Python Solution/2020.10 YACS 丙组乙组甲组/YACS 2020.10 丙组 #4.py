n = int(input())
a,b = list(map(int,input().split())),list(map(int,input().split()))

minprice = a[0]
maxprofit = 0
for i in range(1,n):
    minprice = min(minprice, a[i])
    maxprofit = max(maxprofit, b[i] - minprice)
print(maxprofit)