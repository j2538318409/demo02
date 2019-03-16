import random
if __name__ == '__main__':
    num1 = int(input("请输入一个数字"))
    num2 = num1 ** 1/2
    print("平方根为：",num2)
    num3 = int(input("请输入一个整数并且猜到大小"))
    a = random.choice(range(1000))
    if num3 > a:
        print("你赢了")
    elif num3 == a :
        print("再试一次？")
    else :
        print("你输了")