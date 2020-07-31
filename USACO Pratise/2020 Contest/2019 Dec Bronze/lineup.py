"""
ID: yuhao201
LANG: PYTHON3
TASK: lineup
"""
problem_name = 'lineup'
import sys,itertools,functools

def solution(pro_input):
    n = int(pro_input.pop(0)[0])
    all_choose = []
    for i in range(n):
        pro_input[i] = pro_input[i].strip().split(' must be milked beside ')

    cows = ['Bessie', 'Buttercup', 'Belinda', 'Beatrice', 'Bella', 'Blue', 'Betsy','Sue']

    for i in itertools.permutations(cows):
        tmp = list(i)
        count = 0
        for x,y in pro_input:
            ix,iy = tmp.index(x),tmp.index(y)
            if abs(ix-iy)==1:
                count+=1
        if count==n:
            all_choose.append(tmp)
    all_choose.sort()
    print(len(all_choose))
    ans = all_choose[0]
    # print(pro_input)
    return ans

# open file
fin = open ('%s.in'%problem_name, 'r')
fout = open ('%s.out'%problem_name, 'w')

#input
row_input = fin.readlines()

#output
ans = solution(row_input)
print(ans)

# write answer and close files
for i in ans:
    fout.write(i+'\n')
fout.close()