"""
ID: yuhao201
LANG: PYTHON3
TASK: beads
"""

def solution(n,s):
    l = 2n
    s = s+s
    dp = [0 for _ in range(l)]
    print(n,s)

    return 0
if __name__ == "__main__":
    fin = open ('beads.in', 'r')
    fout = open ('beads.out', 'w')
    ans = solution(int(fin.readline()),fin.readline())
    # fout.write(' '.join(map(str,ans)))
    fout.write('\n')
    fout.close()