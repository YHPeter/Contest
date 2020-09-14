'''
Line 1：输入数字并列表化
Line 2：得到镜像后的数字列表
Line 3：判断是否相等，输出答案

n = list(input())
ans = [[0,1,'x','x','x','x',9,'x',8,6][int(i)] for i in n[::-1]]
print('Strobogrammatic number') if ans==list(map(int,n)) else print('Not a strobogrammatic number')
'''
n = list(input())
nums = [0,1,'x','x','x','x',9,'x',8,6]
ans = []
for i in n[::-1]:
    ans.append(nums[int(i)])
    # print(ans)
if ans==list(map(int,n)):
    print('Strobogrammatic number')
else:
    print('Not a strobogrammatic number')