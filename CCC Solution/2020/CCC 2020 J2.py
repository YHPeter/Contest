p,a,r = int(input()),int(input()),int(input())
import math
if r==1: print(p//a)
else: print(int(math.log((1-(p-p*r)/a),r)))