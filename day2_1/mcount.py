if __name__ == '__main__':
    a = "abcabcabc"
    c = "123456"
    mdict = {}
    for b in c:
        mdict[b] = c.count(b)
    for m in mdict:
        if mdict[m] > 1:
            print("重复的字符为：{0},一共重复了：{1}".format(m,mdict[m]))
        else:
            print("没有重复")