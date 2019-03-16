if __name__ == '__main__':
    arr1 = [1,2,3,4,5,6,7,8,9]
    arr2 = [1,2,3,4,5,6,7,8,9]
    for a in arr1:
        for b in arr2:
            print(a,"*",b,"=",str(a*b).rjust(2," ")," ",end="",sep="")
            if a == b:
                print()
                break




