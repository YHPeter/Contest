sum1,sum2=0,0
for i in range(3):
    sum1=(3-i)*int(input())+sum1
for i in range(3):
    sum2=(3-i)*int(input())+sum2
if sum1 == sum2:
    print("T")
elif sum1<sum2:
    print("B")
else:
    print("A")