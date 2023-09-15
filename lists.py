Students_mark=[60,80,90,98]
#changing 80-89
Students_mark[1]=89
print(Students_mark)

#ADDing an item is called apending ()
Students_mark.append(55)
print(Students_mark)

#finding size
print(len(Students_mark))

#sum
import math
Students_mark=math.fsum([60,80,90,98,55])
print(Students_mark)

#python function that takes two lists and returns two if they have one common member
Students_mark =input("your items")
Students_class= input("your items")
print ("True,there is a common member in students_mark and students_class")
 
 
    
