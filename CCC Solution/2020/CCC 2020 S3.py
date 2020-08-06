def Counter(s):
    ini = {'q': 0, 'w': 0, 'e': 0, 'r': 0, 't': 0, 'y': 0, 'u': 0, 'i': 0, 'o': 0, 'p': 0, 'a': 0, 's': 0, 'd': 0,'f': 0, 'g': 0, 'h': 0, 'j': 0, 'k': 0, 'l': 0, 'z': 0, 'x': 0, 'c': 0, 'v': 0, 'b': 0, 'n': 0, 'm': 0, '#': 0}
    for i in s: ini[i]+=1
    return ini

n = input()
h = '#'+input()
count=0
std = Counter(n)
c = set()
curWord = h[:len(n)]
curCount = Counter(curWord)
nl,hl = len(n),len(h)
for i in range(1,hl-nl+1):
    curCount[h[i-1]]-=1
    curCount[h[i+nl-1]]+=1
    curWord = curWord[1:]+h[i+nl-1]
    if h[i+nl-1] in n and not curWord in c and curCount==std: 
        count+=1
        c.add(curWord)
print(count)

# # 7分
# from typing import Counter
# n = input()
# h = input()
# count=0
# std = Counter(n)
# c = set()
# nl,hl = len(n),len(h)
# for i in range(hl-nl+1):
#     curWord = h[i:i+nl]
#     if Counter(curWord)==std and not curWord in c: 
#         count+=1
#         c.add(curWord)
# print(count)