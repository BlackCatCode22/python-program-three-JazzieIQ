# Coder: Matthew Gutierrez
# # CIT 95 List and Dictionary Program

# program script

def script():
    # Intro
    print("\n\nWelcome to Mac Mac's List and Dictionary Program.\n")
    print("\nThis is a list of contact cards. User please enjoy.\n")

    # Variables: cards = dictionary and contacts = lists
    card = {"name": "Dennis Mohle", "phone": "559-321-1234", "email": "dmohle@gmail.com"}
    user_card = {"name": [], "phone": [], "email": []}
    contacts = []
    contacts.append(card)

    # user menu
    def user_menu():
        manager = input("User Menu --- Are you here to manage the contact cards? Y/N: ").upper()
        if manager[0] == "N":
            print("\nNon-manager access allows you to review the current list without changing it when you exit.")
            confirm_reset = input("\nWould you like to restart menu? Y/N: ").lower()
            if confirm_reset[0] == "y":
                user_menu()
            else:
                print("\nHere is the current list:\n")
                print(type(contacts))
                print(contacts)
                print("\nThank You for accessing Mac Mac's List and Dictionary Program.")
                restart_script = input("\nWould you like return to the user menu? "+'"Return"/"End": ').lower()
                if restart_script[0] == "r":
                    script()
                else:
                    print("\nEnding Mac Mac's List and Dictionary Program.")
                    exit(1)
        #view contacts
        if manager[0] == "Y":

            def admin_menu():
                password = input("Admin Menu --- Please enter password: ").lower()
                if password == "admin":
                    print("\nThank You, Admin. Menu will move to contact cards.\nThe following shows contact card "
                          "information:\n")
                    print(type(card))
                    for key, value in user_card.items():
                        print(f"{key}: {value}")
                    print("\nThe following shows the list of current contact cards:\n\n")
                    print(contacts)
                    print("\nMac Mac's program will test user accessibility.\nHere is Mac Mac's card: \n")
                    card_mac_mac = {"name": "Mac Mac", "phone": "559-365-8702", "email": "bongo90g@yahoo.com"}
                    print(card_mac_mac)

                    # Adding Mac Mac's card to the list...
                    mac_mac_exists = any(card == card_mac_mac for card in contacts)
                    if not mac_mac_exists:
                        contacts.append(card_mac_mac)
                    else:
                        print("\nMac Mac's card already exists in the list. Not adding a duplicate.")

                    print("\n")
                    print(type(contacts))
                    print(contacts)
                    print("\n")
                    print("****Disclaimer****\nMac Mac's List and Dictionary Program is in limited alpha demo phase. "
                          "This is not a permanent directory. Please input your contact card info in the following "
                          "prompt.")
                    def manage():
                        # search function
                        def user_search():
                            print("\n")
                            print(contacts)
                            search_input = input(
                                "\nSearch by Name: ").lower()  # Convert input to lowercase for case-insensitive search
                            print('\nYou are searching for "' + search_input + '".')
                            found_cards = []

                            for card in contacts:
                                if isinstance(card['name'], list):
                                    # Join the elements of the list and convert to lowercase for comparison
                                    card_name = ' '.join(card['name']).lower()
                                else:
                                    card_name = card['name'].lower()

                                if search_input in card_name:  # Partial match check
                                    found_cards.append(card)

                            if found_cards:
                                print("\nYour search query found the following card(s):")
                                for card in found_cards:
                                    print(card)
                            else:
                                print("\nNo matching cards found.")

                            search_redo1 = input('\nDo you have another card name you wish to search or '
                                                 'return to manage menu? "Ok"/"EXIt": ').lower()
                            if search_redo1.startswith("o"):
                                user_search()
                            else:
                                print("\nReturning to manage menu.\n")
                                manage()
                        # user_input function
                        def user_input():
                            print("\nExcellent. Please follow prompts.")
                            user_name = input('\nPlease enter your first and last name as "XXXX XXXXXX"": ')
                            if "name" in user_card:
                                user_card["name"].append(user_name)
                                print('\nThe card name will be "' + user_name + '".')
                            user_phone = input('\nPlease enter your desired phone number as "XXX-XXX-XXXX": ')
                            if "phone" in user_card:
                                user_card["phone"].append(user_phone)
                                print('\nThe card phone number will be "' + str(user_phone) + '".')
                            user_email = input('\nPlease enter your desired email as "XXXXX@domain.com": ')
                            if "email" in user_card:
                                user_card["email"].append(user_email)
                                print('\nThe card email will be "' + user_email + '".')
                            print("\nPrinting user card input...\n")
                            print(user_card)
                            contacts.append(user_card)
                            print("\n")
                            print(type(contacts))
                            print(contacts)
                            return
                        #Contact Card Management
                        manage_input = input("\nChoose Admin task from the following menu. " + 'Enter "1" to perform '
                                                                                              'individual card '
                                                                                              'search. / Enter "2" to '
                                                                                              'provide input. / Enter '
                                                                                              '"0" to cancel admin '
                                                                                              'access: ')
                        if manage_input == "1":
                            user_search()
                        if manage_input == "2":
                            user_input()
                            print("\nThank you for testing Mac Mac's List and Dictionary Program. To interact with "
                                  "this list again revisit the user menu or follow prompt.")
                            def added_contact_return():
                                user_menu_return = input('\nReturn to menu? "user menu"/"manage"/"end program": ').lower()
                                if user_menu_return[0] == "u":
                                    print("\n\nReturning to user menu.")
                                    user_menu()
                                if user_menu_return[0] == "m":
                                    print("\nAdmin Manage Menu")
                                    manage()
                                if user_menu_return[0] == "e":
                                    print('\nYou chose program termination. ')
                                    user_confirm_end = input('\nIs this correct? "Terminate" / "Return( to previous '
                                                             'Menu): ').upper()
                                    #print(user_confirm_end[0])
                                    if user_confirm_end[0] == "T" or user_confirm_end == "Y":
                                        #print(user_confirm_end == "T" or "Y")
                                        print("\nMac Mac's program thanks you, goodbye.")
                                        exit(1)
                                    elif user_confirm_end[0] == "R" or user_confirm_end == "N":
                                        #print(user_confirm_end == "R" or "N")
                                        added_contact_return()
                                    else:
                                        print("\nI'm sorry what was that? Returning to previous menu: ")
                                        added_contact_return()
                                else:
                                    print("\nUser command not clear repeating query.")
                                    added_contact_return()
                            added_contact_return()
                        if manage_input == "0":
                            print("\nAdmin access cancelled.")
                            admin_menu()
                        if manage_input != "1" or "2" or "0":
                            print("Admin Command was not understood. Please type new command: ")
                            manage()
                    manage()
                else:
                    print("Password input was not understood.\n")
                    retype_password = input("Would you like to retype password:" + ' "Yes"/"No": ').lower()
                    if retype_password[0] == "y":
                        admin_menu()
                    else:
                        print("User password entry failure confirmed non-manager status...\n...returning to user menu.")
                        user_menu()
            admin_menu()
        else:
            print ("\nUser input was not understood. Please wait for menu reset.")
            user_menu()
    user_menu()
