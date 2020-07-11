# YACS 2020.7 丙组 #5
# 游戏闯关

n,t = map(int,input().split(' '))
a = map(int,input().strip().split(' '))
b = map(int,input().strip().split(' '))

dp = [[0]*n for i in range(n)]


# a[0] = int(a[0])
# b[0] = int(b[0])
# for i in range(1,n):
#     a[i] = int(a[i])+a[i-1]
# for i in range(1,n):
#     b[i] = int(b[i])+b[i-1]
# print(a,b)
# c = sorted(a+b)
# pre = 0
# for i in range(2*n):
#     pre+=c[i]
#     if pre>t:
#         break
#         print(i)

'''
4 22
6 8 10 7 
7 11 9 9
'''