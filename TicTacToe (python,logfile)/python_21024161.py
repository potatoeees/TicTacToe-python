#import random module 
import random


#user-defined functions

#selection of character played by user
def human():
    human=int(input('Select [1] X or [2] O:'))
    human_valid_input=False
    while human_valid_input==False:
        if human==1:
            print('You selected [1], you are playing as X.')
            human='X'
            break
        elif human==2:
            print('You selected [2], you are playing as O.')
            human='O'
            break 
        else:
            human=int(input('Invalid input! Please try again:')) 
            human_valid_input=False
    return human 
    
#auto generation of character played by computer
def computer(human):
    if human=='X':
        computer='O'
    elif human=='O':
        computer='X'
    print('Computer is playing as',computer,'.')
    return computer
    
#developing the 3x3 grid 
def print_board(board):
    print(board[0][0]+' |'+board[0][1]+' |'+board[0][2])
    print('__|__|__')
    print(board[1][0]+' |'+board[1][1]+' |'+board[1][2])
    print('__|__|__')
    print(board[2][0]+' |'+board[2][1]+' |'+board[2][2])
    print('  |  |  ')
    
#taking in user's input & validating it 
def user_input(current_player):
    
    #1st level to check if input of coordinates are valid
    valid_input='no'
    while valid_input=='no':
        row=int(input('Enter row number:'))
        column=int(input('Enter column number:'))

        if row<=3 and column<=3:
            print('Your input is row',row,'and','column',column,'.')
            
            #2nd level to check if the position chose is available 
            if board[row-1][column-1]==' ':
                board[row-1][column-1]=current_player  
                print_board(board)
                break
            else:
                print('Oops, the place is occupied! Please try again.') 
                valid_input=='no' #need to re-enter row and column(loop again)
        else:
            print('Invalid input! Please try again.')
            valid_input=='no' #need to re-enter row and column(loop again)
    coordinates=row,column
    return coordinates 

#check if someone won with a horizontal line 
def check_horizontal(board):
    global winner
    if board[0][0]==board[0][1]==board[0][2] and board[0][0]!=' ': #take any to check if it's !='', to ensure they are not equal bc they are all empty 
        winner=board[0][0] #choose any 1 location among the 3 to declare the character(X/O) as the winner 
        return True 
    elif board[1][0]==board[1][1]==board[1][2] and board[1][0]!=' ':
        winner=board[1][0]
        return True
    elif board[2][0]==board[2][1]==board[2][2] and board[2][0]!=' ':
        winner=board[2][0]
        return True

#check if someone won with a vertical line 
def check_vertical(board):
    global winner
    if board[0][0]==board[1][0]==board[2][0] and board[0][0]!=' ':
        winner=board[0][0]
        return True
    elif board[0][1]==board[1][1]==board[2][1] and board[0][1]!=' ':
        winner=board[0][1]
        return True
    elif board[0][2]==board[1][2]==board[2][2] and board[0][2]!=' ':
        winner=board[0][2]
        return True

#check if someone won with a diagonal line 
def check_diagonal(board):
    global winner
    if board[0][0]==board[1][1]==board[2][2] and board[0][0]!=' ':
        winner=board[0][0]
        return True
    elif board[0][2]==board[1][1]==board[2][0] and board[0][2]!=' ':
        winner=board[0][2]
        return True

#to check if there is a winner and declare it 
def check_win():
    if check_diagonal(board) or check_horizontal(board) or check_vertical(board):
        print('')
        print('The winner is',winner,'!')
        return True 

#to end the game when it's a tie because all 9 grids are occupied 
def check_tie(board):
    if board[0][0]!=' ' and board[0][1]!=' ' and board[0][2]!=' ' and board[1][0]!=' ' and board[1][1]!=' ' and board[1][2]!=' ' and board[2][0]!=' ' and board[2][1]!=' ' and board[2][2]!=' ':
        print("It's a tie.")
        return True

#randomly generate a coordinate for computer's character 
def computer_input(switch_player):
    comp_input='regenerate'
    while comp_input=='regenerate':
        row=random.randint(0,2) 
        column=random.randint(0,2)
        if board[row][column]==' ':
            board[row][column]=switch_player
            print("Computer's input is row",row+1,"column",column+1,'.')
            break 
        else:
            comp_input='regenerate' #to check if the generated coordinates are already occupied in the board
    print_board(board)
    comp_coordinates=row,column
    return comp_coordinates
    

#main program 

#while loop to repeat the entire game 
continue_play='Y'
while continue_play.upper()=='Y':

    board=[
        [' ',' ',' '],
        [' ',' ',' '],
        [' ',' ',' ']
        ]
    winner=None
    game_running=True

    print('Welcome to the tic-tac-toe game!')
    f=open('logfile_21024161.txt','w') #a log file to track movements in game 
    f.write('Welcome to the log file of Tic Tac Toe!\n')
    #assigning characters 
    current_player=human()
    switch_player=computer(current_player) 

    #nested while loop to repeat the turns in the game 
    move=0
    while game_running==True: #if this variable is true then the whileloop goes on
        print_board(board)
    
        #user's turn
        print('Your turn.')
        coordinates=user_input(current_player)
        move=move+1
        f.write('%d,H,%s,%s\n' %(move,coordinates,current_player)) #string formatting 
        if check_win()==True:
            break
        if check_tie(board)==True:
            break
        
        #computer's turn 
        print('')
        print("Computer's turn.")
        comp_coordinates=computer_input(switch_player)
        move=move+1
        f.write('%d,C,%s,%s\n' %(move,comp_coordinates,switch_player))
        if check_win()==True:
            break
        if check_tie(board)==True:
            break
        
        print('')
        print('')
        print('Next round.')
        print('')

    print('Thank you for playing!')
    continue_play=input('Do you want to restart the game? [Y/N]:')
    f.close() 



