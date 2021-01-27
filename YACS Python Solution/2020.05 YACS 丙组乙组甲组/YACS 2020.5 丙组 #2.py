# YACS 2020.5 丙组 #2
gpa = list(input())
total = 0.0
flag = False
num = 0

for i in gpa:
    if i == 'A': total,num = total+4,num+1
    elif i == 'B': total,num = total+3,num+1
    elif i == 'C': total,num = total+2,num+1
    elif i == 'D': total,num = total+1,num+1
    elif i == '-': total -= 0.3
    elif i == '+': total += 0.3
print(("%.2f" % (total/num)))