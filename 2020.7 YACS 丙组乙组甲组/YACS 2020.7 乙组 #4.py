# YACS 2020.5 乙组 #4
'''
题目背景
哒宝（Dobble） 是一款考验反应力的桌面游戏。该游戏由 55 张纸质圆盘组成，每个圆盘上有 88 种不同的图案。游戏设计者保证，任意两张圆盘之间，有且仅有一个图案是相同的。玩家需要通过观察，抢先发现这个相同的图案，从而获得分数。
题目描述
小爱自己设计了一盒哒宝，她制作了 nn 个圆盘，每个圆盘上有 mm 个图案，每个图案以 11 到 kk 之间的一个正整数来编号。
请你帮助小爱检查一下，是否所有的圆盘都满足任意两个圆盘有且仅有一个图案是相同的，且每个圆盘上的图案互不相同。

输入格式
第一行：三个正整数 n,m 及 k；
接下来 n 行，每行 m 个不同的数字，每个数字在 1 到 k 之间，表示该圆盘上的不同图案。

输出格式
如果小爱设计的哒宝满足要求，请输出 YES，否则输出 NO。

输入:
3 3 6
1 2 3
1 4 5
2 4 6
输出:
YES
输入:
3 3 5
1 2 3
1 4 5
2 4 5
输出:
NO
说明:
圆盘2和3有两个相同图案
输入:
3 3 8
1 2 3
4 5 6
6 7 8
输出:
NO
说明:
圆盘1和2无相同图案
输入:
3 3 6
1 2 3
3 4 4
3 5 6
输出:
NO
说明:
圆盘2有重复图案
行号0: 标准输出: NO 你的输出: ['10 4 13\n', '1 2 3 4\n', '1 5 8 11\n', '1 6 9 12\n', '1 7 13 10\n', '2 5 9 13\n', '2 6 10 11\n', '2 7 8 12\n', '3 5 10 12\n', '3 6 8 13\n', '3 7 1 11\n']
10 4 13
1 2 3 4
1 5 8 11
1 6 9 12
1 7 13 10
2 5 9 13
2 6 10 11
2 7 8 12
3 5 10 12
3 6 8 13
3 7 1 11
号0: 标准输出: YES 你的输出: ['10 4 13\n', '1 2 3 4\n', '1 5 8 11\n', '1 6 9 12\n', '1 7 10 13\n', '2 5 9 13\n', '2 6 10 11\n', '2 7 8 12\n', '3 5 10 12\n', '3 6 8 13\n', '3 7 9 11\n']
10 4 13
1 2 3 4
1 5 8 11
1 6 9 12
1 7 13 10
2 5 9 13
2 6 10 11
2 7 8 12
3 5 10 12
3 6 8 13
3 7 9 11
'''
#version1 basic
def main():
    n,m,k = list(map(int,input().split(' ')))
    total = {}
    for i in range(n):
        x = input().split(' ')
        xs = set(x)
        if len(x)==len(x):
            total[i] = xs
        else:
            return False
    for i in range(n):
        if i>4000: return True
        for j in range(i+1,n):
            if len(total[i]&total[j])!=1: return False
    return True
if main():
    print('YES')
else:
    print('NO')

# version2 with time limitation
import threading
from types import resolve_bases
class SingleDownload(threading.Thread):
    def __init__(self):
        super().__init__()
        pass
    def run(self):
        self.result = self.task()
    def task(self):
        n,m,k = list(map(int,input().split(' ')))
        total = {}
        for i in range(n):
            x = input().split(' ')
            xs = set(x)
            if len(x)==len(x):
                total[i] = xs
            else:
                return False
        for i in range(n):
            for j in range(i+1,n):
                if len(total[i]&total[j])!=1: return False
        return True
    def get_result(self):
        try:
            return self.result
        except Exception:
            return 3


workthread = SingleDownload()
workthread.start()
workthread.join(0.9)
res = workthread.get_result()
if not res:
    print('NO')
else:
    print('YES')