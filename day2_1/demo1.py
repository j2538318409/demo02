if __name__ == '__main__':
    arr = [1,2,3,4,5,6,7,8,9]
    for i in arr :
        for j in arr :
            a = str(i*j)
            print(str(i)+"*"+str(j)+"="+a.rjust(2," "),end=" ")

            if i == j:
                print()
                break
    dif = 0
    d=0
    while dif <=100 :
        dif+=1
        print(str(dif).rjust(4," "),end="",sep="")
        d+=1
        if d%10==0:
            print()
