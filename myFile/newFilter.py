if __name__ == '__main__':
    pass
    s = "good gor on on sres ,oirk.kiss study\n"
    s1 = s.replace(","," ")
    s2 = s1.replace("."," ")
    s3 = s2.replace("\n"," ")
    mlist = s3.split(" ")
    # raise print(23)
    del mlist[5]
    mlist.pop()
    mdict = {a:mlist.count(a) for a in mlist}

    mar = dict(sorted(mdict.items(),key= lambda x:x[1]))

    dix = lambda x:x*2
    print(dix(2))
    print(mar)
    #print(mdict)
    #print(s2)
    raise[ZeroDivisionError]


