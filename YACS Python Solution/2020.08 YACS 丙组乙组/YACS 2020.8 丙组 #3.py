# YACS 2020.8 丙组 #3
'''
样例数据
输入:
5
A 1 1 1
B 20 20 20
C 40 40 40
D 80 80 80
E 120 120 120
输出:
Winning list:
C
D
E
输入:
3
Ai 1 100 20
Be 101 101 21
Ct 40 80 121
输出:
Winning list:
Ct
输入:
2
Old 1 100 121
Egg 101 101 21
输出:
There is no winner.
'''
def stdinput():
    '''simple input function'''
    def strint(x):
        try: return int(x)
        except: return x
    return list(map(strint,input().strip().split()))

n = int(input())
goods = []
ma,mb,mc = 0,0,0
for i in range(n):
    s, a, b, c = stdinput()
    ma,mb,mc = max(a,ma),max(mb,b),max(mc,c)
    goods.append([s, a, b, c]) # 

def pattern(sm):
    return sm[1]>ma-100 and sm[2]>mb-100 and sm[3]>mc-100

ans = list(filter(pattern,goods))

if len(ans)==0: print('There is no winner.')
else:
    print('Winning list:')
    for i in ans:
        print(i[0])