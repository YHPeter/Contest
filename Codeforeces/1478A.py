for _ in range(int(input())):
    n = int(input())
    li = list(map(int,input().split()))
    ans = 1
    cur = li[0]
    tmp = 1
    for i in range(1,n):
        if li[i] == cur: 
            tmp+=1
        else:
            ans = max(ans,tmp)
            cur = li[i]
            tmp = 1
    ans = max(ans,tmp)
    print(ans)


1
5 7
10000007 6999993 369963 369963 36912963