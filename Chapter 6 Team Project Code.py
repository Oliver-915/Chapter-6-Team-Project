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
    contact_file = open('contacts.txt', 'r')
    
    #loop while choice is unconfirmed
    while choice.lower() != "q":
        search = str(input("Enter a Name, Address, Phone Number, or Email Address (q to quit): "))
        
        
    
def contact_edit():
    pass 
    
def contact_delete():
    pass 
    
def contact_display():
    pass