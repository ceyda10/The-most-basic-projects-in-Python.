from phone_class import PhoneBook
pb = PhoneBook()
while True:
    print("\n--- PHONEBOOK MENU ---")
    print("1. Add Contact")
    print("2. List Contacts")
    print("3. Delete  Contact")
    print("4. Exit")
    choice = input("Enter Your Choice (1-4): ")
    if choice == "1":
        first_name = input("Enter name:")
        last_name = input("Enter last name: ")
        phone = input("Enter phone number: ")
        pb.add_contact(first_name, last_name, phone)
    elif choice == "2":
        pb.list_contact()
    elif choice == "3":
        name = input("Enter name to delete: ")
        pb.delete_contact(name)
    elif choice == "4":
        print("Exiting the program...")
        break
    else:
        print("Invalid choice. Please try again.")
        