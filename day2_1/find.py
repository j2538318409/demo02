if __name__ == '__main__':
    str1 = "abcabcabc"
    str2 = "abcdefg"
    a = 0
    arr1 = {}
    for b in str1 :
         # val = 要查找的字符串.count（key）
         # 字典名[key] = val
         arr1[b] = str1.count(b)
    print(arr1)
    for s in arr1:
        if arr1[s] > 1:
            #字典名[key] == value
            print("有重复字符串为{0}，一共出现了{1}".format(s,arr1[s]))
        else:
            print("没有重复")
            break
    rlist = [1,1,2,3,5]
    rset = set(rlist)
    for r in rset:
        print(r)
