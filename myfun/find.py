class MyException(ZeroDivisionError):

    pass

try:
    print("你的分母为零了，")

    #手动抛出异常
    raise MyException

except MyException as a:

    print("catch MyExcetion")

except ValueError as v:

    print(v)

except Exception as e:

    print(e)

else:

    print("try except else")

finally:

    print("finally")

