#program which is able to simulate the work of a seven-display device, 
#although you're going to use single LEDs instead of segments.

numbers = [ ["°°°°", "°  °","°  °","°  °","°°°°"],
            [" °"," °"," °"," °"," °"],
            ["°°°°","   °","°°°°","°   ","°°°°"],
            ["°°°°","   °","°°°°","   °","°°°°"],
            ["°  °","°  °","°°°°","   °","   °"],
            ["°°°°","°   ","°°°°","   °","°°°°"],
            ["°°°°","°   ","°°°°","°  °","°°°°"],
            ["°°°°","   °","   °","   °","   °"],
            ["°°°°","°  °","°°°°","°  °","°°°°"],
            ["°°°°","°  °","°°°°","   °","°°°°"]
            ,]



def printNumber(n):
    lista = list(str(n))
    digits = [int(x) for x in lista]#convert strings in lista to ints

    n = 0
    length_digits = len(digits)

    #for i in digits:
    #    for k in range(5):
    #        print(numbers[i][k], end=" " )
    #    n+=1
    if length_digits == 1:
        for k in range(5):
            print(numbers[digits[0]][k], end="\n" )
    elif length_digits == 2:
        for k in range(5):
            print(numbers[digits[0]][k], numbers[digits[1]][k], end="\n" )
    elif length_digits == 3:
        for k in range(5):
            print(numbers[digits[0]][k], numbers[digits[1]][k], numbers[digits[2]][k], end="\n" )
    elif length_digits == 4:
        for k in range(5):
            print(numbers[digits[0]][k], numbers[digits[1]][k], numbers[digits[2]][k], 
                  numbers[digits[3]][k], end="\n" )
    elif length_digits == 5:
        for k in range(5):
            print(numbers[digits[0]][k], numbers[digits[1]][k], numbers[digits[2]][k], 
                  numbers[digits[3]][k],numbers[digits[4]][k], end="\n" )
    elif length_digits == 6:
        for k in range(5):
            print(numbers[digits[0]][k], numbers[digits[1]][k], numbers[digits[2]][k], 
                  numbers[digits[3]][k],numbers[digits[4]][k],numbers[digits[5]][k], end="\n" )
    elif length_digits == 7:
        for k in range(5):
            print(numbers[digits[0]][k], numbers[digits[1]][k], numbers[digits[2]][k], 
                  numbers[digits[3]][k],numbers[digits[4]][k],numbers[digits[5]][k], 
                  numbers[digits[6]][k],end="\n" )
    elif length_digits == 8:
        for k in range(5):
            print(numbers[digits[0]][k], numbers[digits[1]][k], numbers[digits[2]][k], 
                  numbers[digits[3]][k],numbers[digits[4]][k],numbers[digits[5]][k], 
                  numbers[digits[6]][k],numbers[digits[7]][k],end="\n" )
    elif length_digits == 9:
        for k in range(5):    
            print(numbers[digits[0]][k], numbers[digits[1]][k], numbers[digits[2]][k], 
                  numbers[digits[3]][k],numbers[digits[4]][k],numbers[digits[5]][k], 
                  numbers[digits[6]][k],numbers[digits[7]][k],numbers[digits[8]][k],end="\n" )
    elif length_digits == 10:
        for k in range(5):    
            print(numbers[digits[0]][k], numbers[digits[1]][k], numbers[digits[2]][k], 
                  numbers[digits[3]][k],numbers[digits[4]][k],numbers[digits[5]][k], 
                  numbers[digits[6]][k],numbers[digits[7]][k],numbers[digits[8]][k],
                  numbers[digits[9]][k],end="\n" )
    print()#**************
    
   
printNumber(123)
printNumber(9081726354)
printNumber(1234567890)