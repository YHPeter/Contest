"""
ID: yuhao201
LANG: PYTHON3
TASK: meetings
"""
problem_name = 'milkvisits'

def find(p):
    global b
    if b[p]!=p: b[p] = find(b[p])
    return b[p]

def solution(row_input):
    n,m = map(int,row_input.pop(0))
    c = '#'+row_input.pop(0)[0] # 每个点对应的牛奶品种 str[node]
    global b
    b = [i for i in range(n+1)] # [0,1,2,3,4,5,6,7,8...] 初始化node的父节点
    ans = ''
    for i in range(0,n-1):
        x,y = map(int,row_input[i])
        if c[x] == c[y]: # 如果两个相连的node，牛一样
            b[find(x)] = find(y) # 
    
    for i in range(n-1,n+m-1):
        x,y,z = row_input[i]
        x,y,z = int(x),int(y),z
        if find(x) != find(y) or c[x] == z: ans+='1'
        else: ans+='0'
    return ans

# open file
fin = open ('%s.in'%problem_name, 'r')
fout = open ('%s.out'%problem_name, 'w')

#input
row_input = fin.readlines()
pro_input = [i.strip().split(' ') for i in row_input]

#output
ans = solution(pro_input)
print(ans)

# write answer and close files
fout.write (str(ans) + '\n')
fout.close()