#3) Contact Book

contacts = {}

#Adding a contact
def add_contact():
    name = input("Enter the name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    print("Contact added successfully!\n")

#Viewing all the contacts
def view_contacts():
    if not contacts:
        print("No contacts found.\n")
    else:
        print("\n Contact List:")
        for name, info in contacts.items():
                print(f"{name} - {info['Phone']}")
        print()

#Searching a contact
def search_contact():
    search = input("Enter name/phone no: ")
    found = False
    for name, info in contacts.items():
        if search.lower() in name.lower() or search == info["Phone"]:
            print(f"\nFound Contact:\nName: {name}\nPhone: {info['Phone']}\nEmail: {info['Email']}\nAddress: {info['Address']}\n")
            found = True
            break
    if not found:
        print("Contact not found.\n")

#Updating a contact
def update_contact():
    name = input("Enter the name of the contact which you want to update:")
    if name in contacts:
        print("The new details are:")
        phone = input(f"New phone number (current: {contacts[name]['phone']}):") or contacts[name]['phone']
        email = input(f"New email (current: {contacts[name]['Email']}):") or contacts[name]['Email']
        address = input(f"New address (current: {contacts[name]['Address']}):") or contacts[name]['Address']
        contacts[name] = {
            "phone": phone,
            "Email": email,
            "Address": address
       }
        print("Contact updated successfully!\n")
        
    else:
        print("Contact not found.\n")

#Deleting a contact
def delete_contact():
    name = input("Enter the name of the contact which you wanna delete:")
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully:")
    else:
        print("Contact not found.\n")

def main():
    while True:
        print("Contact Book")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice from(1->6):")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exit made. Bye!")
            break
        else:
            print("Invalid choice. Try again.\n")
main()
            





























