def name(m,n):
    return 1
def age():
    print("123")
def myfundefault(name,cu,val="gundan"):
    print(val,cu)
    print(name)

def mfun(di):
    pass
if __name__ == '__main__':
    myfundefault("23",1,"gan")
    mfun(1)
    print()
    print(name(3,1))
    age()
    yer1 = int(input("请输入第一个人的月分"))
    yer2 = int(input("请输入第二个人的月分"))
    nyer = "2".split(":")
    print(nyer[1])
    sum1 = int(nyer[1])*30+int(nyer[2])
    print("是2018年的{yer}".format(yer=sum1))
    a = yer1 % yer2
    print(a)
    if a == 1 :
        print("非常有缘")
    if a == 2 :
        print("比较有缘")
    if a == 3 :
        print("缘分一般")
    if a == 4 :
        print("有仇")
    pass





