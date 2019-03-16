if __name__ == '__main__':
     mdict = {"name":1,"password":2}
     print(type(mdict))
     #用这种遍历方式取出的是健
     for kv in mdict:
         print("type is {0}".format(type(kv)))
         print(kv)
     #取出字典的值
     for v in mdict:
         print("madict[{key}]={val}".format(key = v,val = mdict[v]))
     for k,v in mdict.items():
         print(k,v)
     nlist = {k:v for k,v in mdict.items() if v % 2 == 0}
     print(nlist)
     v = mdict.get("name")
     print(v)
     a = max(mdict)
     print(a)
     for m in mdict.keys():
         print(m.title())
