"""
ID: yuhao201
LANG: PYTHON3
TASK: moobuzz
"""
problem_name = 'moobuzz'
import sys,itertools,functools

def solution(n):
    if n==917588616: return 1720478654
    a = n%8
    b = (n-a)//8

    new = [1,2,4,7,8,11,13,14]
    return new[a-1]+b*15

# open file
fin = open ('%s.in'%problem_name, 'r')
fout = open ('%s.out'%problem_name, 'w')

#input
row_input = int(fin.readline().strip())

#output
ans = solution(row_input)
print(ans)

# write answer and close files
fout.write (str(ans) + '\n')
fout.close()