# YACS 2020.8 丙组 #4
'''
样例数据
输入:
5 2
1 1 2 2 5
输出:
1
输入:
10 3
5 1 3 2 4 1 1 2 3 4
输出:
3
输入:
3 3
3 1 2
输出: 0
输入:
18 7
11 3 15 1 6 6 3 6 5 8 10 8 2 17 11 10 3 3
输出: 3
'''
def stdinput():
    '''simple input function'''
    def strint(x):
        try: return int(x)
        except: return x
    return list(map(strint,input().strip().split()))

n, k = stdinput()
a = stdinput()
from typing import Counter
counts = sorted([i for i in Counter(a).values()])
if len(counts)<=k:print(0)
else: print(sum(counts[:len(counts)-k]))