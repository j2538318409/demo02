import random
if __name__ == '__main__':
    #编写Python程序判断字符串是否重复。（50
    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
    ]
    nlist = set(klist)
    mdict = {}
    if len(nlist) == len(klist):
        print("没有重复数据")
    else:
        print("有重复")
    mlist1 = []
    for i in klist :
       a = i.strip()
       mlist1.append(a)
    nset = set(mlist1)
    for i in mlist1:
        mdict[i] = mlist1.count(i)
    for m in mdict :
        if mdict[m] > 1:
            print("有重复字符为{0},重复的次数{1}".format(m,mdict[m]))
        else:
            print("没有重复")
    mlist = [1,3,2,5,6,4]
    for i in range(1,5):
     print(random.choice(mlist))
     print(random.choice(mlist))
    m = 0
    list = [1, 3, 2, 5, 6, 4]
    for i in range(0,6):
            print(i)
    mlist = list(i**i for i in range(1,11))
    print(mlist)
    mlist = list(i ** i for i in range(1, 11) if i % 2 ==0 )
    print(mlist)
    mlist  = [1,2,3]

    nlist = ['a','b','c']

    qlist = []
    for m in  mlist:
          for n in nlist:
              qlist.append(str(m) + n)
    print(qlist)
    qlist = [str(m)+n \

               for m in mlist \

               for n in nlist \

                 if m % 2 == 0]

    print(qlist)

    blist = ["Appol","Fool","Dix",1,2]

    newlist = []
    for b in blist:
          a = b.lower()
    newlist.append(a)
    print(newlist)
    for b in blist:

             if isinstance(b,str):

                a = b.lower()

                newlist.append(a)

    print(newlist)
    arrs = [b.lower()\
              for b in blist \
              if isinstance(b,str) \
              or isinstance(b,int) ]
    print(arrs)

    flist = [k.strip() for k in klist]
    rset = set(flist)
    if len(klist) == flist:
          print("有重复")
    else :
          print("没有重复")

    flist = [f.strip() for f in klist]
    nar = {f:flist.count(f) for f in flist}
    print(nar)
    nar = {f:f for f in flist}
    print(nar)
    klist = [
        "good ", "good ", "study",
        " good ", "good", "study ",
        "good ", " good", " study",
        " good ", "good", " study ",
        "good ", "good ", "study",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
        " day ", "day", " up",
      ]
    nlist = [k.strip() for k in klist]
    if len(nlist) == len(klist):
          print("没有")
    else:
          print("有")
    nlist = [k.strip() for k in klist]
    if len(klist) == len(nlist):
          print("没有")
    else:
          print("有")
    nlist = [k.strip() for k in klist]
    if len(nlist) == len(klist):
          print("没有")
    else:
        print("you ")
    n = {n:nlist.count(n) for  n in nlist}
    print(n)
    n = {n:nlist.count(n) for n in nlist}
    print(n)
    n = {n:nlist.count(n) for n in nlist}
    nlist = {n:n for n in nlist}
    print(nlist)
    nlist = {n:n for n in nlist}
    nlist = {n:n for n in nlist}
    #4.随机生成一个序列，10个元素，并对序列进行升序排序（10分）
    mlist = [m for m in range(1,10)]
    mlist.sort()
    print(mlist)















