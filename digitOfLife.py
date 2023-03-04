#digit of life

def birthDigit(num):
    if not num.isdigit() or len(num) != 8:
        print("Enter only numbers in format YYYYMMDD or DDMMYYYY")
        return 0

    digit = 0
    
    while digit == 0 :

        num = str(num)
        for d in num :
            digit += int(d)
        if digit > 9:
            num = digit
            digit = 0


    return digit

##starting app
date = input("Enter your birth date in format YYYYMMDD: ")
print()
print ("Digit of life is ", birthDigit(date))
