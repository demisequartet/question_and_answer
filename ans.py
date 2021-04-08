from copy import deepcopy

ans = []


def printList(ans):
    for i in ans:
        for j in i:
            print(j, end='')
        print('\n')


def solve(list, cnt, now):

    if now == 8:
        return

    temp1 = deepcopy(list)
    temp2 = deepcopy(list)
    temp3 = deepcopy(list)
    temp4 = deepcopy(list)

    temp1.insert(now+cnt+1, '+')
    temp2.insert(now+cnt+1, '-')
    temp3.insert(now+cnt+1, '*')
    temp4.insert(now+cnt+1, '/')

    ans.append(temp1)
    ans.append(temp2)
    ans.append(temp3)
    ans.append(temp4)

    solve(temp1, cnt+1, now+1)
    solve(temp2, cnt+1, now+1)
    solve(temp3, cnt+1, now+1)
    solve(temp4, cnt+1, now+1)


def evalList(list):
    for i in list:
        temp = ''.join(i)
        evalNum = eval(temp)
        # print(temp)
        if evalNum == 100:
            print(temp)


if __name__ == '__main__':
    calc = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    solve(calc, 0, 0)

    evalList(ans)
