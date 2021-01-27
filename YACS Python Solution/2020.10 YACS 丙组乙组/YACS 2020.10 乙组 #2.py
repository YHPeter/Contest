def merge_sort(nums): # https://www.acwing.com/solution/acwing/content/4880/
    if len(nums) <= 1:
        return 0
    mid = len(nums) // 2
    L = nums[:mid]
    R = nums[mid:]
    ans = merge_sort(L) + merge_sort(R)

    # 归并的过程
    i = j = k = 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            nums[k] = L[i]
            k += 1
            i += 1
        else:
            nums[k] = R[j]
            ans += len(L) - i
            k += 1
            j += 1
    while i < len(L):
        nums[k] = L[i]
        k += 1
        i += 1
    while j < len(R):
        nums[k] = R[j]
        k += 1
        j += 1
    return ans

n,k = map(int, input().split())
nums = list(map(int, input().split())) 
a = merge_sort(nums)
d = merge_sort(nums*2)
print(a*k+k*(k-1)*d//2)
'''
4 30
7 2 5 4
'''
# import sys
# print(sys.stdin.readlines())