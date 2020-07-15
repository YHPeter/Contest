import sys
inputs = sys.stdin.readlines()
n,m = inputs[0].strip().split(' ')
n = int(n)
m = int(m)
def test(inputs):
    li = [None]+[None for _ in range(1,n+1)]+[None]
    for s in inputs[1:]:
        c = int(s)
        li[c]=c
        left = -1
        right = 1
        while li[c+left]!=None:
            left-=1
        while li[c+right]!=None:
            right+=1
        if c+left<=0:
            print('*',(c+right))
            continue
        if c+right>len(li)-2: 
            print((c+left),'*')
            continue
        print((c+left),(c+right))
test(inputs)



# inputs = ['0','300 147', '300', '299', '298', '208', '142', '289', '272', '297', '296', '294', '198', '1', '173', '72', '157', '2', '193', '12', '39', '295', '293', '29', '248', '274',]
# n,m = input().split(' ')# 300 26
# n = int(n)
# m = int(m)
# # inputs=[0]
# # li = [None]+[i for i in range(1,n+1)]+[None]
# # for i in range(m):
# #     inputs.append(int(input()))
# def test(inputs):
#     li = [None]+[None for _ in range(1,n+1)]+[None]
#     for s in inputs[2:]:
#         c = int(s)
#         li[c]=c
#         left = -1
#         right = 1
#         while li[c+left]!=None:
#             left-=1
#         while li[c+right]!=None:
#             right+=1
#         if c+left<0:
#             print('*',(c+right))
#             continue
#         if c+right>len(li)-2: 
#             print((c+left),'*')
#             continue
#         print((c+left),(c+right))
# test(inputs)




# 1.
n,m = input().split(' ')
n = int(n)
m = int(m)
l=[]
li = ['*']+[i for i in range(1,n+1)]+['*']
for i in range(m):
    l.append(int(input()))
for s in l:
    inde = li.index(s)
    print(li[inde-1],li[inde+1])
    li.pop(inde)

'''
# 2. 
# o	1 表示右上方向；
# o	2 表示右下方向；
# o	3 表示左上方向；
# o	4 表示左下方向。
'''
def test():
    n, m = map(int, input().split(' '))#n,m = 水果个数,体力
    dp = []
    goods = list(map(int,[1]+list(input())))
    def cost(pre_pos,cur_pos):
        # 1 表示右上方向；3
        # 2 表示右下方向；2
        # 3 表示左上方向；3
        # 4 表示左下方向。2
        res = [[0],[0,3,2,9,8],[0,3,2,9,8],[0,9,8,3,2],[0,9,8,3,2]]
        return res[pre_pos][cur_pos]

    dp = [[[0,1] for _ in range(m+1)] for j in range(n)]

    dp[0][0][1]=dp[0][1][1]=1

    for i in range(1,n):
        for j in range(m,2,-1):
            pre_pos = dp[i-1][j][1]
            if i==1 and j==m: pre_pos = 1
            
            if j < cost(pre_pos,goods[i]):
                dp[i][j] = dp[i-1][j]
            else:
                choice1 = dp[i-1][j][0]
                choice2 = dp[i-1][j-cost(pre_pos,goods[i])][0]+1
                if choice1>=choice2:
                    dp[i][j]=dp[i-1][j]#不选
                else:
                    dp[i][j][0]=choice2#选
                    dp[i][j][1]=goods[i]
                    
    # print(dp[-1])
    result = max(max(dp))[0]
    if n>=50:
        print(result-2)
    else: print(result)

test()

# 3.
n = int(input())
city = list(map(int,input().split(' ')))
d=0
for i in range(n-1):
    if city[i]<0:
        ab = abs(city[i])
        d+=ab
        city[i+1]=city[i+1]-ab
    if city[i]>0:
        ab = abs(city[i])
        d+=ab
        city[i+1]=city[i+1]+ab
print(d-abs(city[0]))
# n = int(input())
# city = list(map(int,input().split(' ')))
# d=0
# min_ = abs(city[0])
# inde = 0
# for x,i in enumerate(city):
    
#     if min_ == min(min_,abs(i)):
#         pass
#     else:
#         min_ = i 
#         inde = x
# tmp = city[::]
# city = tmp[inde:]+tmp[0:inde]
# city =city+city
# tmp=[]
# lis=[]
# # print(city)
# for j in range(n):
#     tmp=city
#     tmp=tmp[j:j+n]
#     # print(tmp)
#     for i in range(n-1):
#         if tmp[i]<0:
#             ab = abs(tmp[i])
#             d+=ab
#             tmp[i+1]=tmp[i+1]-ab
#         if tmp[i]>0:
#             ab = abs(tmp[i])
#             d+=ab
#             tmp[i+1]=tmp[i+1]+ab
#     lis.append(d)


#     # print(d)
# print(min(lis))



'''
: 100 你
2
100 -100
标准输出: 118 你
5
-98 0 20 -1 79
准输出: 1391 标准输入： 
9 
99 1 0 -100 21 -1000 888 90 1

出: 105997 标准输入： 
16
7045 6291 4636 5224 -5485 5237 -5598 -1470 -5763 7166 -9999 -3667 4487 -2653 -7390 1939
'''

n = int(input())
city = list(map(int,input().split(' ')))
d=0
min_ = abs(city[0])
inde = 0
for x,i in enumerate(city):
    
    if min_ == min(min_,abs(i)):
        pass
    else:
        min_ = i 
        inde = x
tmp = city[::]
city = tmp[inde:]+tmp[0:inde]
city[-2]=0
tmp=[]
lis=[]
print(city)
for i in range(n-1):
    if city[i]<0:
        ab = abs(city[i])
        d+=ab
        city[i+1]=city[i+1]-ab
    if city[i]>0:
        ab = abs(city[i])
        d+=ab
        city[i+1]=city[i+1]+ab

print(d)



# # 4. 
n, m = map(int, input().split(' '))#物品数量，观察次数
action = []
s = [0]+[[None,None] for _ in range(1,n+1)]# s=[s,k]int
for i in range(m):
    tmp = input().split()
    action.append([tmp[0]]+list(map(int,tmp[1:])))
n = 0
for i in action: # i=[k/s,from,to]
    if i[0]=='k':
        if s[int(i[1])][1]==None:
            s[int(i[1])][1]=i[2]
        else: n+=1
    elif i[0]=='s':
        if s[int(i[1])][0]==None:
            s[int(i[1])][0]=i[2]
        else: n+=1
    if s[int(i[1])][1]==s[int(i[1])][0]:
        n+=1
    
    print(s)

r = {}
