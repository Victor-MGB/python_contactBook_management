contact = {}

def main_menu():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. View All Contacts")
        print("6. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            update_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            view_contacts()
        elif choice == '6':
            print("Exiting contact book.")
            break
        else:
            print("Invalid choice. Please try again.")

def add_contact():
    name = input("Enter contact name: ")
    if name in contact:
        print("Contact already exists.")
    else:
        phone = input("Enter phone number: ")
        email = input("Enter email address: ")
        contact[name] = {"Phone": phone, "Email": email}
        print("Contact successfully added.")
        
def search_contact():
    name = input("Enter contact name to check details: ")
    if name in contact:
        print(f"Name: {name}")
        print(f"Phone: {contact[name]['Phone']}")
        print(f"Email: {contact[name]['Email']}")
    else:
        print("Contact not found.")
        
def update_contact():
    name = input("Enter contact name to update: ")
    if name in contact:
        phone = input("Enter new phone number: ")
        email = input("Enter new email address: ")
        contact[name] = {"Phone": phone, "Email": email}
        print("Contact updated successfully.")
    else:
        print("Contact not found.")
        
def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in contact:
        del contact[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")
        
def view_contacts():
    if contact:
        for name, info in contact.items():
            print(f"Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}")
    else:
        print("No contacts available.")

if __name__ == "__main__":
    main_menu()
