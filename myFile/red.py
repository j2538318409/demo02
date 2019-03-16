if __name__ == '__main__':
    d = open(r"C:\Users\Lenovo\PycharmProjects\demo1\myFile\f.text","r")

    mpos = d.tell()

    print(mpos)

    list = d.readlines()

    print(list)

    mbool = d.readable()

    # print(mbool)

    d.close()
