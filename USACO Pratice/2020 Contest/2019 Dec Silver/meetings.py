"""
ID: yuhao201
LANG: PYTHON3
TASK: meetings
"""
problem_name = 'meetings'
from collections import defaultdict


def list_duplicates(seq):
    tally = defaultdict(list)
    for i,item in enumerate(seq):
        tally[item].append(i)
    return (locs for key,locs in tally.items() if len(locs)>1 and key!=1)


def solution(cows):
    n,l = cows.pop(0)
    tw = 0
    ans = 0
    cow_places = [0]*n
    cow_speed = [0]*n
    cow_weight = [0]*n
    for i in range(n):
        cow_weight[i],cow_places[i],cow_speed[i] = cows[i]
        tw+=cow_weight[i]
    twi = set()
    sum_twi = 0
    time = 0
    while 1:
        tally = defaultdict(list)
        time+=0.5
        for i in range(n):
            tally[item].append(i)
            if not i in twi:
                cow_places[i] += cow_speed[i]*0.5
                if (cow_places[i]>=l or cow_places[i]<=0):
                    twi.add(i)
                    cow_places[i] = 0
                    sum_twi+=cow_weight[i]
        if sum_twi>=(tw/2): break
        for a,b in list_duplicates(cow_places):
            cow_speed[a],cow_speed[b] = cow_speed[b],cow_speed[a]
            ans+=1
        print(time,ans)
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