script()

"""
                    def manage():
                        # search function
                        def user_search():
                            print("\n")
                            print(contacts)
                            search_input = input(
                                "\nSearch by Name: ").lower()  # Convert input to lowercase for case-insensitive search
                            print('\nYou are searching for "' + search_input + '".')

                            found_cards = []

                            for card in contacts:
                                for key in card:
                                    # Convert the card's name to lowercase for case-insensitive comparison
                                    card_name = card['name'].lower()
                                    if search_input in card_name:  # Partial match check
                                        found_cards.append(card)

                            if found_cards:
                                print("\nYour search query found the following card(s):")
                                for card in found_cards:
                                    print(card)
                            else:
                                print("\nNo matching cards found.")

                            search_redo1 = input('\nDo you have another card name you wish to search or '
                                                 'return to user menu? "Ok"/"EXIt": ').lower()
                            if search_redo1.startswith("o"):
                                user_search()
                            else:
                                print("\nReturning to user menu.\n")
                                user_menu()
                            if card['name'] != search_input:
                                        print("\nYour query input has no results.")
                                        search_redo2 = input('\nDo you have another card name you wish to search, '
                                                             'return to admin manage, or to user menu? '
                                                             '"Ok"/"return"/"EXIt": ').upper()
                                        if search_redo2[0] == "O":
                                            user_search()
                                        if search_redo2[0] == "r":
                                            manage()
                                        else:
                                            print("Returning to user menu.")
                                            user_menu()

                        # search function
                        def user_search():
                            print("\n")
                            print(contacts)
                            search_input = input("\nSearch by Name: ")
                            print('\nYou are searching for "' + search_input + '".')
                            for card in contacts:
                                for key in card:
                                    print(card[key])
                                    print(card[key] == search_input)
                                    while card['name'] == search_input:
                                        search_result = card
                                        print("\nYour search query found a card for " + search_input)
                                        print(search_result)
                                        search_redo1 = input('\nDo you have another card name you wish to search or '
                                                             'return to user menu? "Ok"/"EXIt": ').upper()
                                        if search_redo1[0] == "O":
                                            user_search()
                                        else:
                                            print("Returning to user menu.")
                                            user_menu()
            def admin_menu():
                password = input("Admin Menu --- Please enter password: ").lower()
                if password == "admin":
                    print("\nThank You, Admin. Menu will move to contact cards.\nThe following shows contact card "
                          "information:\n")
                    print(type(card))
                    for key, value in user_card.items():
                        print(f"{key}: {value}")
                    print("\nThe following shows the list of current contact cards:\n\n")
                    print(contacts)
                    print("\nMac Mac's program will test user accessibility.\nHere is Mac Mac's card: \n")
                    card_mac_mac = {"name": "Mac Mac", "phone": "559-365-8702", "email": "bongo90g@yahoo.com"}
                    print(card_mac_mac)
                    print("\nAdding Mac Mac's card to the list... \n")
                    contacts.append(card_mac_mac)
                    print("\n")
                    print(type(contacts))
                    print(contacts)
                    print("\n")
                    print("****Disclaimer****\nMac Mac's List and Dictionary Program is in limited alpha demo phase. "
                          "This is not a permanent directory. Please input your contact card info in the following "
                          "prompt.")

def admin_menu():
            # global user_search
            password = input("Admin Menu --- Please enter password: ").lower()
            if password == "admin":
                print("\nThank You, Admin. Menu will move to contact cards.\nThe following shows contact card "
                      "information:\n")
                print(type(card))
                for key, value in user_card.items():
                    print(f"{key}: {value}")
                print("\nThe following shows the list of current contact cards:\n\n")
                print(contacts)
                for card in contacts:
                    for key in card:
                        if card[key] != "Mac Mac":
                            print("\nMac Mac's program will test user accessibility.\nHere is Mac Mac's card: \n")
                            card_mac_mac = {"name": "Mac Mac", "phone": "559-365-8702", "email": "bongo90g@yahoo.com"}
                            print(card_mac_mac)
                            print("\nAdding Mac Mac's card to the list... \n")
                            contacts.append(card_mac_mac)
                print("\n")
                print(type(contacts))
                print(contacts)
                print("\n")
                print("****Disclaimer****\nMac Mac's List and Dictionary Program is in limited alpha demo phase. "
                      "This is not a permanent directory. Please input your contact card info in the following "
                      "prompt.")
                      """