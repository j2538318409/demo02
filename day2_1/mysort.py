import random
if __name__ == '__main__':
    mystu = ["张三","王二","面膜","半场"]
    mynum = [3,6,2,1,4,5]
    #永久排序reverse设置位降序
    mynum.sort(reverse=True)
    print(mynum)
    #打乱顺序
    #导包random
    random.shuffle(mynum)
    print(mynum)
    print(sorted(mynum))
    #sorted()临时排序结果,返回值就是list列表
    mynum1 = [3,7,4,5]
    #列表反转
    mynum1.reverse()
    print(mynum1)
    

