import random
if __name__ == '__main__':
   arr = [a for a in range(10)]
   print(arr)

   if random.randint(1,100) in arr:
       print("在里面")
   else:
       print("没有在")
   a = random.randrange(4)
   print(a)
   a = range(10)

