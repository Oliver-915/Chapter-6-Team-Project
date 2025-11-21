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
    if menu_selection == 1:
        print("\nSelected Option: Add Contact\n")
        contact_add()
    if menu_selection == 2:
        print("\nSelected Option: Search Contact\n")
        contact_search()
    if menu_selection == 3:
        print("\nSelected Option: Edit Contact\n")
        contact_edit()
    if menu_selection == 4:
        print("\nSelected Option: Delete Contact\n")
        contact_delete()
    if menu_selection == 5:
        print("\nSelected Option: Display All Contacts\n")
        contact_display()
    if menu_selection == 6:
        print("\nSelected Option: Exit\n")
        exit()
    
    
    
def contact_add():
    #accepts no arguments
    #adds a contact to the list
    print("Add contacts here. Input nothing if you do not have anything to put.")
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
    #accepts no arguments
    #searches a contact from the list
    #displays info
    print("Type the name below of the contact you would like to view")
    search_request = input("Name: ")
    try:
        myfile = open("contacts.txt", "r")
        
        name = myfile.readline()
        
        while name != "" and found == False:
            address = myfile.readline()
            phone = myfile.readline()
            email = myfile.readline()
            
            nane = desc.restrip("\n")
            if name.lower() == search.lower(): # deterine if record is found
                print("\nRecord Found!")
                print("Name:", name)
                print("Address:", address)
                print("phone:", phone)
                print("email:", email)
                found = True
                
            # get the next description
            name = myfile.readline()
            
        myfile.close()
        
        
       
        if not found:
            print("\n The record was not found \n")
            
            
    except Exception as e:
        print("Error: Error reading file")
    

    
def contact_edit():
    pass 
    
def contact_delete():
    pass 
    
def contact_display():
    pass

def exit():
    #exit accepts no arguments
    #returns thank you message
    #ends the program
    print("Thank you for using Contact Manager")
def contact_manager():
    contact_menu()
    
def contact_menu():
    pass
    
def contact_add():
    pass
    
def contact_search():
    pass
    
def contact_edit():
    pass 
    
def contact_delete():
    pass 
    
def contact_display():
    pass
