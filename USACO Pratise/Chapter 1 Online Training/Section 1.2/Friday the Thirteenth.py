"""
ID: yuhao201
LANG: PYTHON3
TASK: friday
"""
import calendar
def solution(n):
    statr = 1900
    ans = [0,0,0,0,0,0,0]
    for year in range(1900,1900+n):
        for month in range(1,13):
            week = calendar.weekday(year,month,13)
            ans[week]+=1
    ans = ans[5:7]+ans[:5]
    return ans
if __name__ == "__main__":
    fin = open ('friday.in', 'r')
    fout = open ('friday.out', 'w')
    ans = solution(int(str(fin.readline())))
    fout.write(' '.join(map(str,ans)))
    fout.write('\n')
    fout.close()