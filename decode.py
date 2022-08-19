


def decodeSecretMessage():
    print("""
 ~ Encryption Cyphers ~
------------------------
|   1. Ceasar Shift    |
|   2. Morse Code      |
|   3. Date Shift      |
------------------------
    """)

    while True:
        cypherSelect = int(
            input("Which encryption cypher would you like to decode? "))
        if cypherSelect == 1:
            decodeCeasarShift()
            break
        elif cypherSelect == 2:
            decodeMorseCode()
            break
        elif cypherSelect == 3:
            decodeDateShift()
            break
        else:
            print("Invalid selection, try again.")


def decodeCeasarShift():
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    print("\nThe cesear shift cypher requires a single letter as a key.\n")
    while True:
        ckey = input("Enter your single letter key: ").lower()
        if ckey not in alphabet:
            print("Invalid key, try again.")
        else:
            offset = alphabet.index(ckey)
            break
    cDict = {}
    for i in range(26):
        if (i + offset) >= 26:
            offsetNum = (i + offset) - 26
        else:
            offsetNum = i + offset
        cDict[alphabet[offsetNum]] = alphabet[i]
    # print(cDict)
    print("\nDictionary Created.")
    message = input("\nPlease enter the message you want to decode: ").lower()
    output = ""
    for l in message:
        try:
            output += cDict[l]
        except:
            output += l
    print("\nYour decrypted message is:", output)
    input("\nPress enter to return to the main menu")

def decodeMorseCode():
    morseDict = {
        "a": "*-", "b": "-***", "c": "-*-*", "d": "-**", "e": "*", "f": "**-*", "g": "--*", 
        "h": "****", "i": "**", "j": "*---", "k": "-*-", "l": "*-**", "m": "--", "n": "-*",
        "o": "---", "p": "*--*", "q": "--*-", "r": "*-*", "s": "***", "t": "-", "u": "**-",
        "v": "***-", "w": "*--", "x": "-**-", "y": "-*--", "z": "--**", " ": "|"
    }
    message = input("\nEnter your message: ").lower()
    list_of_words = message.split(" ")
    morseKey = []
    for i in list_of_words:
        morseKey += [k for k, v in morseDict.items() if v == i]
    output = "".join(morseKey)
    print("\nYour decoded message is:", output)
    input("\nPress enter to return to the main menu...")


def decodeDateShift():
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    print("""\nThe date shift cypher uses a date as the key. 
The date must be input as 6 numbers in the format 'mmddyy'""")
    date_key = ""
    while len(date_key) != 6:
        date_key = input("\nEnter your date key: ")
        if len(date_key) != 6:
            print("""\nInvalid key, try again. 
Hint: Your key must be 6 numbers that represent a date formatted as 'mmddyy'""")
    message = input("\nEnter your message: ")
    output = ""
    key_index = 0
    for l in message:
        offset = int(date_key[key_index])
        alpha_index = alphabet.index(l)
        if alpha_index - offset < 0:
            alpha_index += 27
        output += alphabet[alpha_index - offset]
        if key_index == 5:
            key_index = 0
        else:    
            key_index += 1
    print("\nYour decoded message is:", output)
    input("\nPress enter to return to the main menu...")
