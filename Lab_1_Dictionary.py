myTable = {"H":"Hydrogen", "He":"Helium", "Li":"Lithium"}

print(myTable.keys())

print(myTable.values())

print(myTable.items())

print(myTable.get("Li"))

myTable["Be"] = "Berylium"

print(myTable.get("Be"))

myTable["Be"] = "Beryllium"

print(myTable.get("Be"))

for a in myTable:
    print (a, myTable[a])
    
myMetals= {"Cu":"Copper", "Ag":"Silver", "Au":"Gold"}
print (myMetals.items())

myTable.update(myMetals)
print(myTable.items())