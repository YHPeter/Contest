a,b,c,d,x = int(input()),int(input()),int(input()),int(input()),int(input())
ar,br= x%(a+b),x%(c+d)
aa,bb=(x-ar)//(a+b)*(a-b),(x-br)//(c+d)*(c-d)
if ar>a: aa+=2*a-ar
else: aa+=ar
if br>c: bb+=2*c-br
else: bb+=br
if aa==bb: print('Tied')
elif aa<bb: print('Byron')
elif aa>bb: print('Nikky')