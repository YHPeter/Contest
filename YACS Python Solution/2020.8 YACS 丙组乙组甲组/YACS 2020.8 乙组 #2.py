# YACS 2020.8 乙组 #2
'''
输出: 80
输入：
3
200 120
50 40
20 10

输出: 369
输入：
15
64 30
55 52
6 5
2 1
62 22
6 5
596 553
3 2
46 19
6 5
2 1
6 5
2 1
2 1
40 33

输出: 202
输入：
16
2 1
2 1
2 1
2 1
2 1
10 8
8 7
520 154
6 5
6 5
2 1
5 4
6 5
559 302
6 5
2 1
'''
def stdinput():
    '''simple input function'''
    def strint(x):
        try: return int(x)
        except: return x
    return list(map(strint,input().strip().split()))
choose = []
am,bm = 0,0
for i in range(int(input())):
    a,b= stdinput()
    if not [a,b] in choose:
        choose.append([a,b])
        am,bm = max(a,am),max(b,bm)


dp = [[0]*bm for _ in range(am)]

for i in range(1,am+1):
    for j in range(1,bm+1):
        for a,b in choose:

            dp[i][j] = max(dp[i][j],)


print(dp[-1][-1])
# ans = 1

# def f(inside,choose,ans):
#     if len(choose)==0: return ans
#     if len(choose)==1:
#         ans+=(inside//choose[0][0])
#         return ans
#     for cur_outside,cur_inside in choose:
#         if inside<cur_outside: continue

#         ans+=(inside//cur_outside)
#         for i in range(inside//cur_outside):
#             ans = max(ans,f(cur_inside,choose,ans))
#         inside %= cur_outside
        
# print(choose)
# inside_ = sorted(choose,key = (lambda x: x[1]))
# ind = inside_[-1][1]
# inside_.pop()
# ans = f(ind,inside_)
# print(ans)