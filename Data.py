
filename = 'C:/Users/User/PycharmProjects/DataPreparation/MyText.txt'

with open(filename) as fn:

   ln = fn.readline()

   lncnt = 1
   while ln:
       print("Line {}: {}".format(lncnt, ln.strip()))
       ln = fn.readline()
       lncnt += 1




