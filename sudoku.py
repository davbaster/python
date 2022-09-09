#create a sudoku game 3x3 squares
#You provide nine arrays of 9 numbers from 1 to 9, representing a soduko board already filled with numbers.
#program checks the board and returns a message if the soduko game was completed successfully or if it's not a valid soduko game.

#test: 123456789  456123789  789123456  good bad bad
#test 2: 295743861 431865927 876192543


#builds a 9 number logic square given three list, and returns three squares in a list
def checkSquares(rows):
        #checking square 1
    list =[]
    square = ""

    for i in range (0,9,3):
        square =""
        for p in range(0,3):
            square += rows[i][p]
            square += rows[i+1][p]
            square += rows[i+2][p]
        list.append(square)

        #checking square 2
        square =""
        for p in range(3,6):
            square += rows[i][p]
            square += rows[i+1][p]
            square += rows[i+2][p]
        list.append(square)

        #checking square 3
        square =""
        for p in range(6,9):
            square += rows[i][p]
            square += rows[i+1][p]
            square += rows[i+2][p]
        list.append(square)
    #print(list)
    if checkRows(list) == 0 :
        return 0#No valid soduko game.
    
    return 1#valid


 #checks if a given row contains the numbers from 1 to 9
def checkSoduko(row):
   
    #print (row)
    for num in range(1,9):
        if row.find(str(num)) == -1:
            #print("BAD soduko")
            return 0
    # 1 = square has all numbers from 1 to 9
    return 1  

#checks horizontal rows contained in a list. Checks if each rows contains numbers from 1 to 9
def checkRows(rows):

    for p in range(0,9):
        #print("p :", p)
        if checkSoduko(rows[p]) == 0 :
           return 0

    return 1

#check vertical rows given a list of 9 list. Checks if each rows contains numbers from 1 to 9
def checkVerticalRows(rows):#REVISAR SI FUNCIONA BIEN
    for i in range(0,9):
        row=""
        for j in range(0,9):
            row += rows[j][i]#rowToChek = keeps i , an increases j, row[0][0], row[1][0],...,row[8][0],

        if checkSoduko(row) == 0 :
            return 0

    return 1




#main login of the game
def initializeGame(rows):
    

    #print("Calling checkSoduko from CheckRows")
    #checking rows from left to right
    if checkRows(rows) == 0 :
        print("Rows: Not a valid Soduko")
    
    #print("Calling checkSoduko from CheckVerticalRows")
    #checking rows from top to bottom
    elif checkVerticalRows(rows) == 0 :
        print("Cross Rows: Not a valid Soduko")

    #print("Calling checkSoduko from CheckSquares")
    elif checkSquares(rows) == 0 :
        print("Cross Rows: Not a valid Soduko")
    else:
        print("It's a valid Soduko")



#starting app
rows = ["295743861","431865927","876192543","387459216","612387495","549216738","763524189","928671354","154938672"]#should return a valid soduko
rows2 = ["195743862","431865927","876192543","387459216","612387495","549216738","763524189","928671354","254938671"]#should return a NO valid soduko

#for n in range(0,9):
#    row = input("Enter a row: ")
#    rows.append(row)



initializeGame(rows)
