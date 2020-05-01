# 乙组  2020年3月
# 1.
import sys
n = int(input())
inputs = sys.stdin.readlines()
website = []
be_act = ''
current = -1
res = []
for info in inputs[:n]:
    info = info.strip().split(' ')
    act = info[0]
    try:
        current_web = info[1]
    except: pass
    if act=='v':
        current += 1
        website.insert(current,current_web)
        print(website[current])
        res.append(website[current])
        be_act = 'v'
        pass
    elif act=='b':
        current -= 1
        if current == -1:
            res.append('?')
            print('?')
            be_act = 'b'
        else:
            print(website[current])
            res.append(website[current])
            be_act = 'b'
        pass
    elif act=='f':
        current += 1
        if current > len(website)-1 or be_act == 'v':
            res.append('?')
            print('?')
            current -= 1
        else:
            print(website[current])
            res.append(website[current])
        pass
    else: pass
    
# 2.

n = int(input())

def max_contiguous_subarray(A):
    max_overall = float('-inf')
    all_start_pos = None
    all_end_pos = None
    max_ending_here = float('-inf')
    start_pos = None
    end_pos = None

    for pos, a in enumerate(A):
        if a > max_ending_here + a:
            max_ending_here = a
            start_pos = pos
            end_pos = pos
        else:
            max_ending_here = max_ending_here + a
            end_pos = pos
        if max_ending_here > max_overall:
            max_overall = max_ending_here
            all_start_pos = start_pos
            all_end_pos = end_pos
    return max_overall, all_start_pos, all_end_pos

    dp = [0 for _ in range(len(A+1))]
    dp[0] = A[0]
    for pos, a in enumerate(A):
        if a>=0:
            dp[pos] = dp[pos-1]+a
        elif a<0:
            dp[pos] = dp[pos-1]
    return dp[len(A)]


def max_contiguous_trapezoid(B, U):
    min_b_width = 3
    b_start_pos = None
    b_end_pos = None
    u_start_pos = None
    u_end_pos = None
    max_area = float('-inf')
    for i in range(len(B)-min_b_width+1):
        for j in range(i+min_b_width, len(B)+1):
            max_sub_b = max_contiguous_subarray(B[i:j])
            max_sub_u = max_contiguous_subarray(U[i+max_sub_b[1]+1:i+max_sub_b[2]])
            if max_sub_b[0] + max_sub_u[0] > max_area:
                max_area = max_sub_b[0] + max_sub_u[0]
                b_start_pos = max_sub_b[1]
                b_end_pos = max_sub_b[2]
                u_start_pos = b_start_pos + max_sub_u[1] + 1
                u_end_pos = b_start_pos + max_sub_u[2] + 1
    return max_area, b_start_pos, b_end_pos, u_start_pos, u_end_pos

max_contiguous_trapezoid(input().split(' '), input().split(' '))





# 3

# n = list(int(input()))
# n = list(314159265358979323846)

# dp = []
def timeRecord(func):
    import time
    inside()
    def inside():
        start = time.time()
        func()
        print(time.time()-start)

#凸性区域
# l = int(input())
# r1 = str(input()).split(' ')
# r2 = str(input()).split(' ')
# l=10
# r1 = ("8 9 -6 -8 3 -1 4 -3 10 -7").split(' ')
# r2 = ("-4 -10 -5 1 5 6 -2 7 -9 2").split(' ')
# dp = [[0 for _ in range(l+1)] for _ in range(3)] #i,j 为每层又边界
# a = r1+r2
# res = 100000000000
import numpy as np

n=10
r1 = np.array(("8 9 -6 -8 3 -1 4 -3 10 -7").split(' '))
r2 = np.array(("-4 -10 -5 1 5 6 -2 7 -9 2").split(' '))
dp = np.array([[0 for _ in range(n+1)] for _ in range(3)])
print(dp)
for i in range(n):
    for j in range(1,n):
        dp[i][j] = max(int(r1[i]),int(r1[i]) + int(dp[i-1][j-1]))
print(dp)
