contacts = {}

while True:
    print("\n1. Add contact")
    print("2. Search contact")
    print("3. Delete contact")
    print("4. List contacts")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
    elif choice == "2":
        name = input("Name to search: ")
        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found.")
    elif choice == "3":
        name = input("Name to delete: ")
        if name in contacts:
            del contacts[name]
            print("Deleted.")
        else:
            print("Contact not found.")
    elif choice == "4":
        for name, phone in contacts.items():
            print(name, "->", phone)
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
