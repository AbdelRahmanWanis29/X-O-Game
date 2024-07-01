# XO Game by Abd Alrahman Abdel Wanis
board = [['-','-','-'],['-','-','-'],['-','-','-']]
expboard = [[1,2,3],[4,5,6],[7,8,9]]
Turn = 1
P1Win = False
P2Win = False
Draw = False

Played = [False for k in range(10)]

def DisplayBoard():
    for row in board:
        print(' '.join([str(elem) for elem in row]))
        
def CreatePlayers():

    global Player1 , Player2

    Player1 = input("Enter Player one's name: ")
    Player2 = input("Enter Player two's name: ")

def Explain():
    global Player1 , Player2
    print("Welcome to my XO game")
    print("The board is a standard 3x3 XO board")
    print('Each player will be asked to enter an index for the position to play')
    print('The index for the board is as follows:')
    for row in expboard:
        print(' '.join([str(elem) for elem in row]))
    print(Player1," you have the 'X'")
    print(Player2," you have the 'O'")

def Play():
    global board , Player1 , Player2 , Turn ,Played

    if Turn == 1: 
        print(Player1,', your move!')
    else:
        print(Player2,', your move!')

    print()
    print()
    DisplayBoard()
    print()
    print()

    position = int(input("Enter the position to play: "))

    while not(position == 1 or position == 2 or position == 3 or position == 4 or position == 5 or position == 6 or position == 7 or position == 8 or position == 9):

        position = int(input("Wrong index! try again: "))
    

    if position == 1:
        row = 0
        col = 0
    elif position == 2:
        row = 0
        col = 1
    elif position == 3:
        row = 0
        col = 2
    elif position == 4:
        row = 1
        col = 0
    elif position == 5:
        row = 1
        col = 1
    elif position == 6:
        row = 1
        col = 2
    elif position == 7:
        row = 2
        col = 0
    elif position == 8:
        row = 2
        col = 1
    elif position == 9:
        row = 2
        col = 2
        
    if Turn == 1:
        
        while Played[position] == True:
            print("This position is already taken!")
            position = int(input("choose another one: "))
            if position == 1:
                row = 0
                col = 0
            elif position == 2:
                row = 0
                col = 1
            elif position == 3:
                row = 0
                col = 2
            elif position == 4:
                row = 1
                col = 0
            elif position == 5:
                row = 1
                col = 1
            elif position == 6:
                row = 1
                col = 2
            elif position == 7:
                row = 2
                col = 0
            elif position == 8:
                row = 2
                col = 1
            elif position == 9:
                row = 2
                col = 2

        board[row][col] = 'X'
        Played[position] = True
        Turn = 2
    elif Turn == 2:
        while Played[position] == True:
            print("This position is already taken!")
            position = int(input("choose another one: "))
            if position == 1:
                row = 0
                col = 0
            elif position == 2:
                row = 0
                col = 1
            elif position == 3:
                row = 0
                col = 2
            elif position == 4:
                row = 1
                col = 0
            elif position == 5:
                row = 1
                col = 1
            elif position == 6:
                row = 1
                col = 2
            elif position == 7:
                row = 2
                col = 0
            elif position == 8:
                row = 2
                col = 1
            elif position == 9:
                row = 2
                col = 2

        board[row][col] = 'O'
        Played[position] = True
        Turn = 1     

def CheckWinner(board):
    
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != "-":
            return row[0]

    # Check columns
    for col in range(len(board[0])):
        check = []
        for row in board:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != "-":
            return check[0]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "-":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "-":
        return board[0][2]

    # If there is no winner, return "-"
    return "-"

def CheckDraw(board):
    # Check if there is a winner
    winner = CheckWinner(board)
    if winner != "-":
        return False

    # Check if there are any empty cells left
    for row in board:
        for cell in row:
            if cell == "-":
                return False

    # If there are no winner and no empty cells, it's a draw
    return True

#main

CreatePlayers()
Explain()
End = False
while End == False:
    Play()
    Draw = CheckDraw(board)
    returned = CheckWinner(board)
    if Draw == True:
        print("It's a Draw!")
        End = True
    elif returned == 'X':
        P1Win = True
        DisplayBoard()
        print()
        print(Player1,"Wins!!")
        print(Player2,"better luck next time!")
        End = True
    elif returned == 'O':
        P2Win = True
        DisplayBoard()
        print()
        print(Player2,"Wins!!")
        print(Player1,"better luck next time!")
        End = True