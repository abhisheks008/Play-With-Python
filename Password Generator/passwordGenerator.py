import random

def passwordGenerator():
    print("""
Password Generator
------------------
For yes or no questions, enter 'y' or 'n' respectively. (Case insensitive)
    """)
    #Test Comment for first commit
    length = int(input("Enter the length of password: "))
    ch = input("Do you want to include special characters? (y/n): ")
    lowerAlphabets = input("Do you want to include lower case alphabets? (y/n): ")
    upperAlphabets = input("Do you want to include upper case alphabets? (y/n): ")
    numbers = input("Do you want to include numbers? (y/n): ")
    password = ""

    if length == 0:
        print("Please enter a valid length.")
        return
    
    if((ch != 'y' and ch != 'Y' and ch != 'n' and ch != 'N') or (lowerAlphabets != 'y' and lowerAlphabets != 'Y' and lowerAlphabets != 'n' and lowerAlphabets != 'N') or (upperAlphabets != 'y' and upperAlphabets != 'Y' and upperAlphabets != 'n' and upperAlphabets != 'N') or (numbers != 'y' and numbers != 'Y' and numbers != 'n' and numbers != 'N') or (length == 0)):
        print("Please enter 'y' or 'n' for yes or no questions respectively.")
        return

    if ch == 'y' or ch == 'Y':
        password += "!@#$%^&*()_+"
    if lowerAlphabets == 'y' or lowerAlphabets == 'Y':
        password += "abcdefghijklmnopqrstuvwxyz"
    if upperAlphabets == 'y' or upperAlphabets == 'Y':
        password += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if numbers == 'y' or numbers == 'Y':
        password += "0123456789"

    print("Your password is: ", end="")
    for i in range(length):
        print(random.choice(password), end="")
    print()

passwordGenerator()