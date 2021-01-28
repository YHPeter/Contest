def solve():
    n = int(input())
    x = n//2020
    n %= 2020
    return True if n<=x else False

for _ in range(int(input())):
    print('YES') if solve() else print('NO')