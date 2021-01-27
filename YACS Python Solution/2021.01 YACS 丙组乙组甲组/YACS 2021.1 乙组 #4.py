# test
# def isPalindrome(a):
#     a = list(str(a))
#     if a == a[::-1]: return 1
#     else: return 0
# sumnum = 0
# n = 0
# for i in range(1,5,2):
#     for j in range(10**i, 10**(i+1)):
#         if isPalindrome(j):
#             sumnum += j
#             n+=1
#             # if n==0: 
#             #     print(sumnum)
#             #     exit()
#             print(sumnum, n, j)
ans = 0
for i in range(1,int(input())+1):
    ans+=int(str(i)+str(i)[::-1])
print(ans)