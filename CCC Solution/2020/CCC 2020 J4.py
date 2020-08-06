t,s = input(),input()
s = s+s
import sys
l = len(s)//2
for i in range(l):
    if s[i:i+l] in t:
        print('yes')
        sys.exit()
print('no')