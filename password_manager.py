# This program allows you to add, view, and delete passwords stored in a file. 
# You will get a FileNotFoundError if you try to view the passwords and that file doesn't yet exist
# Currently trying to figure out write_key logic

from cryptography.fernet import Fernet

# TBD
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

# View all stored passwords
def view():
    # Open the passwords text file in read more
    with open("passwords.txt", "r") as f:
        
        for line in f.readlines():

            # retrieve the line
            data = line.rstrip()

            # split the username and password with |
            user, pwd = data.split("|")

            # Display this username and password
            print("User: ", user, "| Password: ", pwd)


# Add the new username & password combo to the passwords text file
def add():

    # Prompt for username and password from user
    name = input("Name: ")
    pwd = input("Password: ")
    
    # Open passwords file in 'append' mode
    with open("passwords.txt", "a") as f:

        # Write the username and password to the file
        f.write(name + "|" + pwd + "\n")

# Delete all passwords
def delete():

    # Deletes the contents of the file if it exists or creates an empty file and deletes it
    open("passwords.txt", "w").close()

# Master password providing access to viewing all passwords in the passwords file
master_pwd = input("What is your master password? ")

# Prompt the user for view, add, or quit
mode = input("Would you like to view your existing passwords or add a new one? You can also press q to quit. ")

# While loop controls primary logic of the application
# When a user chooses the quit mode 'q', the application is terminated
while True:

    # Quit the application
    if mode == "q":
        break

    # View existing passwords
    if mode == "view":

        # Prompt the user for the master password
        master_user = input("What is the master password? ")

        if master_user == master_pwd:
            view()
        else:
            print("Invalid password. ")
    
    # Add a username & password combo
    elif mode == "add":
        add()

    # Delete all saved passwords
    elif mode == "delete":
        delete()
        print('Passwords have been deleted. ')

    # If an invalid input is entered, display this to the user
    else:
        print("Invalid response. ")
    
    # Prompt the user to choose their next action
    mode = input("Please enter 'view' to view passwords, 'add' to add a password, 'delete' to delete existing passwrods, or 'q' to quit. ")

print('Program is closing. ')