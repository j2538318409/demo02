if __name__ == '__main__':
    pass
    num = int(input("请输入一个数字"))
    sum = 0
    a = 1
    for n in range(1,num+1):
        a *= n
        sum += a
    print("{0}的阶乘的和为{1}".format(num,sum))
    fn = "arr kors nars"
    nfn = fn.center(20,"o")
    print(nfn)
    

