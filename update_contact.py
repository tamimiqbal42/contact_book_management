from save_data import save_contacts_to_file

def update_contact(book_list):
    contact_info = input("Enter the Phone Number or Gmail of the contact to update: ")

    contact_to_update = None
    if contact_info.isdigit():
        for contact in book_list:
            if contact['phone_number'] == contact_info:
                contact_to_update = contact
                break
    else:
        for contact in book_list:
            if contact['gmail'] == contact_info:
                contact_to_update = contact
                break

    if contact_to_update:
        print(f"Found contact: {contact_to_update['name']}")

        while True:
            new_name = input(f"Enter new name (current: {contact_to_update['name']}): ")
            contact_to_update['name'] = new_name
            new_phone_number = input(f"Enter new phone number (current: {contact_to_update['phone_number']}): ")
            if new_phone_number.isdigit():
                for contact in book_list:
                    if contact['phone_number'] == new_phone_number:
                        print(f"Error: The phone number {new_phone_number} is already in use.")
                        break
                else:
                    contact_to_update['phone_number'] = new_phone_number
                    break
            else:
                print("Error: Phone number must be numeric.")

        new_gmail = input(f"Enter new Gmail (current: {contact_to_update['gmail']}): ")
        for contact in book_list:
            if contact['gmail'] == new_gmail:
                print(f"Error: The phone number {new_gmail} is already in use.")
                break
            else:
                contact_to_update['gmail'] = new_gmail
                break
        
        new_address = input(f"Enter new address (current: {contact_to_update['address']}): ")
        contact_to_update['address'] = new_address

        save_contacts_to_file(book_list)
        print("Contact updated successfully.")
    else:
        print(f"Error: Contact with {contact_info} not found.")
