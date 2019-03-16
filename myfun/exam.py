if __name__ == '__main__':
    pass
    birth1 = input("请输入第一个的生日")
    birth2 = input("请输入第二个的生日")
    find1 = birth1.strip(":")
    find2 = birth2.strip(":")
    if int(find1[0]) > int(find2[0]):
        print("第二个年龄大")
    elif int(find1[0]) == int(find2[0]):
        if int(find1[0]) > int(find2[0]):
            print("第二个年龄大")
        elif int(find1[1]) ==  int(find2[1]):
            print("一样大")
        else:
            print("第一个大")
    else:
        print("第一个大")

