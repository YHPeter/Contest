n,m,s = map(int, input().split()) # n名运动员，m体力，s总圈数, s<=m

value = [m]*n
result = []

def change(cur, s_remain, time_taken):
    if s_remain==0:
        result.append(time_taken)
        return
    max_v = max(cur)
    for speed in range(1,s+1):
        if max_v<speed**2 or s_remain - speed<0: break
        new = [x-speed for x in cur]
        for j in range(n):
            if new[j] == max_v-speed:
                new[j] = new[j]+speed-speed**2
                break
        change(new, s_remain - speed, time_taken+1)

change(value, s, 0)
print(min(result))