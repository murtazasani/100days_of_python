# Simple Encrypting Sentence App

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


