#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from random import randint
from IPython.display import clear_output

def display_board(board):
    print(board[7] + "|" + board[8] + "|" + board[9])
    print('-----')
    print(board[4] + "|" + board[5] + "|" + board[6])
    print('-----')
    print(board[1] + "|" + board[2] + "|" + board[3])

def player_input():
    char1 = ''
    char2 = ''
    while char1 != 'O' and char1 != 'X':
        char1 = input("Hello Player 1, would you prefer to be O or X?").upper()
    if (char1 == 'O'):
        char2 = 'X'
    else:
        char2 = 'O'
    return (char1, char2)

def place_marker(board, marker, position):
    board[position] = marker
    return board 

def win_check(board, mark):
    if (board[1:4] == [mark,mark,mark]  #checks for horizontal
    or board[4:7] == [mark,mark,mark] 
    or board[7:10] == [mark,mark,mark]):
        return True
    
    elif ((board[1] == mark and board[4] == mark and board[7] == mark)  #checks for vertical
    or (board[2] == mark and board[5] == mark and board[8] == mark)
    or (board[3] == mark and board[6] == mark and board[9] == mark)):
        return True
    
    elif ((board[1] == mark and board[5] == mark and board [9] == mark) #checks for diagonal 
    or (board[7] == mark and board[5] == mark and board [3] == mark)):
        return True
    return False

def choose_first():
    starter = ''
    generator = randint(0,1)
    if (generator == 0):
        starter = 'Player 1 shall go first!'
    elif (generator == 1):
        starter = 'Player 2 shall go first!'
    return starter

def space_check(board, position):
    if (board[position]==' '):
        return True 

def full_board_check(board):
    for location in board:
        if location == ' ':
            return False 
    return True

def player_choice(board):
    position = ''
    while position not in list(range (1, 10)):
        try:
            position = int(input("Which position do you want? 1-9! Must choose a space that is not occupied already."))
        except ValueError:
            print("Please input an integer.")
        else:
            clear_output()
   
    if (space_check(board, position)):
        return position
    
    else:
        print("No space at this position. Noob!")
        return 0
        

def replay():
    playAgain = ''
    while playAgain != 'yes' and playAgain!= 'no':
        playAgain = input('Would you like to play again?').lower()
    if (playAgain == 'yes'):
        return True
    return False

def play():
    game_on = True 
    print('Welcome to Tic Tac Toe!')
    replayOrNo = False
    start_board = ['#',' ',' ',' ',' ',' ',' ',' ',' ',' ']
    char1, char2 = player_input() #ask player 1 character preference
    firstie = choose_first()
    print(firstie) #see who goes first 
    if (firstie == 'Player 1 shall go first!'):
        currentMark = char1
    else:
        currentMark = char2 

    while game_on:
        if full_board_check(start_board):
            print('No more space!')
    
            replayOrNo = replay()
            if (replayOrNo == False):
                break
            else:
                play()
        
        print(currentMark + ", it is your turn!")
        display_board(start_board)
        position = player_choice(start_board)
        start_board = place_marker(start_board, currentMark, position)
        clear_output()
        
        if(win_check(start_board,currentMark)): ##check for victory
            print(currentMark + " has won the match!")
            replayOrNo = replay()
            if (replayOrNo == False):
                break
            else:
                play()
        
        if (currentMark == 'O'):
            currentMark = 'X'
        else:
            currentMark = 'O'
       
play()
print('Thank you for playing!')

    #if not replay():
        #break

