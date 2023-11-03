# 1. Напишите программу вычисления арифметического
#    выражения заданного строкой. Используйте операции +,-,/,*
#    приоритет операций стандартный. Добавьте скобки, приоритет операций меняется.

actions = {
    "^": lambda x, y: float(x) ** float(y),
    "*": lambda x, y: float(x) * float(y),
    "/": lambda x, y: float(x) / float(y),
    "+": lambda x, y: float(x) + float(y),
    "-": lambda x, y: float(x) - float(y)
}


def Calc(srcstr):
    ls = srcstr.split()
    prior = {"(": 1, ")": 1, "*": 2, "/": 2, "+": 3, "-": 3}

    priznak = []
    for i in ls:
        if i in prior:
            priznak.append(prior[i])
        else:
            priznak.append('')

    curi = 1
    cur = priznak[1]

    for i, tmp in enumerate(priznak):
        if isinstance(tmp, int) and tmp < cur:
            curi = i
            cur = tmp
    curOperVal = actions[ls[curi]](ls[curi-1], ls[curi+1])
    del ls[curi-1: curi+2]
    ls.insert(curi-1,curOperVal)
    print(ls)
    #print(curOperVal)


    return priznak

srcstr = '2 + 5 / 2 - 3'
print(Calc(srcstr))