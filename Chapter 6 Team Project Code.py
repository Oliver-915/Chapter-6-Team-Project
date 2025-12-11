import os

def contact_manager():
    contact_menu()
    
def contact_menu():
    #contact_menu accepts no arguments
    #prompts the user to select one option
    #returns the users selection
    print("CONTACTS")
    print("Please choose one of the following options...")
    print("(1) Add Contact"+("\n")+"(2) Search Contact"+("\n")+"(3) Edit Contact"+("\n")+"(4) Delete Contact"+("\n")+"(5) Display All Contacts"+("\n")+"(6) Exit")
    menu_selection = int(input("\nEnter your selection here: "))
    while menu_selection > 0 and menu_selection < 7:
        if menu_selection == 1:
            print("\nSelected Option: Add Contact\n")
            contact_add()
        elif menu_selection == 2:
            print("\nSelected Option: Search Contact\n")
            contact_search()
        elif menu_selection == 3:
            print("\nSelected Option: Edit Contact\n")
            contact_edit()
        elif menu_selection == 4:
            print("\nSelected Option: Delete Contact\n")
            contact_delete()
        elif menu_selection == 5:
            print("\nSelected Option: Display All Contacts\n")
            contact_display()
        elif menu_selection == 6:
            print("\nSelected Option: Exit\n")
            print("Thank you for using Contact Manager")
        else:
            print("Invalid input, Try Again")
            menu_selection = int(input("\nEnter your selection here: "))
    
def contact_add():
    #accepts no arguments
    #adds a contact to the list
    print('Add contacts here. Input "." if you do not have anything to put.')
    name = input("Name: ")
    address = input("Street Address: ")
    phone = input("Phone Number: ")
    email = input("Email Address: ")
    
    myfile = open('contacts.txt', 'a')
    
    myfile.write(name + '\n')
    myfile.write(address + '\n')
    myfile.write(phone + '\n')
    myfile.write(email + '\n')
    
    myfile.close()
      
def contact_search():
    # accepts no arguments
    # asks for a string
    # looks for the string in contacts.txt + verification
    # loop until blank if not found
    # if found, return entire contact and ask the user to confirm.
    
    # prime loop
    try_again = "y"
    
    #loop until try_again = no
    while try_again.lower() == "y":
        #get input
        search = input(str("Enter a name to look up contacts for: "))
        
        #set search status
        found = False
        
        #open the file in read
        contact_file = open('contacts.txt', 'r')
        
        #prime loop
        name = contact_file.readline()
        
        #loop to read each line
        while name != '' and not found:
            address = contact_file.readline()
            number = contact_file.readline()
            email = contact_file.readline()
            
            #strip new line
            name = name.rstrip('\n')
            address = address.rstrip('\n')
            number = number.rstrip('\n')
            email = email.rstrip('\n')
            
            if name.lower() == search.lower():
                print("\nContact Found")
                print("Name:", name)
                print("Address:", address)
                print("Phone Number:", number)
                print("Email:", email)
                found = True
            else:
                name = contact_file.readline()
                
        contact_file.close()
        
        #search status = false
        if not found:
            print("\nNo Contact Found.\n")
            
        #Try again?
        try_again = input(str("Try again? (y/n): "))
        
        while try_again.lower() != "y" and try_again.lower() != "n": #validation
            print("Input Error, Try again")
            try_again = input(str("Try again? (y/n): "))
            
        if try_again.lower() == "y":
            print("Reseting\n")
        elif try_again.lower() == "n":
            print("Returning\n")
            return name, address, number, email
            
def contact_edit(name, address, number, email):
    # accepts 4 arguments and uses os module
    # asks what to change
    # input to replace the arguments
    # loop to write contacts.txt to temp file replacing found arguments with input
    
    found = False
    
    # print options
    print("What do you want to change?")
    print("Name (1):", name)
    print("Address (2):", address)
    print("Phone Number (3):", number)
    print("Email (4):", email)
    print("Quit (5):")
    
    # verification and input
    choice = input(int("=> "))
    while choice > 0 and choice < 6:
        print("Invalid input, try again")
        choice = input(int("=> "))
    
    if choice == 1:
    
    
        
    
    
def contact_delete():
    pass 
    
def contact_display():
    # accepts no arguments
    # loops and displays all contacts in the contacts.txt in a readable format
    # when a line is empty quit loop
    
    #open the file in read
    contact_file = open('contacts.txt', 'r')
        
    #prime loop
    name = contact_file.readline()
    
    #loop to read each line
    while name != '':
        address = contact_file.readline()
        number = contact_file.readline()
        email = contact_file.readline()
        
        #strip new line
        name = name.rstrip('\n')
        address = address.rstrip('\n')
        number = number.rstrip('\n')
        email = email.rstrip('\n')
        
        #print all in readable format
        print("\nContact Found")
        print("Name:", name)
        print("Address:", address)
        print("Phone Number:", number)
        print("Email:", email)
        
        #ends loop if empty
        name = contact_file.readline()
            
    contact_file.close()


