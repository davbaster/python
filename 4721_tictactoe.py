from random import randrange

def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        for value in row:
            print("| ",value,"   ", end="")
        print("|\n|       |       |       |")
        print("+-------+-------+-------+")
        

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    free = make_list_of_free_fields(board)
    userMadeMovement = False
    while not userMadeMovement:
        move = int(input("Ingrese el número del cuadro donde quiere hacer su jugada: "))
        #try:
        if move > 0 and move < 10:
            if 1 == move:
                if type (board[0][0]) == int:
                    board[0][0] = 'O'
                    userMadeMovement = True
                else:
                    print("Casilla ya ha sido utilizada.")
                    continue
            elif 2 == move:
                if type (board[0][1]) == int:
                    board[0][1] = 'O'
                    userMadeMovement = True
                else:
                    print("Casilla ya ha sido utilizada.")
                    continue
            elif 3 == move:
                if type (board[0][2]) == int:
                    board[0][2] = 'O'
                    userMadeMovement = True
                else:
                    print("Casilla ya ha sido utilizada.")
                    continue
            elif 4 == move:
                if type (board[1][0]) == int:
                    board[1][0] = 'O'
                    userMadeMovement = True
                else:
                    print("Casilla ya ha sido utilizada.")
                    continue
            elif 5 == move:
                if type (board[1][1]) == int:
                    board[1][1] = 'O'
                    userMadeMovement = True
                else:
                    print("Casilla ya ha sido utilizada.")
                    continue
            elif 6 == move:
                if type (board[1][2]) == int:
                    board[1][2] = 'O'
                    userMadeMovement = True
                else:
                    print("Casilla ya ha sido utilizada.")
                    continue
            elif 7 == move:
                if type (board[2][0]) == int:
                    board[2][0] = 'O'
                    userMadeMovement = True
                else:
                    print("Casilla ya ha sido utilizada.")
                    continue
            elif 8 == move:
                if type (board[2][1]) == int:
                    board[2][1] = 'O'
                    userMadeMovement = True
                else:
                    print("Casilla ya ha sido utilizada.")
                    continue
            elif 9 == move:
                if type (board[2][2]) == int:
                    board[2][2] = 'O'
                    userMadeMovement = True
                else:
                    print("Casilla ya ha sido utilizada.")
                    continue
        else:
            print("Ingrese un numero entre 1 y 9")
                    
    #check if computer made a movement, and if computer won 
    print(userMadeMovement)
    if userMadeMovement:
        display_board (board)
        if victory_for(board, "O"):
            print("Entré como si hubiera ganado usuario")
            return True
        else:
            return False
    
def enter_move2(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    freeFields = make_list_of_free_fields(board)
    
    while True:
        move = int(input("Ingrese el número del cuadro donde quiere hacer su jugada: "))
        
        if move > 0 and move < 10:
            if 1 == move:
                if (0,0) in freeFields:
                    board[0][0] = 'O'
                    return None
                else:
                    print("Casilla ya ha sido utilizada2222.")
                    continue                   
    

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    freeFields = []
    row = 0
    for rows in board:
        col = 0
        for value in rows:
            if (type(value) == int):
                freeFields.append((row,col))
            col += 1
        row += 1
    #print (freeFields)
    return freeFields

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    
    #checking horizontal
    if sign == board[0][0] == board[0][1] == board[0][2]:
        print("El el símbolo ", sign," ha ganado.")
        return True
    elif sign == board[1][0] == board[1][1] == board[1][2]:
        print("El el símbolo ", sign," ha ganado.")
        return True
    elif sign == board[2][0] == board[2][1] == board[2][2]:
        print("El el símbolo ", sign," ha ganado.")
        return True
        
    #checking vertical
    elif sign == board[0][0] == board[1][0] == board[2][0]:
        print("El el símbolo ", sign," ha ganado.")
        return True
    elif sign == board[0][1] == board[1][1] == board[2][1]:
        print("El el símbolo ", sign," ha ganado.")
        return True
    elif sign == board[0][2] == board[1][2] == board[2][2]:
        print("El el símbolo ", sign," ha ganado.")
        return True
    
    #checking Crosses
    elif sign == board[0][0] == board[1][1] == board[2][2]:
        print("El el símbolo ", sign," ha ganado.")
        return True
    elif sign == board[0][2] == board[1][1] == board[2][0]:
        print("El el símbolo ", sign," ha ganado.")
        return True
    else:
        return False
    ##problema: siempre gana el usuario. 



def draw_move(board):
    # The function draws the computer's move and updates the board.
    #use randrange to iterate in the freeFields list. More eficient
    computerMadeMovement = False
    
    while not computerMadeMovement:
        move = randrange(10)
        print(move)
        if 1 == move:
            if type (board[0][0]) == int:
                board[0][0] = 'X'
                computerMadeMovement = True
            else:
                #print("Casilla ya ha sido utilizada.")
                continue
        elif 2 == move:
            if type (board[0][1]) == int:
                board[0][1] = 'X'
                computerMadeMovement = True
            else:
                #print("Casilla ya ha sido utilizada.")
                continue
        elif 3 == move:
            if type (board[0][2]) == int:
                board[0][2] = 'X'
                computerMadeMovement = True
            else:
                #print("Casilla ya ha sido utilizada.")
                continue
        elif 4 == move:
            if type (board[1][0]) == int:
                board[1][0] = 'X'
                computerMadeMovement = True
            else:
                #print("Casilla ya ha sido utilizada.")
                continue
        elif 5 == move:
            if type (board[1][1]) == int:
                board[1][1] = 'X'
                computerMadeMovement = True
            else:
                #print("Casilla ya ha sido utilizada.")
                continue
        elif 6 == move:
            if type (board[1][2]) == int:
                board[1][2] = 'X'
                computerMadeMovement = True
            else:
                #print("Casilla ya ha sido utilizada.")
                continue
        elif 7 == move:
            if type (board[2][0]) == int:
                board[2][0] = 'X'
                computerMadeMovement = True
            else:
                #print("Casilla ya ha sido utilizada.")
                continue
        elif 8 == move:
            if type (board[2][1]) == int:
                board[2][1] = 'X'
                computerMadeMovement = True
            else:
                #print("Casilla ya ha sido utilizada.")
                continue
        elif 9 == move:
            if type (board[2][2]) == int:
                board[2][2] = 'X'
                computerMadeMovement = True
            else:
                #print("Casilla ya ha sido utilizada.")
                continue
        else:
            print("Beep Bop, No se que hacer")
        
        #check if computer made a movement, and if computer won 
    if computerMadeMovement:
        display_board (board)
        if victory_for(board, "X"):
            return True
        
            
            


def start():
    board =     [   [1,2,3],
                    [4,5,6],
                    [7,8,9]   
                ]
    
    while True:
        
        freeFields = make_list_of_free_fields(board)
        
        #enter if computer won
        if draw_move(board):
            return True
          
        #enter if user won
        if enter_move(board):
            return True
        
        #enter if no more free spaces to play
        if len(freeFields) == 0:
           #display_board (board)
           print("Juego Terminado.")
           return None

        #enter_move2(board) #experimental reduced function.
        #print("Casillas libres: ",len(freeFields)) #testing 


start()           
