'''
3
1 1 1
2 2 2
3 3 3
'''
n = int(input())
grid = [list(map(int,input().split())) for i in range(n)]

total = sum([sum(x) for x in grid])
print(total)