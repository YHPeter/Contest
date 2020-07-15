# YACS 2020.7 乙组 #2
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
输出:3

输入:
3 4 0
输出:11

标准输出: 128 标准输入： 
8 8 5
2 2
2 5
2 7
6 3
6 6

输出: 27
5 6 2
1 4
2 1

输出: 55
7 5 3
3 2
4 4
6 4

输出: 1084
7 6 2
1 4
4 1

输出: 12
7 6 5
1 1
2 3
4 1
4 4
6 3

输出: 1242
8 7 4
3 3
5 4
6 1
6 6

输出: 87 
6 7 4
1 1
1 4
3 4
4 6

准输出: 7641 
8 7 3
1 1
1 5
6 3
标准输出: 15 标准输入： ['6 6 3\n', '2 4\n', '4 1\n', '5 3\n']
标准输出: 7641 标准输入： ['8 7 3\n', '1 1\n', '1 5\n', '6 3\n']
'''

n,m,k = map(int,input().split(' '))
zeros = []
points = []
for i in range(1,n+1):
    for j in range(1,m+1):
        zeros.append([i,j])
for i in range(k):
    x,y = map(int,input().split(' '))
    points.append([x,y])
    for a,b in [[1,1],[1,0],[0,1],[0,0]]:
        try:
            zeros.remove([x+a,y+b])
        except: pass
        try:
            if x+a == 2: zeros.remove([1,y+b])
        except: pass
        try:
            if x+a == n-1: zeros.remove([n,y+b])
        except: pass
        try:
            if y+b == 2: zeros.remove([x+a,1])
        except: pass
        try:
            if y+b == m-1: zeros.remove([x+a,m])
        except: pass

center_point = []
for x,y in zeros:
    flag = True
    for a,b in [[1,1],[1,0],[0,1]]:
        if not [x+a,y+b] in zeros:
            flag = False
            break
    if flag:
        center_point.append([x,y])
ans = 0
def f(ans,can_choose):
    visited = []
    for x,y in can_choose:
        ans+=1
        cur_choose = can_choose[::]
        for h in visited:
            cur_choose.remove(h)
        for a,b in [[0,0],[1,1],[1,0],[0,1],[-1,-1],[-1,0],[0,-1],[1,-1],[-1,1]]:
            if cur_choose==[]: break
            if [x+a,y+b] in cur_choose:
                cur_choose.remove([x+a,y+b])
        if cur_choose!=[]: 
            ans = f(ans,cur_choose)
        visited.append([x,y])
    return ans
x = f(ans,center_point)
print(x+1)