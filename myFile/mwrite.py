if __name__ == '__main__':
    #全路径
    d = open(r"C:\Users\Lenovo\PycharmProjects\demo1\myFile\f.text", "a")
    #返回值是写入多少字符

    #判断文件是否具有可写全限
    mbool = d.writable()

    # mwe = d.write("gundan")
    # print("mwr = {mwrkey}".format(mwrkey = mwe))

    mlist = ["gun","dan","c can i up"]

    d.writelines(mlist)
    #指定指定位置到

    d.seek(0,2)

    mpos = d.tell()

    print(mpos)


    print("你说对象了laotie")

    d.close()



