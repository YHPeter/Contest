# YACS 2020.8 乙组 #3
'''
3 4
1 3
1 4
2 4
2 3
[1,3,2,4]

5 5
1 3
1 4
2 5
3 5
3 4

输出: 1 4 6 5 7 8 3 9 2 10 
输入:
10 18
1 10
2 10
2 9
3 9
3 8
4 8
4 7
5 7
5 6
1 9
1 4
6 1
1 7
7 1
9 2
6 7
1 4
7 1
'''
def stdinput():
    '''simple input function'''
    def strint(x):
        try: return int(x)
        except: return x
    return list(map(strint,input().strip().split()))

n,m = stdinput()
graph = {}
for i in range(m):
    