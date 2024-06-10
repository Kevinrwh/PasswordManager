# This program allows you to add, view, and delete passwords stored in a file. 
# You will get a FileNotFoundError if you try to view the passwords and that file doesn't yet exist
# Currently trying to figure out write_key logic

from cryptography.fernet import Fernet

# Uncomment and run write_key() with load_key() commented out to create key file
'''# Define a key for us
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key()
'''

# Once running the program once to write the key, comment write_key out
# and run the rest of the program
def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

# View all stored passwords
def view():
    # Open the passwords text file in read more
    with open("passwords.txt", "r") as f:
        
        for line in f.readlines():

            # retrieve the line. rstrip removes carriage return
            data = line.rstrip()

            # split the username and password with |, assumes username and password do not have a |
            user, pwd = data.split("|")

            # Display this username and password
            print("User: ", user, "| Password: ", 
                  fer.decrypt(pwd.encode()).decode())


# Add the new username & password combo to the passwords text file
def add():

    # Prompt for username and password from user
    name = input("Name: ")
    pwd = input("Password: ")
    
    # Open passwords file in 'append' mode
    with open("passwords.txt", "a") as f:

        # Write the username and encrypted password to the file
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# Delete all passwords
def delete():

    # Deletes the contents of the file if it exists or creates an empty file and deletes it
    open("passwords.txt", "w").close()


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

        view()
    
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