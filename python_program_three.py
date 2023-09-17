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
        manager = input("Are you here to manage the contact cards? Y/N: ").upper()
        if manager[0] == "N":
            print("\nNon-manager access allows you to review the current list without changing it and receive a text "
                  "copy.")
            confirm_reset = input("\nWould you like to restart menu? Y/N: ").lower()
            if confirm_reset[0] == "y":
                user_menu()
            else:
                print("\nHere is the current list:\n")
                print(type(contacts))
                print(contacts)
                print("\nThank You for accessing Mac Mac's List and Dictionary Program.")
                restart_script = input("\nWould you like restart the program? "+'"Restart"/"End": ').lower()
                if restart_script[0] == "r":
                    script()
                else:
                    print("\nEnding Mac Mac's List and Dictionary Program.")
                    exit(1)
        if manager[0] == "Y":
            def admin_menu():
                password = input("Please enter password: ").lower()
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
                    contacts.append(card_mac_mac)
                    print("\n")
                    print(type(contacts))
                    print(contacts)
                    print("\n")
                    print("****Disclaimer****\nMac Mac's List and Dictionary Program is in limited alpha demo phase. "
                          "Multiple features are not available. This is not a permanent directory. Please input your "
                          "contact card info in the following prompt.")
                    manage_input = input()
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