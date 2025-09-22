from contact import Contact
import check_input
def write_file(contacts):
    with open("addresses.txt") as file:
        for contact in contacts:
            file.writelines(contact)
def read_file():
    contacts = []
    with open("addresses.txt") as file:
        line = file.readline()
        while len(line): 
            contacts.append(line.split(','))
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
    option = check_input.get_int_range("Option: ",1,5)
    return option


def main():
    contacts = read_file()
    while True: 
        match get_menu_choice():
            case 1: 
                for index in range(len(contacts)):
                    print(index, end=' ')
                    print(contacts[index])
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
            case 5: 
                write_file(contacts)
                break

if __name__ == "__main__":
   main()
    