if __name__ == '__main__':
    i = 0
    sum1 = 0
    while i <= 100:
        sum1+=i
        i=i+1
    print(sum1)
    i = 1
    while i <=5:
        j = 1
        while j <=i:
            print("*",end="",sep="")
            j=j+1
        print()
        i = i + 1
    nlist = ["Google","Baidu","Runoob","Taobao"]
    for n in range(len(nlist)):
        print(n,nlist[n])
    pass
    num1 = 2
    num2 = 1
    sum1 = 0
    for f in range(1,21):
        sum1+=num1/num2
        tem = num1a
        nnum1= num1+num2
        num2=tem
    print(sum1)
    for b in range(1,21):
         sum1 += num1/num2
         print(num1, "/", num2)
         tem = num1
         num1 = num1+num2
         num2 = tem
    print(sum1)
    a = int(input("请输入一个数"))



