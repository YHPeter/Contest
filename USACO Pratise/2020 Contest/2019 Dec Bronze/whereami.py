"""
ID: yuhao201
LANG: PYTHON3
TASK: whereami
"""
problem_name = 'whereami'

def solution(pro_input):
    n = int(pro_input.pop(0)[0])
    mails = pro_input[0][0]
    ans = 0
    while 1:
        ans+=1
        prelist = set()
        pre_len = 0
        flag = True
        for i in range(n-ans+1):
            x = mails[i:i+ans:]
            if x in prelist: 
                flag = False
                break
            else: prelist.add(x)
        print(prelist)
        if flag: return ans

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