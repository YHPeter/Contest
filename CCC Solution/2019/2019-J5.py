'''Sample Input
AA AB
AB BB
B AA
4 AB AAAB
Possible Output for Sample Input
2 1 BB
3 1 AAB
3 3 AAAA
1 3 AAAB
Explanation of Output for Sample Input
This is the example outlined in the problem description. Note that the following is another possible
valid substitution sequence:
2 1 BB
3 2 BAA
1 2 BAB
3 1 AAAB
Specifically, showing the substitutions in bold, we get
AB → BB → BAA → BAB → AAAB.

AA AB
AB BB
B AA
1 AB AAA
'''

rules = {}
rulein = {}
for i in range(1,4):
    a,b = input().split()
    rules[a] = b
    rulein[a] = i
porul = [len(x) for x in rules.keys()]
n, start, end = input().split()
n = int(n)

def possbile(x):
    for rule in rules.keys():
        into = rules[rule]
        i = len(rule)
        for d in range(len(x)):
            if x[d:d+i]==rule:
                yield d,rule,x[:d]+into+x[d+i:]
ansli = []
def find(n,start):
    if start==end: return True
    if n==0: return False
    n-=1
    for d,r,x in possbile(start):
        if find(n,x):
            ansli.append([d,r,x])
            return True
    
find(n,start)
for a,b,c in ansli[::-1]:
    print(rulein[b],a+1,c)