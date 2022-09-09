text = input("Enter your message: ")
shift = input("Enter a shift number between 1 and 25: ")

def encrypt(text, shift):
    cipher = ''

    if shift.isnumeric():
        n = int(shift)

        if (n > 0 and n < 26 ):

            for char in text:
                 
                if char.isalnum() or char.isspace():
                    
                    
                 
                    if char.isupper(): #65-90

                        if not (ord(char) + n) > 90:
                            
                            code = ord(char) + n
                            cipher += chr(code)  

                        else:
                            code = 65 + ((ord(char) + n) - 90) - 1
                            #B, 25
                            #66 + 25 = 91 => 65 + (90 - (66 + 25)) -1 = 65 => A
                            
                            cipher += chr(code)

                    elif char.islower():#lower 97-122
                        if not (ord(char) + n) > 122:
                            
                            code = ord(char) + n
                            cipher += chr(code)  

                        else:
                            code = 97 + ((ord(char) + n) - 122) - 1
                            cipher += chr(code)
                    
                    else:
                        cipher += char
                        
                else:
                    print("Not valid character: ", char )
                    return 0

            print(cipher)
        else:
            print("Please enter a number between 1 and 25. ")

    else: 
        print("Please enter a correct shift number. ")

encrypt(text, shift)
