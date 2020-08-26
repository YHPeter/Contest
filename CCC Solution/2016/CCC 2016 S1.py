a,b = input(),input()

from typing import Counter
a = Counter(a)
b = Counter(b)
n = b.get('*',0)
for i in a.keys():
    if a[i]>=b.get(i,0):
        n-=(a[i]-b.get(i,0))
    if n<0:
        print('N')
        exit()
print('A')