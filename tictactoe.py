import os, time
from random import randint

spaces = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
win = 'nwin'

def clearscreen():
    os.system('cls')

def printboard(spaces):
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
    if ((answer.lower() == 'y') or (answer.lower() == 'yes')):
        return True
    elif ((answer.lower() == 'n') or (answer.lower() == 'no')):
        return False

def teamSelect(character):
    if (character.lower() == 'x'):
        return True
    else:
        return False

def pieceOutput(x):
    if(x):
        return 'X'
    else:
        return 'O'

def move(space, team):
    if(spaces[space] == ' '):
        spaces[space] = pieceOutput(team)
        return True
    if (team and spaces[space] != ' '):
        print('Space occupied try again.')
        return False
    else:
        return False

def winningCondition():
    if(spaces[0] == 'X'):
        if(spaces[1] == 'X'):
            if(spaces[2] == 'X'):
                return 'xwin'
        if(spaces[4] == 'X'):
            if(spaces[8] == 'X'):
                return 'xwin'
        if(spaces[3] == 'X'):
            if(spaces[6] == 'X'):
                return 'xwin'
        
    if(spaces[4] == 'X'):
        if(spaces[3] == 'X'):
            if(spaces[5] == 'X'):
                return 'xwin'
        if(spaces[1] == 'X'):
            if(spaces[7] == 'X'):
                return 'xwin'
        if(spaces[6] == 'X'):
            if(spaces[2] == 'X'):
                return 'xwin'

    if(spaces[8] == 'X'):
        if(spaces[7] == 'X'):
            if(spaces[6] == 'X'):
                return 'xwin'
        if(spaces[5] == 'X'):
            if(spaces[2] == 'X'):
                return 'xwin'
    
    if(spaces[0] == 'O'):
        if(spaces[1] == 'O'):
            if(spaces[2] == 'O'):
                return 'owin'
        if(spaces[4] == 'O'):
            if(spaces[8] == 'O'):
                return 'owin'
        if(spaces[3] == 'O'):
            if(spaces[6] == 'O'):
                return 'owin'
    
    if(spaces[4] == 'O'):
        if(spaces[3] == 'O'):
            if(spaces[5] == 'O'):
                return 'owin'
        if(spaces[1] == 'O'):
            if(spaces[7] == 'O'):
                return 'owin'
        if(spaces[6] == 'O'):
            if(spaces[2] == 'O'):
                return 'owin'
    
    if(spaces[8] == 'O'):
        if(spaces[7] == 'O'):
            if(spaces[6] == 'O'):
                return 'owin'
        if(spaces[5] == 'O'):
            if(spaces[2] == 'O'):
                return 'owin'
    
    return 'nwin' 

def endGameCheck():
    global win
    win = winningCondition()
    if((win == 'nwin') and (' ' in spaces)):
        return win
    else:
        return win 

def turn(team):
    printboard(spaces)
    print('Using your NumPad, choose a location to move.\n(Hint: Enable NumLock)')
    while(not(move(int(input())-1,team))):
        pass
    clearscreen()
    printboard(spaces)
    time.sleep(1)
    if (endGameCheck() != 'nwin'):
        return
    clearscreen()
    print('Enemy turn', end ="")
    time.sleep(0.2)
    print('.', end ="")
    time.sleep(0.2)
    print('.', end ="")
    time.sleep(0.2)
    print('.', end ="")
    while(not(move(randint(0,8),not(team)))):
        pass
    clearscreen()
    if(endGameCheck() != 'nwin'):
        return

def begingame():
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
            time.sleep(0.2)
            print('.', end ="")
            time.sleep(0.2)
            print('.', end ="")
            time.sleep(0.2)
            print('.', end ="")
            time.sleep(0.2)
            break
        else :
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