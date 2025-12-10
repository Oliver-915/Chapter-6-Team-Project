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
            
    
def contact_edit():
    pass 
    
def contact_delete():
    pass 
    
def contact_display():
    pass