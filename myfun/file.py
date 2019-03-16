import random
if __name__ == '__main__':
    with open(r"C:\Users\Lenovo\PycharmProjects\demo1\myfun\temp1.text","a") as myfile:

        mlist = [random.randrange(0,100) for m in range(0,20)]

        print(mlist)

        for m in mlist:
            print(str(m) + "\n")

            myfile.write(str(m) + "\n")
