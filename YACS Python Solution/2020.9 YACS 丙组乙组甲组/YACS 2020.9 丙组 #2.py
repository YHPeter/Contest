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