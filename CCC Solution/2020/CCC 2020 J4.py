import sys
base = input()
test = input()

def cyc (string):
    output = []
    for i in range(len(string)):
        test = str(string)
        temp = test[i:] + test[0:i]
        output.append(temp)
    return(output)
for i in (cyc(test)):
    if i in base:
        print('yes')
        sys.exit()
print('no')