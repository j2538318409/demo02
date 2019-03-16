class MyExcept(Exception):
    def show(self):
        print("123")
        print(self,"1")
    pass
if __name__ == '__main__':
    me = MyExcept()

    try:
        pass
        raise MyExcept
    except MyExcept as a:
        print("123")
        #调用了自定义类型拓展的方法
        a.show()
