n,m = map(int, input().split())

column = n+m-1

if column%2 == 0:
    print(sum(range(1,column))+n)
else:
    print(sum(range(1,column))+column-n+1)