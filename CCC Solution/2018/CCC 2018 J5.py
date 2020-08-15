from collections import deque

n = int(input())
points = [[]]
for i in range(n):
    points.append(list(map(int,input().split())))
visited,depth = [True,True]+[False]*(n-1),[1,1]+[0]*n
ans = 100
q = deque()
q.append(1)
while q:
    cur = q.popleft()
    for node in points[cur]:
        if node == 0:
            ans = min(ans,depth[cur])
        else:
            if not visited[node]:
                q.append(node)
                depth[node] = depth[cur]+1
                visited[node] = True

if not False in visited: print('Y\n%d'%ans)
else: print('N\n%d'%ans)

'''Sample Input 1
3
2 2 3
0
0
Output for Sample Input 1
Y
2
Explanation of Output for Sample Input 1
Since we start on page 1, and can reach both page 2 and page 3, all pages are reachable. The only
paths in the book are 1 → 2 and 1 → 3, each of which is 2 pages in length.
Sample Input 2
3
2 2 3
0
1 1
Output for Sample Input 2
Y
2

Output: Y \n 6
100
6 93 84 54 46 7 20
7 53 73 60 51 33 63 80
4 24 46 93 47
2 34 52
5 92 7 9 94 90
1 76
6 48 34 91 79 18 11
7 47 34 63 70 54 48 49
7 86 48 41 85 42 84 50
5 32 65 8 27 1
4 49 34 68 11
7 89 52 93 5 20 96 86
1 34
2 55 51
7 97 60 1 41 27 42 65
4 83 73 63 80
8 43 86 13 96 1 69 90 31
1 83
8 72 29 70 57 54 2 36 53
3 18 91 66
3 84 41 75
6 65 54 95 71 63 13
6 25 2 89 16 76 17
4 13 14 47 68
1 25
4 13 18 84 71
1 16
6 39 9 29 31 19 10
3 98 20 100
3 85 22 72
4 31 54 7 92
6 24 18 100 8 23 85
1 88
1 14
7 96 4 64 22 43 74 78
1 23
1 100
6 83 32 73 52 65 80
4 92 18 55 44
5 38 18 4 64 11
1 4
2 77 5
5 50 88 35 94 33
3 63 74 79
2 19 4
7 12 76 79 52 74 3 69
1 69
2 29 84
4 3 17 23 45
6 3 7 31 69 32 38
3 33 96 26
7 98 83 77 70 74 25 94
5 71 36 38 37 92
1 20
7 86 7 52 76 20 23 21
1 82
2 86 7
3 39 51 77
2 46 45
4 92 30 50 84
0
3 6 87 93
8 55 76 17 65 89 56 44 61
3 76 16 68
6 95 85 78 11 20 76
4 32 52 90 80
5 43 51 3 26 89
4 19 50 1 94
4 62 57 43 51
2 94 85
8 10 23 20 30 25 29 5 94
8 2 52 42 12 3 90 99 95
7 5 41 48 60 49 45 50
8 53 28 83 74 14 35 33 85
1 31
1 60
7 13 49 40 46 72 86 83
1 1
5 46 81 67 11 64
5 55 42 23 52 28
8 69 4 87 25 80 53 93 14
1 14
6 36 77 82 91 58 24
4 100 41 39 62
7 52 19 65 38 59 92 23
5 62 40 90 94 33
1 21
6 71 15 40 37 28 13
1 45
1 38
8 44 62 54 69 20 58 29 36
5 20 97 5 31 60
8 72 59 25 40 6 64 73 41
1 59
1 75
2 10 4
8 100 93 74 24 96 82 27 91
5 41 46 92 1 71
4 56 82 47 79
5 46 27 44 2 83

'''