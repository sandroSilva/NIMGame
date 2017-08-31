#Function for the computer to choose the move
def computerMove(n, m):
    if n <= m:
        return n
    else:
        moveC = n % (m+1)
        if moveC > 0:
            return moveC
        return m
 

#Function for the human to choose the move
def humanMove(n, m):
    moveH = 0
    while moveH == 0:
        moveH = int(input("How many pieces you want to remove? "))
        if moveH > n or moveH < 1 or moveH > m:
            moveH = 0
            print("Move not permited!")
            
    return moveH


#game function that define number of pieces, moves and the turn of computer or human.
def game():
    n = int(input("How many pieces? "))
    m = int(input("Limit of pieces for move? "))
    
    #here is where computer defines who is will start
    if (((n )%(m + 1)) == 0):
        print("Human start!")
        is_computer_move = False
    else:
        print("Computer start!")
        is_computer_move = True           
    
    while n > 0:
        if is_computer_move:
            move = computerMove(n, m)
            is_computer_move = False
            print("The computer removed {} piece(s)".format(move))
        else:
            move = humanMove(n, m)
            is_computer_move = True
            print("You removed {} piece(s)".format(move))
        n = n - move
        print("It still just {} piece(s) on the game".format(n))
        
    if is_computer_move:
        print("You win! (it is never will!)")
        return 1
    else:
        print("The computer win! (again)")
        return 0

    
#function that repeat the game for a championship
def championship(nGames):
    human = 0
    computer = 0
    
    for _ in range(nGames):
        winner = game()
        if winner == 1:
            human = human + 1
        else:
            computer = computer + 1
            
    print("Results: Poor human {} x {} Computer".format(human, computer))

    
#main function that determine the configure the type of the game
def main():
    gameType = 0
    
    while gameType == 0:
        print("Welcome to the NIM game! Choose:")
        print("1 - To play one game")
        print("2 - To play a championship")
        gameType = int(input("Type your choice: "))
        if gameType == 1:
            print("You choose a one game!")
            game()
        if gameType == 2:
            print("You choose to play a championship!!")
            nGames = int(input("Type number of games in the championship: "))
            championship(nGames)
        else:
            print("Option not permited!")
            gameType = 0

            
#call the main function
main()