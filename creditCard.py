userInput = input("Enter credit card number: ")
ccNumber = ""
for char in userInput:
    if char.isalnum():
        ccNumber = ccNumber + char
        print(ccNumber)