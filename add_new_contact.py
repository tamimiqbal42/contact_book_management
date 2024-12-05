from save_data import save_contacts_to_file

def add_contact(book_list):
    name = input('Enter Name: ')

    phone_number = input('Enter Phone Number: ')
    if not phone_number.isdigit():
        print("Error: Please enter a valid number.")
        return
    
    for contact in book_list:
        if contact['phone_number'] == phone_number:
            print(f"Error: The phone number {phone_number} is already assigned.")
            return
    
    gmail = input('Enter Gmail: ')
    for contact in book_list:
        if contact['gmail'] == gmail:
            print(f"Error: The Gmail {gmail} is already assigned.")
            return
    
    address = input('Enter Address: ')

    new_contact = {
        'name': name,
        'phone_number': phone_number,
        'gmail': gmail,
        'address': address,
    }

    book_list.append(new_contact)
    
    save_contacts_to_file(book_list)

    print('Contact added successfully.')
