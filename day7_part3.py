def cryption(sentence):
    encryption = ""
    for element in sentence:
        if element in "Aa":
            encryption = encryption + "1"
        elif element in "Bb":
            encryption = encryption + "2"
        elif element in "Cc":
            encryption = encryption + "3"
        elif element in "Dd":
            encryption = encryption + "4"
        elif element in "Ee":
            encryption = encryption + "5"
        elif element in "Ff":
            encryption = encryption + "6"
        elif element in "Gg":
            encryption = encryption + "7"
        elif element in "Hh":
            encryption = encryption + "8"
        elif element in "Ii":
            encryption = encryption + "9"
        elif element in "Jj":
            encryption = encryption + "!"
        elif element in "Kk":
            encryption = encryption + "@"
        elif element in "Ll":
            encryption = encryption + "#"
        elif element in "Mm":
            encryption = encryption + "$"
        elif element in "Nn":
            encryption = encryption + "%"
        elif element in "Oo":
            encryption = encryption + "^"
        elif element in "Pp":
            encryption = encryption + "&"
        elif element in "Qq":
            encryption = encryption + "*"
        elif element in "Rr":
            encryption = encryption + "("
        elif element in "Ss":
            encryption = encryption + ")"
        elif element in "Tt":
            encryption = encryption + "{"
        elif element in "Uu":
            encryption = encryption + "}"
        elif element in "Vv":
            encryption = encryption + "|"
        elif element in "Ww":
            encryption = encryption + "<"
        elif element in "Xx":
            encryption = encryption + ">"
        elif element in "Yy":
            encryption = encryption + "?"
        elif element in "Zz":
            encryption = encryption + "/"
        else:
            encryption = encryption + element
    return encryption

# Used to Store Output in Variable


user_input = input("What you want to Encrypt: ")
encrypted_data = cryption(user_input)
print("Encrypted Data is: ", encrypted_data)


def decryption(sentence):
    decrypted = ""
    for element in sentence:
        if element in "":
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


user_input = encrypted_data
decrypted_data = decryption(user_input)
print("Decrypted Data is: ", decrypted_data.capitalize())
