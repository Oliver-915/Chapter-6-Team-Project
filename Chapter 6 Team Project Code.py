def contact_manager():
    contact_menu()
    
def contact_menu():
    pass
    
def contact_add():
    pass
    
def contact_search():
    # main accepts no arguments
    # asks for a string
    # looks for the string in contacts.txt + verification
    # loop 2-3 if not found
    # if found, return entire contact and ask the user to confirm.
    
    # prime loop
    choice = "0"
    
    
    #loop while choice is unconfirmed
    while choice.lower() != "1":
        #get input
        search = str(input("Enter a name to look up contacts for (1 to quit): "))
        
        #set search status
        found = False
        
        #open the file in read
        contact_file = open('contacts.txt', 'r')
        
        #loop to read each line
        while info != '' or found != True:
            name = contact_file.readline()
            address = contact_file.readline()
            number = contact_file.readline()
            email = contact_file.readline()
            
            #strip new line
            name = name.rstrip('\n')
            address = address.rstrip('\n')
            number = number.rstrip('\n')
            email = email.rstrip('\n')
            
            if name.lower() == search.lower():
                print("\nContact Found\n")
                print("Name:", name)
                print("Address:", address)
                print("Phone Number:", number)
                print("Email:", email)
                found = True
                
        coffee_file.close()
        
        #search status = false
        if not found:
            print("\nNo Contact Found.\n")
        
        #confirm
        while found = True:
            confirm = input(str("\nIs this what you wanted? (y/n): "))
            if confirm == "y":
                choice = "1"
                found = False
                print("\nContact Confirmed\n")
                return name, address, number, email
            elif confirm == "n":
                found = False
                confirm = input(str("Try again? (y/n): "))
                if confirm == "y":
                    print("Reseting\n")
                elif confirm == "n":
                    choice = "1"
                else:
                    print("Input Error, Try again")
            else:
                print("Input Error, Try again")
        
            
    
def contact_edit():
    pass 
    
def contact_delete():
    pass 
    
def contact_display():
    pass