n = int(input())
s = list(map(int,input().split()))

def findmax(n,s):
    cur,max_ = s[0],s[0]
    for i in range(n):
        cur = max(0,cur)+s[i]
        max_ = max(max_,cur)
    return max_

def findmin(n,s):
    cur,min_ = s[0],s[0]
    for i in range(n):
        cur = min(0,cur)+s[i]
        min_ = min(min_,cur)
    return sum(s)-min_
    
print(max(findmax(n,s),findmin(n,s)))



'''
5
3 1 -4 1 5

10 

30
-59 552 974 -313 698 793 440 340 -761 281 160 -50 64 876 -841 -336 -951 592 788 326 704 154 -318 643 -280 -329 669 -208 530 598

7864 
'''