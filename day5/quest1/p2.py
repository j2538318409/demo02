def checkedSort():
    mlist = ["张震", "王越", "靳中伟", "李庸", "李广军"]

    mdict = {m:len(m) for m in mlist}

    dict_sorted = dict(sorted(mdict.items(), key=lambda x: x[1], reverse=True))

    print(sorted(mdict.items(), key=lambda x: x[1], reverse=True))

    print(mdict.items())

    print(dict_sorted)

    lu = lambda a: a[1]
    list1 = ["1", "2", "3"]
    #print(lu(list1))

    # i = 0
    #
    # while i < len(mlist):
    #
    #     j = 0
    #
    #     while j < len(mlist)-1:
    #
    #         if int(nlist[j]) < int(nlist[j + 1]):
    #
    #             i = nlist[j]
    #
    #             nlist[j] = nlist[j + 1]
    #
    #             nlist[j + 1] = i
    #
    #             i1 = mlist[j]
    #
    #             mlist[j] = mlist[j + 1]
    #
    #             mlist[j + 1] = i1
    #
    #         j = j + 1
    #
    #     i = i + 1
    #
    # print(mlist)

def checkedSord1():
    mlist = ["张震", "王越", "靳中伟", "李庸", "李广军"]

    nlist = [len(m) for m in mlist]

    mr = {}

    print(sorted(nlist))

    for i in sorted(nlist):

        mr[mlist[nlist.index(i)]] = i

    print(mr)
    pass
if __name__ == '__main__':
    checkedSort()
    pass













