for _ in range(int(input())):
    q,d = map(int,input().split())
    li = list(map(int,input().split()))

    for x in li:
        
        while True:
            if x<10 and x!=d: 
                print('NO')
                break
            x-=d
            if x%10 == 0:
                print('YES')
                break
            