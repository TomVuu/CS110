answer = input("Continue (Y/N)?")
if answer.upper () == "N":
    exit ("Aborting...")
elif answer.upper () == "Y":
    processEverything ()
else:
    print ("Invalid response, fool!")