# YACS 2020.7 乙组 #3
'''
区间的最大交集
给定 n 个区间，请从中挑出 k 个区间，使得它们的交集长度到达最大。区间的长度定义为这个区间的右端点与左端点的差。
输入格式
第一行：两个整数 n 与 k；
接下来 n 行：每行两个整数 a_i与 b_i，表示一个区间的左端点与右端点。

输出格式
单个整数：表示交集的最大长度。
样例数据
输入:
5 2
1 10
5 7
3 6
4 8
2 9
输出:
7
: 标准输出: 9 你的输出 
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
import numpy as np

n,k = list(map(int,input().split(' ')))
all_interval = []
rl = []
ll = []
basic_line = np.zeros((n,300*1000+13),dtype = np.int)
print(basic_line)
max_pos,min_pos = 0, 0

for i in range(n):
    l,r = list(map(int,input().split(' ')))
    basic_line[i][l:r] = 1
    print(basic_line[i][:r+3])
    max_pos,min_pos = max(max_pos, r),min(min_pos, l)
basic_line = basic_line[...,:max_pos]

sum_column = np.sum(basic_line,axis = 0)
np.set_printoptions(threshold=np.inf)
print(sum_column)
nozeros = np.nonzero(basic_line[...,9])
print(nozeros)
pre_list = np.array([0]*n)
max_ = np.array([0]*n)

for i in range(min_pos,max_pos):
    if sum_column[i]<k:
        pre_list = np.array([0]*n)
        break
    cur_list = np.nonzero(basic_line[...,i])[0]

    for i in cur_list:
        if i in pre_list:
            continue
        else:
            max_[i] = 1
    for i in cur_list:
        if i in cur_list:
            continue
        else:
            max_[i] = 1