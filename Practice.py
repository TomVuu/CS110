number = []
max_input = 5
digit = 0
product = 1
while digit < 5:
    my_num = input("Please enter a number:")
    if my_num.isdigit():
        number.append(int(my_num))
        digit = digit + 1
    else:
        print ("That is not a number")   
    print ("The sum of the number is:" , sum(number))
for element in number:
    product = element * product
    print("The product of these numbers is:" , product)
    print("The largest number you entered was:", max(number))

 
#Q2
Scratch = ["ab", "helloh", "abab","aba", "1221", "2321", "yellow"]
total = 0
for element in Scratch:
    if len(element) >= 3:
        if element[0] == element[(len(element)-1)]:
            total = total + 1
    else:
        print("none")
    print("There are", total, "elements in the list that satify the constraint.")
    
        