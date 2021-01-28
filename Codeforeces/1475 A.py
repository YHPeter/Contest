import math, itertools, functools

def solve():
    n = int(input())
    while True:
        if n==1 or n==0: return False
        if n%2==1: return True
        n = n//2

for _ in range(int(input())):
    print('YES') if solve() else print('NO')

'''
6
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16

NO
YES
NO
YES
YES
YES
NO
YES
YES
YES
YES
YES
YES
YES
NO
YES
YES
YES
YES'''