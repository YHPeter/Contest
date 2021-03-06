# YACS 2020.7 乙组 #3
'''
区间的最大交集
给定 n 个区间，请从中挑出 k 个区间，使得它们的交集长度到达最大。区间的长度定义为这个区间的右端点与左端点的差。
输入格式
第一行：两个整数 n 与 k；
接下来 n 行：每行两个整数 a_i与 b_i，表示一个区间的左端点与右端点。

输出格式
单个整数：表示交集的最大长度。

输出: 7 输入:
5 2
1 10
5 7
3 6
4 8
2 9

标准输出: 9 输入： 
16 4
14 47
17 19
1 3
9 14
12 28
13 20
12 15
4 5
6 9
12 15
8 16
19 28
14 37
12 20
18 21
3 6
'''
class Queue():
    def __init__(self):
        self.queue = []
    
    def push(self,x):
        self.queue.insert(0,x)
        self.queue.sort(reverse = True)

    def top(self):
        return self.queue[-1]

    def pop(self):
        return self.queue.pop()

n,k = map(int,input().split(' '))
intervals = []
for i in range(n):
    intervals.append(list(map(int,input().split(' '))))
intervals = [[0,0]]+intervals.sort(key = lambda x: x[0])

q = Queue()
for i in range(1,k+1):
    q.push(intervals[i][1])

L = intervals[k][0] # 当前k个的左边界
R = q.top() # 当前右边界的最小值
ans = R - L # 当前答案

for i in range(k+1, n+1):
    L = intervals[i][0]
    q.push(intervals[i][1])
    q.pop()
    R = q.top()
    ans = max(ans, R - L)
print(ans)