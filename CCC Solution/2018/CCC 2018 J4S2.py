
'''
2018
Q2
Sample Input 2
3
4 3 1
6 5 2
9 7 3
Output for Sample Input 2
1 2 3
3 5 7
4 6 9

4
4 8 12 16
3 7 11 15
2 6 10 14
1 5 9 13
'''
n = int(input())
raw = []
mini = 99999999
for i in range(n):
    raw.append(input().split())
    mini = min(mini,min(map(int,raw[i])))

def rotate(l):
    ans = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            ans[i][j] = l[j][n-i-1]
    return ans

def isright(l):
    if l[0][0]==str(mini): return True
    else: return False

def out(l):
    for i in l:
        print(' '.join(i))

def main():
    if isright(raw): return raw
    x = rotate(raw)
    if isright(x): return x
    x = rotate(x)
    if isright(x): return x
    return rotate(x)
out(main())