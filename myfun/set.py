import random
import myfun.mfun as m
def reg (name,pwd,naleName = ""):
    if naleName :
        user = {"name":name,"pwd":pwd,"naleName":naleName}
    else :
        user = {"name":name,"pwd":pwd}
    return  user
if __name__ == '__main__':
    mset = {1,2,3,4}
    nset = {4,5,6}
    print(reg("张三","123"))
    print(ms not in mset)
    #或运算|
    nset = mset | nset
    #与运算&
    nset = mset & nset
    print(nset)
    #逻辑差
    mset = mset - nset
    print(mset)
    mset = mset ^ nset
    print(mset)
    knet = {3}
    print(mset.issuperset(knet))
    nfs = frozenset(nset)
    print(nfs)
    slist = [a for a in range(1,10)]
    b = random.choice(range(1,10))
    print(b in slist)
    m.myfunction(a="123",b="321")
    arr = [" 1 ","2","3"]

    #arr12 =[]
    arr = [i.strip() for i in arr]


