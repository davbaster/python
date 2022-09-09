# IBAN Validator.
#CR050907801032104104010

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','')

if not iban.isalnum():
    print("You have entered invalid characters.")
elif len(iban) < 23:
    print("IBAN entered is too short.")
elif len(iban) > 23:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for ch in iban:
        if ch.isdigit():
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A'))
            print(str(10 + ord(ch) - ord('A')))
    iban = int(iban2)
    print(iban % 97)
    if iban % 97 == 1:
        
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")