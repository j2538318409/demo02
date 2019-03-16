import random
if __name__ == '__main__':
    str1 = "abcdefjhjkrimon mon dix"
    a = str.find("dix")
    print(a)
    b = str.index("d")
    print(b)
    #查看m字符在str种出现了几次
    c = str.count("m")
    print(c)
    #replace(old,new[,max])
    vars = str.replace("a","o")
    print(vars)
    d = str1.split(" ")
    print(d)
    a = str1.capitalize()
    print(a)
    b = str1.startswith("2",0,6)
    print(b)
    mynum = [3,5,2,3,1]
    print("打乱签",mynum)
    random.shuffle(mynum)
    print("打乱后",mynum)
    mynum.sort()
    print(mynum)
    sorted(mynum,reverse=True)
    mynum.reverse()
    print(mynum)
    a = mynum.__len__()
    #print(a)
    for l in  mynum :
        print("mynum[{0}] = {1}".format(l.__index__(),l))
