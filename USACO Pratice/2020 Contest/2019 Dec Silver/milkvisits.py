"""
ID: yuhao201
LANG: PYTHON3
TASK: meetings
"""
problem_name = 'milkvisits'


def solution(row_input):
    n,m = row_input.pop(0)
    types = '#'+row_input.pop(0)
    Hset,Gset = {},{}
    for i in range(n):
        x, y = map(int,row_input[i])
        if types[x]=='H' and types[y]==types[x]:
            if x in Hset:
                Hset[x] |= set(y)
                Hset[y] |= set(x)
            else:
                Hset[x] = set(y)
                Hset[y] = set(x)

        if types[x]=='G' and types[y]==types[x]:
            if x in Gset:
                Gset[x] |= set(y)
                Gset[y] |= set(x)
            else:
                Gset[x] = set(y)
                Gset[y] = set(x)
    ans = ''
    for i in range(n,n+m):
        x,y,c = row_input[i]
        if c=='H' and y in Hset[x]:
            ans+='1'
        elif c=='G' and y in Gset[x]:
            ans+='1'
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