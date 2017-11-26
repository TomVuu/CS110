myTable = []
nbrRows = 3
nbrCols = 3
for i in range (nbrRows):
    print("Processing row", i+1)
    myRow = []
    for j in range (nbrCols) :
        value = input("Enter col " + str(j+1) + " value : ")
        if value.isdigit():
            value=int(value)
        else:
            value = value
        myRow.append(value)
    myTable.append(myRow)
print("The elements in the table are: ",myTable)
