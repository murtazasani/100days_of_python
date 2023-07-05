# Simple Decrypting Sentence App

def decryption(sentence):
    decrypted = ""
    for element in sentence:
        if element in "1":
            decrypted = decrypted + "a"
        elif element in "2":
            decrypted = decrypted + "b"
        elif element in "3":
            decrypted = decrypted + "c"
        elif element in "4":
            decrypted = decrypted + "d"
        elif element in "5":
            decrypted = decrypted + "e"
        elif element in "6":
            decrypted = decrypted + "f"
        elif element in "7":
            decrypted = decrypted + "g"
        elif element in "8":
            decrypted = decrypted + "h"
        elif element in "9":
            decrypted = decrypted + "i"
        elif element in "!":
            decrypted = decrypted + "j"
        elif element in "@":
            decrypted = decrypted + "k"
        elif element in "#":
            decrypted = decrypted + "l"
        elif element in "$":
            decrypted = decrypted + "m"
        elif element in "%":
            decrypted = decrypted + "n"
        elif element in "^":
            decrypted = decrypted + "o"
        elif element in "&":
            decrypted = decrypted + "p"
        elif element in "*":
            decrypted = decrypted + "Q"
        elif element in "(":
            decrypted = decrypted + "r"
        elif element in ")":
            decrypted = decrypted + "s"
        elif element in "{":
            decrypted = decrypted + "t"
        elif element in "}":
            decrypted = decrypted + "u"
        elif element in "|":
            decrypted = decrypted + "v"
        elif element in "<":
            decrypted = decrypted + "w"
        elif element in ">":
            decrypted = decrypted + "x"
        elif element in "?":
            decrypted = decrypted + "y"
        elif element in "/":
            decrypted = decrypted + "z"
        else:
            decrypted = decrypted + element
    return decrypted

# Used to Store Output in Variable


user_input = input("What you want to Decrypt: ")
decrypted_data = decryption(user_input)
print("Decrypted Data is: ", decrypted_data.capitalize())
