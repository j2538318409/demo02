def find1():
    nlist = [i for i in range(1,11)]
    mlist = [i for i in range(1, 11)]
    for n in nlist:
        for m in mlist:
            print(n,"+",m,"=",str(n*m).rjust(2," ")," ",end="",sep="")
            if n==m:
                print()
                break
def find2(numr):
    i = 0
    while i <=numr//2 :
        k = numr//2+1
        while k > i:
            print(" ",end="",sep="")
            k=k-1
        j = 0
        while j < i*2-1:
            print("*",end="",sep="")
            j=j+1
        print()
        i=i+1
    i = 0
    while i <= numr//2:
        k =0
        while k < i:
            print(" ", end="", sep="")
            k = k + 1
        j = numr
        while j > i * 2 :
            print("*", end="", sep="")
            j = j - 1
        i=i+1
        print()
def find3(ner):
    i = 0
    while i <= ner:
        k = ner
        while k > i:
            print(" ",end="",sep="")
            k=k-1
        j = 0
        j = 0
        while j < i*2-1:
            print("*", end="", sep="")
            j=j+1
        print()
        i = i + 1
def find4():
    i = 1
    while i < 200:
        print(str(i).rjust(4," "),end="",sep="")
        if i % 10 == 0:
            print()
        i = i +1
if __name__ == '__main__':
    find1()
    find2(7)
    find3(4)
    find4()
    pass