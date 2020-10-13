from typing import Counter

n = int(input())
b = list(map(int,input().split()))
numcount = Counter(b)
maxnuber = max(b) #number of hambergers 
count = [0]+[0]*maxnuber