def search_contact(book_list):
    search = input("Enter the name or phone number to search: ")

    found_contacts = []
    for contact in book_list:
        if search.lower() in contact['name'].lower() or search in contact['phone_number']:
            found_contacts.append(contact)

    if found_contacts:
        print(f"{'Name':<20} {'Phone Number':<15} {'Gmail':<20} {'Address':<25}")
        print("=" * 80)
        for contact in found_contacts:
            print(f"{contact['name']:<20} {contact['phone_number']:<15} {contact['gmail']:<20} {contact['address']:<25}")
            print("=" * 80)
    else:
        print(f"No contacts found '{search}'.")
