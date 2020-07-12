# YACS 2020.5 乙组 #2
'''小爱有很多 2×2 的积木拼块，现在她打算在一个n×m 的底板上，铺上一些积木拼块，拼块之间不能重合。底板上可能已经存在一些拼块，具体位置由输入给定。请统计小爱有多少种放置拼块的方法。
举例来说，假设在一个3×4 的蓝色底板上，已经存在一个拼块（以红色表示）：
01.png
那么继续放置只有三种可能：
02.png
第一种是不放置新的拼块，第二、第三种可能方案是在绿色部分放置一块拼块。

输入格式
第一行：三个正整数 n，m 与 k；
接下来 k 行，每行两个整数 x_i与 y_i ，表示一个已经存在的拼块，(x_i,y_i) 表示该拼块的左上角位置。

输出格式
单个整数：表示放置拼块的方案数。

样例数据
输入:
3 4 1
2 3
输出:
3

输入:
3 4 0
输出:
11

标准输出: 128 你的输出: 
8 8 5
2 2
2 5
2 7
6 3
6 6
准输出: 27 你的输出:
5 6 2
1 4
2 1
出: 55 你的输出: ['7 5 3\n', '3 2\n', '4 4\n', '6 4\n']
准输出: 1084 你的输出: ['7 6 2\n', '1 4\n', '4 1\n']
标准输出: 15 你的输出: ['6 6 3\n', '2 4\n', '4 1\n', '5 3\n']
 7641 你的输出: ['8 7 3\n', '1 1\n', '1 5\n', '6 3\n']
 输出: 12 你的输出: ['7 6 5\n', '1 1\n', '2 3\n', '4 1\n', '4 4\n', '6 3\n']
 准输出: 1242 你的输出: ['8 7 4\n', '3 3\n', '5 4\n', '6 1\n', '6 6\n']
 出: 87 你的输出: ['6 7 4\n', '1 1\n', '1 4\n', '3 4\n', '4 6\n']
 准输出: 7641 你的输出: ['8 7 3\n', '1 1\n', '1 5\n', '6 3\n']
'''
import numpy as np
n,m,k = map(int,input().split(' '))
arr = np.ones((n,m),dtype=np.int)#np.array(n,m)
points = []
for i in range(k):
    x,y = map(int,input().split(' '))
    points.append([x,y])
    for a,b in [[-1,-1],[-1,0],[0,-1],[0,0]]:
        arr[x+a,y+b] = 0
        if x+a==1: arr[0,y+b]=0
        if y+b==1: arr[x+a,0]=0
        # if x+a==m-1: arr[-1,y+b]=1
        # if y+b==n-1: arr[x+a,-1]=1

all_start_point = set()
print(arr)
start_points = np.nonzero(arr)
for i in range(len(start_points[0])):
    x,y = start_points[0][i],start_points[1][i]
    count = 0
    for a,b in [[-1,0],[1,0],[0,1],[0,-1]]:
        try: 
            if arr[x+a,y+b]: count+=1
        except: pass
    if count>=3:
        points.append([x,y])
    else:
        arr[x,y] = 0
print(points)
print(arr)

