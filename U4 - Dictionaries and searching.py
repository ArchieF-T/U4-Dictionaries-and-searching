# Archie Fall-Taylor 05/03/21
# Dictionaries and searching

romanInventions = {
    "Aquaducts": "Bridges that carry water",
    "Sanitation": "Clean water and adequate sewage disposal",
    "Roads": "Wide ways leading from anywhere to Rome",
    }

menu = [
    "List invention",
    "Look up an invention",
    "Add an invention",
    "Edit an invention",
    "Delete an invention",
    "Quit"
     ]

loopMenu = True

while loopMenu:
    print("What did the Romans ever give us?")
    for i in range(len(menu)):
        print(i+1, menu[i])
    option = int(input("Please enter a number:"))

    if option == 1:
        #print("You selected option", option)
        print("The Romans gave us...\n")
        for j in romanInventions.keys():
            print(j)
    elif option == 2:
        #print("You selected option", option)
        a = input("\nWhich invention are you interested in?")
        x = romanInventions.get(a, "Sorry, invention not found\n")
        print (x)
    elif option == 3:
        #print("You selected option", option)
        b = input("Enter an invention to add: ")
        if not b in romanInventions:
            bb = input("Enter a definition: ")
            romanInventions[b] = bb
            print("invention added")
        else:
            print("That invention already exists")
    elif option == 4:
        #print("You selected option", option)
        c = input("Which invention would you like to edit? ")
        if c in romanInventions:
            cc = input("Enter a new definition")
            romanInventions[c] = cc
            print("Invention added")
        else:
            print("Invention not found")
    elif option == 5:
        #print("You selected option", option)
        d = input("Invention to delete: ")
        if d in romanInventions:
            dd = input("Are you sure? Enter (y/n):")
            romanInventions.pop(d)
            print("Invention deleted")
        else:
            print("Invention not found")
    else:
        print("Bye")
        loopMenu = False
