import random
def chekedNum():
    slist = [random.randint(1,10) for i in range(0,10)]
    mlist = [random.randint(1,15) for i in range(0,10)]
    set1 = set(slist)
    set2 = set(mlist)
    nlist = set1 | set2
    print(nlist)
    pass
if __name__ == '__main__':
    pass
