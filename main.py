import code, decode


def mainMenu():
    print(""" 
    ~ Secret Code Generator ~   
--------------------------------
| 1. Generate a secret message |
| 2. Decode a secret message   |
| 3. Quit                      |
--------------------------------
""")
    
    while True:
        selection = int(input("Select an option: "))
        if selection == 1:
            code.generateSecretMessage()
            mainMenu()
        elif selection == 2:
            decode.decodeSecretMessage()
            mainMenu()
        elif selection == 3:
            print("\nQuitting application...Goodbye!\n")
            quit()
        else:
            print("Invalid selection, try again.")


if __name__ == "__main__":
    mainMenu()
