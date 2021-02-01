for _ in range(int(input())):
    n,m = map(int,input().split())
    s = list(map(int,input().replace('+','1,').replace('-','-1,').split(',')[:-1]))
    interval = [list(map(int,input().split())) for _ in range(m)]
    prefix_min,prefix_max,surffix_min,surffix_max = [0],[0],[0],[0]
    value = [0]
    for i in range(n):
        value.append(s[i]+value[-1])
        prefix_min.append(min(value[-1],prefix_min[-1]))
        prefix_max.append(max(value[-1],prefix_max[-1]))
        surffix_min.append(min(0,s[n-i-1]+surffix_min[-1]))
        surffix_max.append(max(0,s[n-i-1]+surffix_max[-1]))
        
    # print(surffix_min,surffix_max,prefix_min,prefix_max,value)
    
    surffix_max = surffix_max[::-1]
    surffix_min = surffix_min[::-1]
    for l,r in interval:
        l-=1
        l1 = prefix_min[l]
        r1 = prefix_max[l]
        l2 = surffix_min[r]+value[l]
        r2 = surffix_max[r]+value[l]
        print(max(r1, r2) - min(l1, l2) + 1)
'''
2
4 10
+-++
1 1
1 2
2 2
1 3
2 3
3 3
1 4
2 4
3 4
4 4
8 4
-+--+--+
1 8
2 8
2 5
1 1
'''