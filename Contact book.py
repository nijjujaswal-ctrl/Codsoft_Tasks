# Contact Management System

contacts = []


# Add Contact
def add_contact():
    print("\n========== ADD CONTACT ==========")

    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }

    contacts.append(contact)

    print("\nContact added successfully!")


# View Contacts
def view_contacts():
    print("\n========== CONTACT LIST ==========")

    if not contacts:
        print("No contacts found.")
        return

    for i, contact in enumerate(contacts, start=1):
        print(f"\nContact {i}")
        print("Name    :", contact["name"])
        print("Phone   :", contact["phone"])
        print("Email   :", contact["email"])
        print("Address :", contact["address"])


# Search Contact
def search_contact():
    print("\n========== SEARCH CONTACT ==========")

    search = input("Enter name or phone number: ").lower()

    found = False

    for contact in contacts:
        if (search in contact["name"].lower() or
                search in contact["phone"]):

            print("\nContact Found!")
            print("Name    :", contact["name"])
            print("Phone   :", contact["phone"])
            print("Email   :", contact["email"])
            print("Address :", contact["address"])

            found = True

    if not found:
        print("\nContact not found.")


# Update Contact
def update_contact():
    print("\n========== UPDATE CONTACT ==========")

    name = input("Enter the name of the contact to update: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:

            print("\nLeave blank if you don't want to change a detail.")

            new_name = input(f"Enter new name ({contact['name']}): ")
            new_phone = input(f"Enter new phone ({contact['phone']}): ")
            new_email = input(f"Enter new email ({contact['email']}): ")
            new_address = input(f"Enter new address ({contact['address']}): ")

            if new_name:
                contact["name"] = new_name

            if new_phone:
                contact["phone"] = new_phone

            if new_email:
                contact["email"] = new_email

            if new_address:
                contact["address"] = new_address

            print("\nContact updated successfully!")
            return

    print("\nContact not found.")


# Delete Contact
def delete_contact():
    print("\n========== DELETE CONTACT ==========")

    name = input("Enter the name of the contact to delete: ").lower()

    for contact in contacts:
        if contact["name"].lower() == name:

            contacts.remove(contact)

            print("\nContact deleted successfully!")
            return

    print("\nContact not found.")


# Main Menu
while True:

    print("\n======================================")
    print("       CONTACT MANAGEMENT SYSTEM")
    print("======================================")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("======================================")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("\nThank you for using Contact Management System!")
        break

    else:
        print("\nInvalid choice! Please select 1-6.")
