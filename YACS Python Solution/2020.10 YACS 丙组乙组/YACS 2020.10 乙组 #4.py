'''
标准输出: 1991
6 5
147 1969 933 10095 1557

标准输出: 4843
5 6
147 1969 933 10095 1557 10308

标准输出: 7913
7 7
199 10104 11847 1892 2750 7600 9804

'''
# 二分搜索
def check(minh):
    value,j = 0,0
    for _ in range(n):
        while j<m and value<minh:
            value+=a[j]
            j+=1
        if value<minh: return False
        value//=2
    return True
    
n,m = map(int, input().split())
a = list(map(int, input().split()))

ll,rr = 0,sum(a)//2+1
while rr>ll+1:
    mid = (rr+ll)//2
    if check(mid): ll = mid
    else: rr = mid
print(ll)