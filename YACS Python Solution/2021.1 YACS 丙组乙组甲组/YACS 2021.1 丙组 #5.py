n,k = map(int, input().split())
sequence = list(map(int, input().split()))
previous = [x for x in range(1, n+1)]
for _ in range(k):
    now = [previous[x-1] for x in sequence]
    previous = now
print(' '.join(map(str,now)))