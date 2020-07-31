"""
ID: yuhao201
LANG: PYTHON3
TASK: gymnastics
"""
problem_name = 'gymnastics'

def solution(cows):
    k,n = cows.pop(0)
    ans = 0
    new_cows = [[0]*n for _ in range(k)]
    for i in range(k):
        for j in range(n):
            new_cows[i][cows[i][j]-1] = j+1
    cows = new_cows   
    print(new_cows)
    for i in range(n):
        for j in range(i+1,n):
            counta,countb = 0,0
            for h in range(k):
                if cows[h][j]>=cows[h][i]:
                    counta+=1
                else:
                    countb+=1
            if (counta==0 and countb!=0) or (countb==0 and counta!=0):
                ans+=1
    return ans

# open file
fin = open ('%s.in'%problem_name, 'r')
fout = open ('%s.out'%problem_name, 'w')

#input
row_input = fin.readlines()
pro_input = [list(map(int,i.strip().split(' '))) for i in row_input]

#output
ans = solution(pro_input)
print(ans)

# write answer and close files
fout.write (str(ans) + '\n')
fout.close()