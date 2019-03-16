if __name__ == '__main__':

   dix = dict({"1":"321"})
   print(dix)
   dict0 = {'zhao': 89,
            'qian': 91,
            'sun': 84,
            'li': 98,
            'zhou': 93,
            'wu': 86}
   # print(dict0.items())
   dict_sorted = dict(sorted(dict0.items(), key=lambda x: x[1], reverse=True))
   #print(lambda x: x[1])
   # print(dict_sorted)