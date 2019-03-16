#随机数生成器
import random
if __name__ == '__main__':
    n3 = range(0,10,2)
    print(type(n3))
    for n in n3:
        print(n)
    #第一个参数小于第二个参数时，第三个参数必须为证
    #第二个参数小于第一个参数时，第三个参数必须为负
    mlist= [i for i in range(0,10,2)]
    print(mlist)
    v = random.randint(5,10)
    print(v)
    # 从给定序列中选择一个数
    val = random.choice(range(9))
    print("val={val}".format(val=val))
    mstr = "abcdefibdsad"
    tstr = ""
    for i in range(5):
        v = random.choice(mstr)
        tstr+=v
        print(v)
    print(tstr)
    #从零到9随机生成数字
    #从零到9随机生成数字rval = random.randrange(0,10,1)
    print("rval={rval}".format(rval = rval))
    #打乱原有的顺序
    a = int(input("请输入一个数字"))
    b = random.randint(0,1000)
    print(b)
    if a > b:
        print("你赢了")
    elif a == b:
        print("相等")
    else:
        print("你输了")