from contact import Contact
import check_input
def write_file(contacts):
    with open("addresses.txt", 'w') as file:
        for contact in contacts:
            file.write(repr(contact))
def read_file():
    contacts = []
    with open("addresses.txt") as file:
        line = file.readline()
        while len(line): 
            contactInfo = line.split(',')
            contact = Contact(contactInfo[0], contactInfo[1], contactInfo[2], contactInfo[3], contactInfo[4], contactInfo[5].strip())
            contacts.append(contact)
            line = file.readline()
            
    contacts.sort()
    return contacts
def get_menu_choice():
    print("-Rodolex Menu-")
    print("1. Display Contacts")
    print("2. Add Contact")
    print("3. Search Contacts")
    print("4. Modify Contact")
    print("5. Save and Quit")
    option = check_input.get_int_range("> ",1,5)
    return option


def main():
    contacts = read_file()
    while True: 
        match get_menu_choice():
            case 1: 
                for index in range(len(contacts)):
                    print(index + 1, end='.')
                    print(contacts[index], end ='')
                    print()
            case 2: 
                print("Enter new contact")
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

                contacts.append(Contact(f_name, l_name, phone,address,city, zip))
                contacts.sort()
            case 3: 
                print("1. Search by last name")
                print("2. Search by zip")
                option = check_input.get_int_range("> ", 1,2)
                found = False
                match option:
                    case 1: 
                        print("Enter last name: ", end='')
                        last_name = input()
                        for contact in contacts:
                            if(last_name == contact.l_name):
                                print(contact)
                                found = True
                    case 2: 
                        print("Enter zip code: ", end='')
                        zip = input()
                        for contact in contacts:
                            if(zip == contact.zip):
                                print(contact)
                                found = True
                if(not found):
                    print("Contact Does Not Exist")
                        

            case 5: 
                write_file(contacts)
                print("Saving File..")
                print("Ending Program")
                break

if __name__ == "__main__":
   main()
    