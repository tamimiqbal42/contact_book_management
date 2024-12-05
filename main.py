import csv
from save_data import load_books
from add_new_contact import add_contact
from view_all_data import view_all_contacts
from remove_contact import delete_contact
from update_contact import update_contact
from search_contact import search_contact

book_list = load_books()

while True:
    print("\n --- Welcome to Contact Book Management System ---")
    print('0. Exit Program.')
    print('1. Add Contact.')
    print('2. View Contacts.')
    print('3. Update Contact.')
    print('4. Remove Contact.')
    print('5. Search Contact by Name or Phone Number.')

    enter_choice = input('Enter Your Choice: ')

    if enter_choice == '0':
        print('Thanks for use the program.')
        break
    
    elif enter_choice == '1':
        add_contact(book_list)
        
    elif enter_choice == '2':
        view_all_contacts(book_list)
        
    elif enter_choice == '3':
        update_contact(book_list)
        
    elif enter_choice == '4':
        delete_contact(book_list)
        
    elif enter_choice == '5':
        search_contact(book_list)
        
    else:
        print('Invalid Choice.')
