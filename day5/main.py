import day5.quest1.p1 as p1

import day5.quest1.p2 as p2

import day5.quest1.p3 as p3

import day5.quest1.p4 as p4

if __name__ == '__main__':
    pass

    mlist = ["[1]对一字符串进行翻转操作",
             "[2]创建一个列表，存储公司10个名单，对这些名单进行排序，要求按姓名的字符多少来排",
             "[3].输入用户名密码进行注册，要求用户名允许数字字母6-16位，密码6-16位，不允许出现*#!",
             "[4]输入一个字符串为社会主义核心价值观的全拼，每个词用空格进行分隔，将这个字符串，转成列表，遍历输出"
             ]

    mdict = {1:p1.myReverse,
             2:p2.checkedSort(),
             3:p3.checkedRe(),
             4:p4.checkedSplit()
             }

    while True:

        for m in mlist:

            print(m)

        che = input("请输入你的选择")

        mdict[int(che)]()

