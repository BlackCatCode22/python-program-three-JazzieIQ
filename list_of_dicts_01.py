# list_of_dicts_01.py
# Dennis Mohle, 10 Sep 23
#
# Sample code snippets for Python Program Three


# Create a dictionary.

my_dict = {"name": "Dennis Mohle", "phone": "559-321-1234", "email": "dmohle@gmail.com" }
print(type(my_dict))
print("\n\n")
for key, value in my_dict.items():
    print(f"{key}: {value}")
print("\n\n")

# Create a list of dict objects.

my_list_of_contacts = []
my_list_of_contacts.append(my_dict)
print("\n")
print(my_list_of_contacts)

# do this again for a second contact

# Create a dictionary.
# my_dict = {"name": "YourNameHere"}
my_dict = {"name": "Donald Duck", "phone": "559-308-1234", "email": "donduck@gmail.com" }
print(type(my_dict))
print("\n\n")
for key, value in my_dict.items():
    print(f"{key}: {value}")
print("\n\n")

# Create a list of dict objects.
# my_list_of_contacts = []
my_list_of_contacts.append(my_dict)
print("\n")
print(my_list_of_contacts)

# Create a third contact and append to the list
my_third_contact = {"name": "Minnie Mouse", "phone": "702-638-8388", "email": "minniem@gmail.com"}
# Output the newly created dictionary...
print("\n\n")
for key, value in my_third_contact.items():
    print(f"{key}: {value}")
print("\n\n")
# append the third contact to the list
my_list_of_contacts.append(my_third_contact)


# Iterate through the list and print key-value pairs for each dictionary
for my_dict in my_list_of_contacts:
    for key, value in my_dict.items():
        print(f"{key}: {value}")
    print()  # Print an empty line to separate the dictionaries











