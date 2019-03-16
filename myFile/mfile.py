if __name__ == '__main__':
   pass
   myfile = open(r"C:\Users\Lenovo\PycharmProjects\demo1\myFile\f.text","r")

   while True:

      mydir = myfile.readline()

      print(mydir)

      if mydir == "":

           break

      print(mydir)

      print(mydir)
      a = " st"
      b = a.lstrip()
      print(b)


   myfile.close()