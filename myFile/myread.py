if __name__ == '__main__':
    pass
    with open(r"C:\Users\Lenovo\PycharmProjects\demo1\myFile\f.text","a") as myfile:
        # 把光标设置在最开头


        a = myfile.tell()

        print(a)

        mboor = myfile.writable()

        print(mboor)

        arr = ["111mar","dix","krtrs"]
        #拿到当前光标在的位置



        myfile.writelines(arr)

