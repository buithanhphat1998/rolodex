"""CECS 277 Classes & Objects
09/24/2025
Group 4
Student 1: Thanh Phat Bui
Student 2: Ha Gia Bao Hoang
Description:
Rolodex
Create a program that allows the user to view, search, and modify a contact list made up of
contact objects. A contact has a name, phone number, address, city, and zip code. Contacts are
initially read in from the file ‘addresses.txt’ and then are written back to the file when the
program ends."""

# import the Contact class and check_input module
from contact import Contact
import check_input

def write_file(contacts):
    """
    INPUT:
        - global 'contacts'
    OUTPUT:
        - writes to 'contacts.txt'
    """
    with open("addresses.txt", 'w') as file:
        for contact in contacts:
            # write in file
            file.write(repr(contact))
def read_file():
    """
    INPUT:
        - reads from file
    OUTPUT:
        - populates to global 'contacts' list
    """
    contacts = []
    # open the file
    with open("addresses.txt") as file:
        # remove newline and split by commas into 6 pieces
        line = file.readline()
        while len(line): 
            contactInfo = line.split(',')
            contact = Contact(contactInfo[0], contactInfo[1], contactInfo[2], contactInfo[3], contactInfo[4], contactInfo[5].strip())
            contacts.append(contact)
            line = file.readline()
    #sort    
    contacts.sort()
    return contacts
def modify_contact(cont):
    """
    INPUT:
        cont (contact): the contact object to modify
    OUTPUT:
        updates 'cont' fields and writes to file after each edit
    """
    # display modify menu
    print("Modify Menu")
    print("1. First name")
    print("2. Last name")
    print("3. Phone")
    print("4. Address")
    print("5. City")
    print("6. Zip")
    print("7. Save")
    print("> ", end='')
    match check_input.get_int_range("",1,7):
        #handle choice with match case 

        #apply changes
        case 1: 
            print("First Name: ",end='')
            cont.f_name = input()
        case 2: 
            print("Last Name: ",end='')
            cont.l_name = input()
        case 3: 
            print("Phone #: ",end='')
            cont.phone = input()
        case 4: 
            print("Address: ",end='')
            cont.address = input()
        case 5: 
            print("City: ",end='')
            cont.city = input()
        case 6: 
            print("Zip: ",end='')
            cont.zip = input()      
        case 7:
            return


def get_menu_choice():
    """
    INPUT:
        reads from userinput
    OUTPUT:
        option 1–5 
    """
    #Main Menu
    print("-Rodolex Menu-")
    print("1. Display Contacts")
    print("2. Add Contact")
    print("3. Search Contacts")
    print("4. Modify Contact")
    print("5. Save and Quit")
    # user's choice
    option = check_input.get_int_range("> ",1,5)
    return option


def main():
    # load data
    contacts = read_file()
    while True: 
        # show menu and get choice
        match get_menu_choice():
            case 1: 
                # display contacts
                for index in range(len(contacts)):
                    # print each contact
                    print(index + 1, end='.')
                    print(contacts[index], end ='')
                    print()
            case 2: 
                # add a new contact
                print("Enter new contact")
                # get user new contact fields from user
                print("First Name: ",end='')
                f_name = input()
                print("Last Name: ",end='')
                l_name = input()
                print("Phone #: ",end='')
                phone = input()
                print("Address: ",end='')
                address = input()
                print("City: ",end='')
                city = input()
                print("Zip: ",end='')
                zip = input()
                
                # create new contact object and add to lis
                contacts.append(Contact(f_name, l_name, phone,address,city, zip))
                contacts.sort()
            case 3: 
                #search
                # sub-menu
                print("1. Search by last name")
                print("2. Search by zip")
                option = check_input.get_int_range("> ", 1,2)
                found = False
                match option:
                    case 1: 
                        # search option by last name
                        print("Enter last name: ", end='')
                        last_name = input()
                        for contact in contacts:
                            if(last_name == contact.l_name):
                                print(contact)
                                found = True
                    case 2: 
                        # search option by zip code
                        print("Enter zip code: ", end='')
                        zip = input()
                        for contact in contacts:
                            if(zip == contact.zip):
                                print(contact)
                                found = True
                # report not found
                if(not found):
                    print("Contact Does Not Exist")
                        
            case 4:
                # modify a contact
                print("Enter first name: ", end='')
                first_name = input()
                print("Enter last name: ", end='')
                last_name = input()
                # to track found
                found = False
                for contact in contacts:
                    # found, modify contact
                    if(contact.f_name == first_name and contact.l_name == last_name):
                        print(contact)
                        modify_contact(contact)
                        found = True
                        break
                # report no contact matched
                if(not found):
                    print("Contact Does Not Exist")
            # exit
            case 5: 
                write_file(contacts)
                print("Saving File..")
                print("Ending Program")
                break

if __name__ == "__main__":
   main()
    
