if __name__ == '__main__':
    #尝试异常的代码
    try:
         print(5/0)
    #捕捉异常
    except ZeroDivisionError :
         print("你输入有错误")
         pass
    mstr = " "
    mstr += 1
    print()
    print("234")
    try:
        print(5/0)
    except ZeroDivisionError as d:
        print("你的分母为0了")
    except Exception as d:
        print("来了")
    raise print("123321")
    raise 123


    pass