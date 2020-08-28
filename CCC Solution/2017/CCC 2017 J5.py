def number_of_height(height, list_of_board_lengths):
    lengths = list_of_board_lengths[:]
    a = max(1, height - 2000)
    b = height - a
    number_boards = 0
    while a <= height/2:
        if a == b:
            boards = lengths[a] // 2
            lengths[a] -= boards * 2
            number_boards += boards
        else:
            boards = min(lengths[a], lengths[b])
            lengths[a] -= boards
            lengths[b] -= boards
            number_boards += boards
        a += 1
        b -= 1
    return number_boards

n = int(input())
l = list(map(int,input().split()))
heights = [0]*2001

for i in l:
    heights[i] += 1

max_boards = 0
max_heights = 0

for counter in range(2, 4001):
    x = number_of_height(counter, heights)
    if x > max_boards: max_boards,max_heights = x,0
    elif x == max_boards: max_heights += 1

print(max_boards, max_heights+1)
