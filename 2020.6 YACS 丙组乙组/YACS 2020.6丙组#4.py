# YACS 2020.6丙组#4.py
n,m = map(int,input().split(' '))
stock = []
total = 0
flag = False
for i in range(n):
    p,c = map(int,input().split())
    stock.append(p)
    if c==0:
        continue
    else:
        cur = 0
        x = max(i-m,0)
        for j in range(x,i+1):
            if stock[j]==0: continue
            cur += stock[j]
            if cur>c:
                total += c
                stock[j] = cur-c
                flag = True
                break
            else:
                stock[j] = 0
        if not flag:
            total+=cur
print(total)

# # YACS 2020.6丙组#4.py
# n,m = map(int,input().split(' '))
# stock = [0]*(m+1)
# total_stock,ans = 0,0
# total = 0
# flag = False
# for i in range(n):
#     p,c = map(int,input().split())
# #     stock.insert(0,p)
# #     total_stock+=p
# #     if c==0:
# #         continue
# #     elif c>=sum(stock):
# #         # total_stock = 0
# #         stock = [0]*m
# #         ans+=sum(stock)
# #     for j in range(m-1,-1,-1):
# #         c-=stock[j]
# #         if c<0:
# #             stock[i]==abs(c)
# #             ans+=c
# #             break
# #     # total_stock-=stock.pop()
# # print(ans)
#     if c==0:
#         continue
#     else:
#         cur = 0
#         x = max(i-m,0)
#         for j in range(x,i+1):
#             if stock[j]==0: continue
#             cur += stock[j]
#             if cur>c:
#                 total += c
#                 stock[j] = cur-c
#                 flag = True
#                 break
#             else:
#                 stock[j] = 0
#         if not flag:
#             total+=cur
# print(total)