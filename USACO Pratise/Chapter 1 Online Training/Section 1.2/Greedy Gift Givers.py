"""
ID: yuhao201
LANG: PYTHON3
TASK: gift1
"""
def solution(input_list):
    ans = []
    for i in range(len(input_list)):
        input_list[i] = input_list[i].strip()
    input_list = input_list[::-1]

    n = int(input_list[-1])
    input_list.pop()
    people_name = []
    for i in range(n):
        cur = input_list.pop()
        people_name.append(cur)
    poeple_money = [0 for i in range(n)]

    while input_list!=[]:
        who_give = input_list.pop()
        money,num = map(int,input_list.pop().split(' '))
        if num==0: continue
        if money==0: get_each=0
        else: get_each = (money-money%num)//num
        give = get_each*num
        poeple_money[people_name.index(who_give)] -= give
        for i in range(num):
            poeple_money[people_name.index(input_list.pop())] += get_each
        

    ans = []
    for i in range(n):
        ans.append(str(people_name[i]+' '+str(poeple_money[i])+"\n"))
    return ans


if __name__ == "__main__":
    fin = open ('gift1.in', 'r')
    fout = open ('gift1.out', 'w')
    fout.writelines(solution(fin.readlines()))
    fout.close()