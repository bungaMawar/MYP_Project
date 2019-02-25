import random

def display_board(places):
    
    print('   |   |   ')
    print(places[7] + '|' + places[8] + '|' + places[9])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(places[4] + '|' + places[5] + '|' + places[6])
    print('   |   |   ')
    print('-----------')
    print('   |   |   ')
    print(places[1] + '|' + places[2] + '|' + places[3])
    print('   |   |   ')
            
def ticTacToe():
    print ('This is Tic-Tac-Toe.')
    wut = False
    tab = False
    while(tab == False):
        player = None
        player2 = None
        
        response = input('Pick either X or O: ') 
        if response == 'X' or response == 'x':
            player = ' X '
            player2 = ' O '
            if random.randint(1, 10) % 2 == 0:    
                print (player + ' will go first.')
                wut = False
            else:
                print (player2 + ' will go first.')
                wut = True
            tab = True
        elif response == 'O' or response == 'o':
            player = ' O '
            player2 = ' X '
            if random.randint(1, 10) % 2 == 0:    
                print (player + ' will go first.')
                wut = False
            else:
                print (player2 + ' will go first.')
                wut = True
            tab = True
        else:
            print ('That is an invalid input')
            tab = False
            
    print()
    board = ['   '] * 10
    this = False
    turn = 0
    #display_board(board)
    
    while this == False:
        #display_board(board)
        
        tab = False
        while (tab == False):
            display_board(board)
            choice = int(input('Choose where you want to place your marker by using the keypad: '))
            
            for item in board:
                if item == ' X ' or item == ' O ':
                    if board[choice] == item:
                        print ('That space is already taken. Please try again.')
                        board[choice] = item
        
            if choice == 1 or choice == 2 or choice == 3 or choice == 4 or choice == 5 or choice == 6 or choice == 7 or choice == 8 or choice == 9:
                if wut == False and turn % 2 == 0:
                    board[choice] = player
                    turn = turn + 1
                elif wut == True and turn % 2 != 0:
                    board[choice] = player2
                    turn = turn + 1
            
                elif wut == False and turn % 2 != 0:
                    board[choice] = player2
                    turn = turn + 1
                elif wut == True and turn % 2 == 0:
                    board[choice] = player
                    turn = turn  + 1
                
                if board[1] == ' X ' or board[1] == ' O ':
                    if board[1] == board[2] and board[2] == board[3] and board[3] == board[1]:
                        print("We have a winner!")
                        display_board(board)
                        this = True
                    if board[1] == board[5] and board[9] == board[1] and board[5] == board[9]:
                        print ("We have a winner!")
                        display_board(board)
                        this = True
                    if board[4] == board[7] and board[1] == board[4] and board[7] == board[1]:
                        print ("We have a winner!")
                        display_board(board)
                        this = True
                if board [2] == ' X ' or board[2] == ' O ':
                    if board[8] == board[5] and board[2] == board[8] and board[5] == board[2]:
                        print ("We have a winner!")
                        display_board(board)
                        this = True
                if board[3] == ' X ' or board[3] == ' O ':
                    if board[9] == board[3] and board[6] == board[9] and board[3] == board[6]:                                             
                        print ("We have a winner!")
                        display_board(board)
                        this = True
                    if board[7] == board[5] and board[3] == board[5] and board[3] == board[7]:
                        print ('We have a winner!')
                        display_board(board)
                        this = True
                if board[4] == ' X ' or board[4] == ' O ':
                    if board[4] == board[5] and board[6] == board[4] and board[5] == board[6]:
                        print ("We have a winner!")
                        display_board(board)
                        this = True
                if board [7] == ' X ' or board[7] == ' O ':
                    if board[7] == board[8] and board[9] == board[7] and board[8] == board[9]:
                        print ("We have a winner!")
                        display_board(board)
                        this = True
                if turn == 9 and this != True:
                    print ("It's a draw!")
                    display_board(board)
                    this = True
                if this == True:
                    break

def guessing_game():
    print ('This is a guessing game.')
    print('You have five tries to guess the correct number')
    this = False
    while this == False:
        num = random.randint(0, 101)
        for tries in range(0, 5):
            guess = int(input('Insert a number from 0 to 100: '))
            if guess == num:
                print ('Congrats! you guessed the number!')
                print (f'It took you {tries} tries.')
                break
            elif guess >= num:
                print ('The number is lower')
            elif guess <= num:
                print('The number is higher')
        print(f'The number is {num}')
   
        other = input('Do you want to play again? (y/n): ')
        if other == 'Y' or other == 'y':
            this = False
            
        elif other == 'n' or other == 'N':
            this = True
                    
