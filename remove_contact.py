from save_data import save_contacts_to_file

def delete_contact(book_list):
    contact_info = input("Enter the Phone Number or Gmail to remove: ")

    contact_found = None
    if contact_info.isdigit():
        for contact in book_list:
            if contact['phone_number'] == contact_info:
                contact_found = contact
                break
    else:
        for contact in book_list:
            if contact['gmail'] == contact_info:
                contact_found = contact
                break
    
    if contact_found:
        book_list.remove(contact_found)
        save_contacts_to_file(book_list)
        print(f"Contact with {contact_found['phone_number']} has been removed successfully.")
    else:
        print(f"Error: Contact with {contact_info} not found.")
