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
    searched = False
    
    while True:
        if menu_selection == 1:
            print("\nSelected Option: Add Contact\n")
            contact_add()
        elif menu_selection == 2:
            print("\nSelected Option: Search Contact\n")
            name, address, number, email = contact_search()
            searched = True
        elif menu_selection == 3:
            if searched:
                print("\nSelected Option: Edit Contact\n")
                contact_edit(name, address, number, email)
            else:
                print("Please search first\n")
        elif menu_selection == 4:
            if searched:
                print("\nSelected Option: Delete Contact\n")
                contact_delete(name)
                searched = False
            else:
                print("Please search first\n")
        elif menu_selection == 5:
            print("\nSelected Option: Display All Contacts\n")
            contact_display()
        elif menu_selection == 6:
            print("\nSelected Option: Exit\n")
            print("Thank you for using Contact Manager")
            quit()
        else:
            print("Invalid input, Try Again")
            menu_selection = int(input("\nEnter your selection here: "))
            
        print("Please choose one of the following options...")
        print("(1) Add Contact"+("\n")+"(2) Search Contact"+("\n")+"(3) Edit Contact"+("\n")+"(4) Delete Contact"+("\n")+"(5) Display All Contacts"+("\n")+"(6) Exit")
        if menu_selection > 0 and menu_selection < 7:
            menu_selection = int(input("\nEnter your selection here: "))
    
def contact_add():
    #accepts no arguments
    #adds a contact to the list
    print('Add contacts here. Input "." if you do not have anything to put.')
    name = input("Name: ") or "."
    address = input("Street Address: ") or "."
    phone = input("Phone Number: ") or "."
    email = input("Email Address: ") or "."
    
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
    # renames temp and deletes contact
    
    found = False
    
    # print options
    print("What do you want to change?")
    print("Name (1):", name)
    print("Address (2):", address)
    print("Phone Number (3):", number)
    print("Email (4):", email)
    print("Quit (5):")
    
    # verification and input
    choice = int(input("=> "))
    while not found:
        if choice <= 0 or choice >= 6:
            print("Invalid input, try again")
            choice = int(input("=> "))
    
    if choice == 1:
        name = input("New Name: ") or name
        found = True 
    elif choice == 2:
        address = input("New Address: ") or address
        found = True 
    elif choice == 3:
        number = input("New Phone Number: ") or number
        found = True 
    elif choice == 4:
        email = input("New Email: ") or email
        found = True 
    elif choice == 5:
        return name, address, number, email
    
    #open files
    infile = open('contacts.txt', 'r')
    outfile = open('temp.txt', 'w')
    
    #prime loop
    old_name = infile.readline()
    old_address = infile.readline()
    old_number = infile.readline()
    old_email = infile.readline()
    
    while old_name != '' or old_address != '' or old_number != '' or old_email != '' :      
        old_name = old_name.rstrip('\n')
        old_address = old_address.rstrip('\n')
        old_number = old_number.rstrip('\n')
        old_email = old_email.rstrip('\n')
        
        if old_name.lower() == name.lower():
            outfile.write(name + '\n')
            outfile.write(address + '\n')
            outfile.write(number + '\n')
            outfile.write(email + '\n')
        else:
            outfile.write(old_name + '\n')
            outfile.write(old_address + '\n')
            outfile.write(old_number + '\n')
            outfile.write(old_email + '\n')
            
        old_name = infile.readline()
    
    #close files
    infile.close()
    outfile.close()
    
    #remove and rename files
    if found:
        os.remove('contacts.txt')
        os.rename('temp.txt', 'contacts.txt')
        print("Contact changed.")
    
   

def contact_delete(name):
    # accepts name argument
    # writes a temp file using contacts.txt without name and attached contacts

    confirm = input(f"Are you sure you want to delete {name}? (y/n): ")
    if confirm.lower() != "y":
        print("Delete cancelled.")
        return 

    # open files
    infile = open('contacts.txt', 'r')
    outfile = open('temp.txt', 'w')
    
    # edit files
    current_name = infile.readline()
    
    while current_name != '':
        address = infile.readline()
        number = infile.readline()
        email = infile.readline()

        # strip newline characters
        name_delete = current_name.rstrip('\n')
        address_delete = address.rstrip('\n')
        number_delete = number.rstrip('\n')
        email_delete = email.rstrip('\n')

        # write all contacts that do NOT match the name
        if name_delete.lower() != name.lower():
            outfile.write(name_delete + '\n')
            outfile.write(address_delete + '\n')
            outfile.write(number_delete + '\n')
            outfile.write(email_delete + '\n')
        else:
            deleted = True

        # read next contact
        current_name = infile.readline()

    infile.close()
    outfile.close()
    
    print(f"Contact '{name}' deleted.")

def contact_display():
    # accepts no arguments
    # loops and displays all contacts in the contacts.txt in a readable format
    # when a line is empty quit loop
    
    #open the file in read
    contact_file = open('contacts.txt', 'r')
        
    #prime loop
    name = contact_file.readline()
    address = contact_file.readline()
    number = contact_file.readline()
    email = contact_file.readline()
    
    #loop to read each line
    while name != '' or address != '' or number != '' or email != '':
        
        #strip new line
        name = name.rstrip('\n')
        address = address.rstrip('\n')
        number = number.rstrip('\n')
        email = email.rstrip('\n')
        
        #print all in readable format
        print("Name:", name)
        print("Address:", address)
        print("Phone Number:", number)
        print("Email:", email)
        
        #ends loop if empty
        name = contact_file.readline()
        address = contact_file.readline()
        number = contact_file.readline()
        email = contact_file.readline()
        
    contact_file.close()

contact_manager()
