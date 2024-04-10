import json

# Function to load contacts from file
def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Function to save contacts to file
def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file)

# Function to add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    save_contacts(contacts)
    print(f"Contact '{name}' added successfully!")

# Function to remove a contact
def remove_contact(contacts):
    view_contacts(contacts)
    if contacts:
        try:
            index = int(input("Enter contact number to remove: ")) - 1
            if 0 <= index < len(contacts):
                removed_contact = contacts.pop(index)
                save_contacts(contacts)
                print(f"Contact '{removed_contact['name']}' removed successfully!")
            else:
                print("Invalid contact number!")
        except ValueError:
            print("Invalid input!")
    else:
        print("No contacts currently.")

# Function to view all contacts
def view_contacts(contacts):
    if contacts:
        print("Contacts:")
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']} | Phone: {contact['phone']} | Email: {contact['email']}")
    else:
        print("No contacts currently.")

# Function to search contacts
def search_contact(contacts):
    search_term = input("Enter search term: ").lower()
    search_results = [contact for contact in contacts if search_term in contact['name'].lower() or 
                                                            search_term in contact['phone'] or 
                                                            search_term in contact['email'].lower()]
    if search_results:
        print("Search Results:")
        for i, result in enumerate(search_results, start=1):
            print(f"{i}. Name: {result['name']} | Phone: {result['phone']} | Email: {result['email']}")
    else:
        print("No matching contacts found.")

def main():
    contacts = load_contacts()

    while True:
        print("\nWelcome to the Contact List Manager!\n")
        print("1. Add Contact")
        print("2. Remove Contact")
        print("3. View Contacts")
        print("4. Search Contact")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            remove_contact(contacts)
        elif choice == "3":
            view_contacts(contacts)
        elif choice == "4":
            search_contact(contacts)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
