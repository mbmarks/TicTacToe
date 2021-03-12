import os, time
from random import randint

# Represents the empty spaces on the board
spaces = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
#The win condition of the game, 'nwin' is no win, 'xwin' x wins, 'owin' o wins
win = 'nwin'

def clearscreen():
    '''Clears the screen.'''
    os.system('cls')

def printboard(spaces):
    '''Prints the current board state to the console.'''
    print()
    print("      |     |     ")
    print(f'   {spaces[6]}  |  {spaces[7]}  |  {spaces[8]}  ')
    print(" _____|_____|_____")
    print("      |     |     ")
    print(f'   {spaces[3]}  |  {spaces[4]}  |  {spaces[5]}  ')
    print(" _____|_____|_____")
    print("      |     |     ")
    print(f'   {spaces[0]}  |  {spaces[1]}  |  {spaces[2]}  ')
    print("      |     |     ")

def yorn(answer):
    '''Returns true if yes, false if no.
    
    Parameters:
        answer(string): options are 'y', 'yes', 'n', or 'no'
    '''
    if ((answer.lower() == 'y') or (answer.lower() == 'yes')):
        return True
    elif ((answer.lower() == 'n') or (answer.lower() == 'no')):
        return False

def teamSelect(character):
    '''Returns the team selection, True for 'X' and False for 'O'.

    Parameters:
        character (char): team selection
    '''
    if (character.lower() == 'x'):
        return True
    else:
        return False

def pieceOutput(x):
    '''Returns the string value of the team given boolean.

    Parameters:
    x (boolean): True for 'X', False for 'O'
    '''
    if(x):
        return 'X'
    else:
        return 'O'

def move(space, team):
    '''Moves a team to a space on the board. Returns true if successful.

    Parameters:
        space (int): The position selection on the board
        team (boolean): Team 'X' if true, 'O' if false
    '''
    if(spaces[space] == ' '):
        spaces[space] = pieceOutput(team)
        return True
    if (team and spaces[space] != ' '):
        print('Space occupied try again.')
        return False
    else:
        return False

def winningCondition():
    '''Return the victory condition given the current board state.'''
    for i in ['X','O']:
        if(spaces[0] == i):
            if(spaces[1] == i):
                if(spaces[2] == i):
                    return i.lower() + 'win'
            if(spaces[4] == i):
                if(spaces[8] == i):
                    return i.lower() + 'win'
            if(spaces[3] == i):
                if(spaces[6] == i):
                    return i.lower() + 'win'
            
        if(spaces[4] == i):
            if(spaces[3] == i):
                if(spaces[5] == i):
                    return i.lower() + 'win'
            if(spaces[1] == i):
                if(spaces[7] == i):
                    return i.lower() + 'win'
            if(spaces[6] == i):
                if(spaces[2] == i):
                    return i.lower() + 'win'

        if(spaces[8] == i):
            if(spaces[7] == i):
                if(spaces[6] == i):
                    return i.lower() + 'win'
            if(spaces[5] == i):
                if(spaces[2] == i):
                    return i.lower() + 'win'
    return 'nwin' 

def endGameCheck():
    '''Checks and sets the current win condition.'''
    global win
    win = winningCondition()

def turn(team):
    '''Prompts the user to make their move and computes the enemy turn.

    Parameters:
        team (boolean): team of the human player    
    '''
    printboard(spaces)
    print('Using your NumPad, choose a location to move.\n(Hint: Enable NumLock)')
    while(not(move(int(input())-1,team))):
        pass
    clearscreen()
    printboard(spaces)
    time.sleep(1)
    endGameCheck()
    if (win != 'nwin'):
        return
    clearscreen()
    print('Enemy turn', end ="")
    for _ in range(3):
        time.sleep(0.2)
        print('.', end ="", flush=True)
    print()
    while(not(move(randint(0,8),not(team)))):
        pass
    clearscreen()
    endGameCheck()

def begingame():
    '''Begins the game of TicTacToe.'''
    print('Do you want to play a game of tic tac toe?')
    
    while True:
        answer = yorn(input('Yes or No?'))
        if (answer == None):
            clearscreen()
            print('Only \'Yes\' or \'No\'.')
            continue
        elif (answer):
            clearscreen()
            print('Starting the game', end ="")
            for _ in range(3):
                time.sleep(0.2)
                print('.', end ="",flush=True)
            print()
            break
        else:
            clearscreen()
            print('Okay, see you next time!')
            print('Goodbye!')
            return

    clearscreen()

    team = teamSelect(input('Select your team (X or O):'))
    clearscreen()
    print(f'You seleceted {pieceOutput(team)}')
    time.sleep(1)
    clearscreen()

    while(win == 'nwin'):
        turn(team)

    if(win == 'xwin'):
        clearscreen()
        printboard(spaces)
        print('Nice! X won!')
    if(win == 'owin'):
        clearscreen()
        printboard(spaces)
        print('Good Job! O won!')

os.system('cls')
begingame()