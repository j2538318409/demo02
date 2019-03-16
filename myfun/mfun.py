import myfun.nesum as n
def myfunction(**names):
    print(type(names))
    for n in names.items():
        print(n)
if __name__ == '__main__':
    mstr = "1"
    nstr = "kkkkk"
    nstr = mstr.center(10,"-")
    print(nstr)
    ntuple = mstr.partition("o")
    print(ntuple)
    print( mstr.join(nstr))
    n.find4()
    n.find2(7)
    n.find3(8)
    n.find1()




