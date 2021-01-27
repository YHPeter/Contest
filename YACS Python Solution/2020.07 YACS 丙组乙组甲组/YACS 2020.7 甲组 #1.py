# YACS 2020.7 甲组 #1
# sample answer from https://iai.sh.cn/contribution/214
'''
输入:
10 16 3

输出:
4
说明:
分别为
dxl
hph
lxd
xpx

输入:
10 0 2
输出:
0
'''

def S_search(dep,state):
    if dep==0: num[state]+=1
    else:
        for i in range(1,27):
            S_search(dep - 1,((state * 33) ^ i) & mod)
    
def E_search(dep,state):
    global ans
    if dep==0: ans += num[state]
    else:
        for i in range(1,27):
            E_search(dep - 1,((state ^ i) * inv_33) & mod)

m,k,n = list(map(int,input().split(' ')))
mod = (1<<m)-1
ans,inv_33 = 0,1
num = [0]*134217728
while ((inv_33 * 33) & mod) != 1:
    inv_33 = (inv_33 * 33) & mod
S_search(n // 2,0)
E_search(n - (n // 2),k)
print(ans)