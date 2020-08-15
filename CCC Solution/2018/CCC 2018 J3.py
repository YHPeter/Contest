# Q3
list1=list(str(input()).split())
d1 = int(list1[0])
d2 = int(list1[1])
d3 = int(list1[2])
d4 = int(list1[3])
d12 = d1+d2
d123 = d1+d2+d3
d1234 = d1+d2+d3+d4
d23 = d2+d3
d34 = d3+d4
d234 = d2+d3+d4
print(0,d1,d12,d123,d1234)
print(d1,0,d2,d23,d234)
print(d12,d2,0,d3,d34)
print(d123,d23,d3,0,d4)
print(d1234,d234,d34,d4,0)