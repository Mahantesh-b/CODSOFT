"""Contact Book - CODSOFT Python Internship Project."""

import json
from pathlib import Path

DATA_FILE = Path("contacts.json")


def load_contacts():
    """Load contacts from JSON storage."""
    if not DATA_FILE.exists():
        return {}

    try:
        return json.loads(DATA_FILE.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        print("Could not read contacts file. Starting with an empty contact book.")
        return {}


def save_contacts(contacts):
    """Save contacts to JSON storage."""
    DATA_FILE.write_text(
        json.dumps(contacts, indent=4),
        encoding="utf-8",
    )


def display_contact(name, contact):
    """Display one contact in a readable format."""
    print(f"\nName: {name}")
    print(f"Phone: {contact['phone']}")
    print(f"Email: {contact['email']}")
    print(f"Address: {contact['address']}")


def add_contact(contacts):
    name = input("Enter name: ").strip()

    if not name:
        print("Name cannot be empty.")
        return

    if name.lower() in {key.lower() for key in contacts}:
        print("A contact with this name already exists.")
        return

    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()
    address = input("Enter address: ").strip()

    contacts[name] = {
        "phone": phone,
        "email": email,
        "address": address,
    }
    save_contacts(contacts)
    print("Contact added successfully.")


def view_contacts(contacts):
    if not contacts:
        print("No contacts saved.")
        return

    print("\n=== Contact List ===")
    for name in sorted(contacts):
        display_contact(name, contacts[name])


def search_contact(contacts):
    query = input("Enter name or phone number to search: ").strip().lower()

    matches = [
        (name, contact)
        for name, contact in contacts.items()
        if query in name.lower() or query in contact["phone"].lower()
    ]

    if not matches:
        print("No matching contact found.")
        return

    for name, contact in matches:
        display_contact(name, contact)


def update_contact(contacts):
    name = input("Enter the contact name to update: ").strip()

    actual_name = next((key for key in contacts if key.lower() == name.lower()), None)

    if actual_name is None:
        print("Contact not found.")
        return

    contact = contacts[actual_name]
    print("Press Enter to keep the existing value.")

    phone = input(f"Phone [{contact['phone']}]: ").strip()
    email = input(f"Email [{contact['email']}]: ").strip()
    address = input(f"Address [{contact['address']}]: ").strip()

    if phone:
        contact["phone"] = phone
    if email:
        contact["email"] = email
    if address:
        contact["address"] = address

    save_contacts(contacts)
    print("Contact updated successfully.")


def delete_contact(contacts):
    name = input("Enter the contact name to delete: ").strip()
    actual_name = next((key for key in contacts if key.lower() == name.lower()), None)

    if actual_name is None:
        print("Contact not found.")
        return

    del contacts[actual_name]
    save_contacts(contacts)
    print("Contact deleted successfully.")


def main():
    """Run the contact book application."""
    contacts = load_contacts()

    while True:
        print("\n=== Contact Book ===")
        print("1. View contacts")
        print("2. Add contact")
        print("3. Search contact")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            print("Thank you for using Contact Book!")
            break
        else:
            print("Invalid option. Please choose 1-6.")


if __name__ == "__main__":
    main()
