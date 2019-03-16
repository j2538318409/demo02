import random
if __name__ == '__main__':
    a = 0
    while a < 10:
        j = 10
        while j > a:
            j=j-1
            print(" ",end="")
        a=a+1
        i = 0
        while i < a:
            i=i+1
            print("*", end="")
            if i > 1:
                print("*", end="")
            else:
                continue
        print()