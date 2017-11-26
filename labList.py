student = [[1, "Jane", "10%"], [2, "Adam", "80%"], [3, "Alley", "90%"]]
for row in student:
    for col in row:
        print (col, "", end="") 
    print()
for row in range (len(student)):
    for colum in range (len(student[row])):
        print(student[row][colum], " ", end="")
    print()

student[0][2] = "70%"
for row in range (len(student)):
    for col in range (len(student[row])):
        print(student[row][col], " ", end= "")
    print()
    
    