def brain_teasers():
    print("These are brain teasers.")
    print("You will have three tries for each question")
    print("Some questions may repeat themselves.")
    name = input("Before we start, what's your name? ")
    loop = 0
    while loop != 8:
        loop = loop + 1
        teasers = ("If Teresa's daughter is my daughter's mother, what am I to Teresa?", "A woman shoots her husband. Then she holds him underwater for five minutes. Finally, she hangs him. And yet, five minutes later, they both go out and enjoy a nice dinner together. What is the most logical answer to this?", "You're the pilot of an airplane that travels from NY to Chicago - a distance of 800 miles. What is the pilot's name?", "What can travel the whole world and still stay in a corner?", "What has a head, a tail, but no body?", "A buctcher is 6 feet high and has size 9 shoes. What does he weigh?", "What kind of room has no doors or windows?", "Imagine you are in a dark room. How do you get out?")
    
        number = random.randint(0, len(teasers) - 1)
        print (teasers[number])
        truth = False
        turn = 0
        if number == 0:
            print("a. Daughter")
            print("b. Mother")
            print("c. Aunt")
            print("d. Grandmother")
            while truth == False or turn >= 2:
                response = input(" ")
                if response == "a":
                    print("That is correct!")
                    truth = True
                    break
                elif response == "b" or response == "c" or response == "d":
                    print ("That is incorrect.")
                    turn = turn + 1
                    truth = False
                else:
                    print("That is an invalid input")
                    truth = False
                    turn = turn + 0
            print ("The answer was choice a!")
        if number == 1:
                print("a. He's immortal")
                print("b. She's a photographer")
                print("c. It was a dream")
                print("d. They are robots")
                while truth == False and turn <= 2:
                    response = input(" ")
                    if response == "b":
                        print("That is correct!")
                        truth = True
                    elif response == "a" or response == "c" or response == "d":
                        print ("That is incorrect.")
                        truth = False
                        turn = turn + 1
                    else:
                        print("That is an invalid input") 
                        truth = False
                print("The answer was choice b!")
        if number == 2:
            while truth == False and turn <= 2:
                answer = input(" ")
                if answer == name:
                    print("That is correct!")
                    truth = True
                else:
                    print ("That is incorrect.")
                    truth = False
                    turn = turn + 1
            print("His name was " + name + "!")
                    
        if number == 3:
                print("a. A box")
                print("b. A cat")
                print("c. A stamp")
                print("d. A spider")
                while truth == False and turn <= 2:
                    ey = input("")
                    if ey == "c":
                        print("That is correct!")
                        truth = True
                    elif ey == "a" or ey == "b" or ey == "d":
                        print ("That is incorrect.")
                        truth = False
                        turn = turn + 1
                    else:
                        print("That is an invalid input") 
                        truth = False
                print("The answer was choice c!")
        if number == 4:
            while truth == False and turn <= 2:
                oy = input("")
                if oy == 'A coin' or oy == 'a coin':
                    print("That is correct!")
                    truth = True
                else:
                    print ("That is incorrect.")
                    truth = False
                    turn = turn + 1
            print("The answer was a coin!")
        
        if number == 5:
            while truth == False and turn <= 3:
                hey = input("")
                if hey == 'meat' or hey == 'Meat':
                    print("That is correct!")
                    truth = True
                else:
                    print ("That is incorrect.")
                    truth = False
                    turn = turn + 1
            print("He weighs meat!")
        if number == 6:
            while truth == False and turn <= 3:
                hey = input("")
                if hey == 'a mushroom' or hey == 'A mushroom':
                    print("That is correct!")
                    truth = True
                else:
                    print ("That is incorrect.")
                    truth = False
                    turn = turn + 1
        if number == 7:
             while truth == False and turn <= 3:
                hey = input("")
                if hey == 'stop imagining' or hey == "don't imagine":
                    print("That is correct!")
                    truth = True
                else:
                    print ("That is incorrect.")
                    truth = False
                    turn = turn + 1
            
loop = 0
while loop == 0:      
    print ('Enter 1 for Tic-Tac-Toe')
    print ('Enter 2 for a guessing game')
    print ('Enter 3 for brain teasers')
    print ('Enter 0 to exit.')
    response = int(input(''))
    if response == 1:
        ticTacToe()
        now = False
        while now == False:
            ay = input('Do you want to play again? (y/n): ')
            if ay == 'y' or ay == 'Y':
                ticTacToe()
                now = False
            elif ay == 'n' or ay == 'N':
                now = True
    elif response == 2:
        guessing_game()
    elif response == 3:
        brain_teasers()
        now = False
        while now == False:
            ay = input('Do you want to play again? (y/n): ')
            if ay == 'y' or ay == 'Y':
                brain_teasers()
                now = False
            elif ay == 'n' or ay == 'N':
                now = True
    elif response == 0:
        print('Thanks for coming!')
        quit()
    else:
        print("That is an invalid response, please try again.")
