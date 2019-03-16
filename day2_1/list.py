import random
if __name__ == '__main__':
    #添加元素
    mlist = list()
    mlist.append("还行吧")
    mlist.append(1)
    print(mlist)
    #使用insert在列表指定为值添加数字
    mlist.insert(1,"不行")
    print(mlist)
    #删除mlist链表
    del mlist
    #remove（）通过指定元素名删除值域
    mlist.remove("还行吧")
    print(mlist)
    mlist.append("123")
    a = mlist.pop()
    mlist.clear()
    print(mlist)
    dlist = mlist[1:3]
    dix = 1
    print("nid={0}".format(id(mlist)))
    print("did={0}".format(id(dlist)))
    print("int--->",dix in mlist)
    print("not in ---->",dix not in mlist)
    llist = [1,23,4,56]
    squeres = [v**2 for v in range(1,10)]
    print(squeres)
    nlist = [[7,8,9],[4,5,6],[1,2,3]]
    for n in nlist:
         for b in n :
             print("nlist[{0}]={val}".format(b.__index__(),val=b))
    nlist = [1,2,4,5,6]
    mlist = [6,5,4,3,2]
    qlist = [m+n for n in nlist if n % 2 ==0 for m in mlist]
    print(qlist)
    mlist = [['a','b'],['c','d'],['e','f']]
    qlist = [[a,b] for a,b in mlist]
    print(qlist)
    plist = [random.randint(0, 100) for v in range(1,10)]
    llist = plist[1:3:1]
    print(llist)
    a = len(plist)
    print(max(plist))
    b = plist.count(1)
    print(b)
    fan = [123,321]
    plist.extend(fan)
    print(plist)



