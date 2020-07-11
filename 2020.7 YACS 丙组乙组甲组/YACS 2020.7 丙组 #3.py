# YACS 2020.7 丙组 #3
# 倍数区间

# test: ... out:4
'''
4 2
3 2 4 1
'''


n,k = map(int,input().split(' '))
a = list(map(lambda x: int(x)%k,input().split(' ')))
count=0
arr = [[0]*n for _ in range(n)]
# print(a)
for i in range(n):
    arr[i][i] = a[i]
    for j in range(i,n):
        if j!=i:
            arr[i][j] = (arr[i][j-1]+a[j])%k
        if arr[i][j]==0: count+=1
# for i in arr:
#     print(i)
print(count)

        