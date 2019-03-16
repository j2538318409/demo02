if __name__ == '__main__':
   mlist = list()
   #在列表尾部追加
   mlist.append("123")
   mlist.append("123")
   #给定位置追加
   mlist.insert(0,"321")
   arr = []
   print(type(arr))
   print(mlist)
   #使用pop从列表算出数据
   mlist.pop()
   print(mlist)
   #输出del中的数据
   del mlist[0]
   print(mlist)
   mlist.remove("123")
   print(mlist)
   #删除本身数据，但不删除本身
   del mlist
   #删除整个列表，该对象不存在
   #mlist.remove(输入数据)通过数据去删除数据
   #pop如果不指定参数删除列表种最后一个参数并返回
   




