import csv        # This line imports the `csv` module. This module provides functions for reading and writing CSV files.
contact = {}

def save_contact(contact, filename):        # This line defines a dictionary called `contact`. This dictionary will store the contact list.
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        for name, phone in contact.items():
            writer.writerow([name, phone])


def display_contact():        # This function saves the contact list to a CSV file. The file is named `filename`.
    print("\nName\tContact Number: ""\n")
    with open('S:\Contact.csv', 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        if reader:
            for row in reader:
                print("{}  {}".format(row[0], row[1]))
        else:
            print("\n\t\t\t The file is empty!")


def edit_contact(contact, del_contact):        # This function displays the contact list. The contact list is read from the CSV file `S:\Contact.csv`.
    if del_contact in contact:
        phone = int(input("\nEnter a New Number: "))
        contact[del_contact] = phone
        save_contact(contact, 'S:\Contact.csv')
        print("\n\t\t\tContact Updated")
        display_contact()
    else:
        print("\n\t\t\tName not found in contact!!")


# This function edits a contact in the contact list. The contact name is `del_contact`.
# The new phone number is entered by the user. The contact list is then updated and saved to the CSV file. 


def delete_contact(contact, del_contact):        
    if del_contact in contact:
        contact.pop(del_contact)
        save_contact(contact, 'S:\Contact.csv')
        print("\n\t\t\tcontact deleted Successfully")
    else:
        print("\n\t\t\tName not found in contact!!")



while True:        # This function deletes a contact from the contact list. The contact name is `del_contact`. The contact list is then updated and saved to the CSV file.
    print("\n------------------------------------------------------------\n")
    choice = int(input(" 1. Add New Contact \n 2. Search Contact \n 3. Display Contact \n 4. Edit Contact \n 5. Delete Contact \n 6. Exit \n\n Enter your option: "))


# This while loop allows the user to interact with the program. The user can choose to add a new contact, search for a contact, display the contact list, edit a contact,
# delete a contact, or exit the program.


    if choice == 1:
        print("\n------------------------------------------------------------\n")
        name = input("Enter the Contact Name: ")
        phone = int(input("Enter the Number: "))
        if len(str(phone)) == 10:
            contact[name] = phone
            save_contact(contact, 'S:\Contact.csv')
            print("\n\t\t\tNumber Added Successfully\n")
        else:
            print("\nEnter 10 Digit Number")
            

    elif choice ==2:
        print("\n------------------------------------------------------------\n")
        search_name = input("Enter the Contact Name: ")
        print()
        if search_name in contact:
            print(search_name," Contact number is ",contact[search_name])
            print()
        else:
            print("\nName not found!\n")
            
            
    elif choice == 3:
        print("\n------------------------------------------------------------\n")
        display_contact()
        
            
    elif choice == 4:
        print()
        print("\n------------------------------------------------------------\n")
        edit_contact(contact, input("Enter the Contact Name to Edit: "))
        
            
    elif choice == 5:
        print()
        print("\n------------------------------------------------------------\n")
        delete_contact(contact, input("Enter the conact Name to Delete: "))

            
    else:
        break
