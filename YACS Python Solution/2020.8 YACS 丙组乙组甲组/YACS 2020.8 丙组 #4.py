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
counts = [i for i in Counter(a).values()]
counts.sort()
print(sum(counts[:k-1]))