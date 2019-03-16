if __name__ == '__main__':
    mdict = {"name":"kor","age":"12"}
    #通过变量名拿到属性值
    print(mdict["name"])
    #通过属性名修改值域
    mdict["name"] = "fand"
    print(mdict)
    #删除键值对
    del mdict["name"]
    print(mdict)
    #str()返回一个字符串型的字典
    a = str(mdict)
    print(type(a))
    print(mdict)
    for m in mdict :
        print("mdict key = {key},values = {val}".format(key=m,val=mdict[m]))
    for m in mdict.values():
        print("mdict index={ind},val={v}".format(ind=123,v=m))
    for n in range(1,10):
         print(n.__index__())
    for m,r in mdict.items() :
        print("mdict key={key} val={val}".format(key=m,val=r))
