This program allows a user to add, view, or delete passwords that are saved to a file. The passwords are encrypted using a Fernet key. 

To use this program do the following:
1. Uncomment the write_key function and comment out the load_key function and the next two lines of code. Run the program once to generate the key.
2. Comment out write_key and uncomment out the load_key logic
3. Run the program

Goals
1. Change cryptography to not have to comment out code, if possible.
2. Use more sophisticated cryptography
3. Feature: Add ability to change a password.
4. Feature: Introduce master password to take executive actions
