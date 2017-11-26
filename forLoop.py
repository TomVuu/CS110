sum = 0
for i in range (0, 101, 2):
   sum = sum + i
   print ("The sum of all even numbers between 1 and 100 is", sum)
...

sum = 0
for i in range (1,16):
    sum = sum + i*i
    print("The sum of squares between 1 and 15 is ", sum)


for row in range (0,8):
   for col in range (0,8):
      if (row + col) % 2 == 0:
            char = "X"
      else:
            char = "_"
      print (char, end = "")
   print()
            
    
    