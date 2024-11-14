# This program allows you to add, view, and delete passwords stored in a file. 
# You will get a FileNotFoundError if you try to view the passwords and that file doesn't yet exist
# Currently trying to figure out write_key logic

from cryptography.fernet import Fernet

# Uncomment and run write_key() with load_key() commented out to create key file
# Define a key for us
# def write_key():
#     key = Fernet.generate_key()
#     with open("key.key", "wb") as key_file:
#         key_file.write(key)

# write_key()


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

    # Try to open the passwords file in read mode
    try:
        with open(file_name, "r") as f:

            content = f.readlines()

            # Check for empty file
            if not content:
                print("You have not saved any passwords!")
            
            # If there are passwords, display each un/pw pair
            for line in content:

                # retrieve the line. rstrip removes carriage return
                data = line.rstrip()

                # split the username and password with |, assumes username and password do not have a |
                user, pwd = data.split("|")

                # Display this username and password
                print("User: ", user, "| Password: ", 
                    fer.decrypt(pwd.encode()).decode())
                
    except FileNotFoundError:
        # Create a passwords file if there wasn't one already and notify the user
        open(file_name, "w")
        print("passwords file was created as it did not exist.")
        print("The file is empty. No username and password pairs found.")


# Add the new username & password combo to the passwords text file
def add():

    # Prompt for username and password from user
    name = input("Name: ")
    pwd = input("Password: ")
    
    # Open passwords file in 'append' mode
    with open(file_name, "a") as f:

        # Write the username and encrypted password to the file
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

# Delete all passwords
def delete():

    # Deletes the contents of the file if it exists or creates an empty file and deletes it
    open(file_name, "w").close()

# Main processing
if __name__ == "__main__":
    file_name = "passwords.txt"

    while True:

        # Display the menu of options to the user
        mode = input("Select an option: v: view existing passwords, a: add a password, d: delete all passwords, or q: quit.\n")

        # Exit if the user quits
        if mode == "q":
            break

        # Display passwords
        elif mode == "v":
            view()
        
        # Add a new password
        elif mode == "a":
            add()

        # Delete all passwords
        elif mode == "d":
            delete()
            print('All passwords have been PURGED.')

        # Prompt the user that they've provided an invalid response.
        else:
            print("Invalid response. ")

    print('Goodbye!')