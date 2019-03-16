if __name__ == '__main__':
    vad = int(input("请输入行数"))
    dix = range(1,2*vad)
    for i in dix[0:vad]:
        for j in dix[0:vad-i]:
            print(" ",end="")
        for j in dix[0:2*i-1]:
            print("*",end="")
        print()
    for i in dix[0:vad-1]:
        for j in dix[0:i]:
            print(" ",end="")
        for j in dix[(vad-i)*2-1:0:-1]:
            print("*",end="")
        print()