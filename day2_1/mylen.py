if __name__ == '__main__':
    mlist = [1,2,3,4]

    #拿到长度
    mlen = len(mlist)

    print(mlen)

    for l in mlist:
       print("mlist[{0}]={1}".format(l.__index__(),l))
    nlist = mlist[0:3]
    print("mlist id is {mlistid}".format(mlistid=id(mlist)))
    print("nlist id is {nlistid}".format(nlistid=id(nlist)))

