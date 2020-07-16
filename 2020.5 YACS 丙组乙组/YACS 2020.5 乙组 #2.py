# YACS 2020.5 乙组 #2
'''
题目背景
中国正在以前所未有的力度推进脱贫攻坚，国家计划在2020年使得在现行标准下的贫困人口实现全面脱贫，为此，需要对居民的经济状况进行普查。

题目描述
给定一个正整数 nn，表示人口数量。一开始，每个居民拥有的财产记为 a1, a2,... an，财产可能发生两种变化：
一种来源于个体，由某个居民的经济活动而产生。在某个时刻，某个居民的财产会直接变成某个数值，可能升高也可能降低。
一种来源于政策，在某个时刻，国家会对财产低于某个标准线全部的居民，实施政策支持，使得他们的财产全部正好到达标准线。
给定这些变化的详细参数，请做一次统计，输出每个居民最后拥有的财产数量。

输入格式
第一行：两个正整数 n 和 m；
第二行：nn个正整数表示 a1,a2,a3....an
接下来 m 行：每行依次表示一次财产变化：
以字母 i 开头的表示一次个体变化，后接两个整数参数 u 和 t，u表示财产发生变化的居民编号，tt 表示财产变化的结果；
以字母 p 开头的表示一次政策变化，后接一个整数参数 s，s 表示政策的标准线。

输出格式
共 n 行：第 ii 行有一个整数，表示 ii 号居民最后拥有的财产数量。

样例数据
输入:
4 3
10 20 30 40
p 35
i 1 20
p 25
输出:
25
35
35
40
代码提交区域
'''

# 优化分四种情况 sample answer from https://iai.sh.cn/contribution/104

n,m = list(map(int,input().split(' '))) # n个人 m次政策和调整
a=[0]+list(map(int,input().split(' ')))
ans,pos,value = [0]*200010,[0]*200010,[0]*200010
max_line = 0
for i in range(1,m+1):
    op = input().split(' ')
    if op[0]=='i': pos[i],value[i] = int(op[1]),int(op[2])
    else: value[i] = int(op[1])

for i in range(m,-1,-1):
    if pos[i]==0: 
        max_line = max(max_line,value[i])
    else: 
        if ans[pos[i]]==0: ans[pos[i]]=max(max_line,value[i])

for i in range(1,n+1):
    if ans[i]==0: print(max(a[i],max_line))


# 无优化 30分
n,m = list(map(int,input().split(' '))) # n个人 m次政策和调整
ini=[0]+list(map(int,input().split(' ')))
citizen={}
for i in range(1,len(ini)):
    citizen[i]=ini[i]
max_p = 0
for i in range(m):
    a = input().split(' ')
    if a[0]=='p':
        for i in citizen.keys():
            citizen[i]=max(citizen[i],int(a[1]))
    elif a[0]=='i':
        citizen[int(a[1])] = int(int(a[2]))
for i in citizen.keys():
    x = citizen.get(i)
    if x==None: print(max_p)
    else: print(x)