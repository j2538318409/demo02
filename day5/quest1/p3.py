def checkedRe():

    name = input("请输入用户名")

    if not (len(name) >= 6 and len(name) <= 16):

        print("用户名允许数字字母6-16位")

        return

    password = input("请输入密码")

    if password.find("*") > -1 or password.find("#") > -1:

        print("不允许出现*#!")

        return
    print("注册成功 用户名：{name},密码:{password}".format(name=name,password=password))
if __name__ == '__main__':
    pass
