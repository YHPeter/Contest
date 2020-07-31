"""
ID: yuhao201
LANG: PYTHON3
TASK: ride
"""
def solution(x,y):
    xx,yy = 1,1
    for i in range(len(x)):
        xx = xx*(ord(x[i])-64)%47
    for i in range(len(y)):
        yy = yy*(ord(y[i])-64)%47
    if xx==yy: return 'GO'
    else: return 'STAY'
if __name__ == "__main__":
    fin = open ('ride.in', 'r')
    fout = open ('ride.out', 'w')
    x,y = fin.readline().strip(),fin.readline().strip()
    fout.write (str(solution(x,y))+'\n')
    fout.close()
