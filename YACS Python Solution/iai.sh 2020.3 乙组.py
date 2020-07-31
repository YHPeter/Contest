# 乙组  2020年3月
# 1. my answer 30分
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

# 1. sample answer from https:#iai.sh.cn/contribution/25
import sys
inputs = sys.stdin.readlines()
n = int(inputs[0])
content = inputs[1:]
pages = []
current = -1
prekey = ''
for line in content:
    line = line.strip()
    if line[0] == 'v':
        current += 1
        pages = pages[:current]
        pages.append(line[2:])
        print(pages[current])
        prekey = 'v'
    elif line[0] == 'b':
        if current <= 0 :
            print('?')
        else:
            current -= 1
            print(pages[current])
            prekey = 'b'
    elif line[0] == 'f':
        if current == len(pages)-1 or prekey == 'v':
            print('?')
        else:
            current += 1
            print(pages[current])  
            prekey = 'f'

# 2. my teacher answer
# top =    [ 8,   9, -6, -8, 3, -1,  4, -3, 10, -7]
# bottom = [-4, -10, -5,  1, 5,  6, -2,  7, -9,  2]
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
n = input()
top = list(map(int,input().split(' ')))
bottom = list(map(int,input().split(' ')))
print(max_contiguous_trapezoid(bottom, top))

# 3. sample answer from https:#iai.sh.cn/contribution/6
ans = 0
num = [0]*300100
def cmp(a,b):
    if a[0] < b[0]: return 1
    elif a[0] == b[0] and a[1] < b[1]: return 1
    else: return 0
q = []
n = int(input())
for i in range(n):
    q.append(list(map(int,input().strip().split(' '))))
q.sort()
for i in range(n):
    if num[q[i][1]] > 0: num[q[i][1]]-=1
    else: ans+=1
    num[q[i][1] - 1]+=1
print(ans)

# 4. sample answer from https://iai.sh.cn/contribution/9

dp = [0,1000000000,1000000000]+[0]*100002
def cal(l,r):
    point = 1
    dis = s[l + 1] - s[l]

    for i in range(l,r+1):
        if s[i] != s[l]: point = 2

    if point == 2:
        for i in range(l,r):
            if (s[i + 1] - s[i] != dis) or (abs(dis) > 1): point = 4

    if point == 4:
        for i in range(l+2,r+1):
            if s[i] != s[i - 2]: point = 5

    if point == 5:
        for i in range(l,r):
            if s[i + 1] - s[i] != dis: point = 10
    return point

s = [0]+list(map(int,list(input())))+[-1]

for r in range(3,len(s)+2):
    if s[r]==-1: break
    print(max(1,r - 5),max(0,r - 2))
    for l in range(max(1,r - 5),max(0,r - 2)+1):
        
        if dp[r] == 0:
            dp[r] = dp[l - 1] + cal(l,r)
        else:
            dp[r] = min(dp[r],dp[l - 1] + cal(l,r))

print(dp[len(s)-2])