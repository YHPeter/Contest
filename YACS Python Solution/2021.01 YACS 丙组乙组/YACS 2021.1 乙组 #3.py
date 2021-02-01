n,m,s = map(int, input().split()) # n名运动员，m体力，s总圈数, s<=m
import math
time = 0
for i in range(n):
    max_speed = math.floor(m**0.5)
    s -= max_speed
    m -= max_speed
    time+=1
    if s<=0: break
print(time)