file = open("myfile.txt", "r")
data = file.read()
lines = data.split("\n")
for line in lines:
    line = line.strip(".")
    words = line.split(" ")
    for word in words:
        print(word)
file.close()