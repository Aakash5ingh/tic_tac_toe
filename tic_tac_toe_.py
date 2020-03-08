from IPython.display import clear_output
print("Welcome to Aakash's Tic Tac Toe")
inboard = [" "," "," "," "," "," "," "," "," "]
test_board = ["9","8","7","6","5","4","3","2","1"]    

def wrng_mve(board,a):
    if a.isdigit():
       if int(a) >= 0 and int(a) <= 9: return board[9-int(a)] != " "
       elif int(a)>9: return True
    else: return True
def inp(p,board):
    a = input("{}'s turn:".format(p[0]))
    while wrng_mve(board,a):
          print("wrong move, try again")
          a = input("{}'s turn:".format(p[0]))
    else: board[9-int(a)] = p[1]

def display_board(board):
    for n in range(0,9,3):
        print(" {} | {} | {}".format(board[n],board[n+1],board[n+2]))
        if n<6: print("............")
            
def win_check(p,board):
    marker = p[1]
    for n in range(0,7,3):
        if board[n] == board[n+1] == board[n+2] == marker: 
           return True
           break
    for n in range(0,3):
        if board[n] == board[n+3] == board[n+6] == marker:
           return True
           break
    if board[0] == board[4] == board[8] == marker: return True
    elif board[2] == board[4] == board[6] == marker: return True
      
def head():
    print("Welcome to Aakash's Tic Tac Toe")
    print("Player 1's name:{}".format(p1[0]))
    print("Player 2's name:{}".format(p2[0]))
    print("Markers are {} for {}  and {} for {}".format(p1[1],p1[0],p2[1],p2[0]))
    print("\n")
        
def run(p,board):
     head()
     display_board(board)
     print("\n")    
     display_board(test_board)
     inp(p,board)
     print("\n")
     display_board(board)


pl1 = input("Player 1's name:")
pl2 = input("Player 2's name:")
c_o = input("{}, Enter your marker choice: cross/zero:".format(pl1))
clear_output()
p1 =[]
p1.append(pl1)
p2 =[]
p2.append(pl2)
if c_o == "cross":
   p1.append("×")
   p2.append("o")
elif c_o == "zero":
     p1.append("o")
     p2.append("×")
    
def display(board):
    for i in range(0,9,2):
        run(p1,board)
        if win_check(p1,board):
           clear_output()
           display_board(board)
           print("{} wins".format(p1[0]))
           break
        clear_output()
        if i==8:
            display_board(board)
            print('The game is a draw!')
            break
        run(p2,board)
        if win_check(p2,board):
           clear_output()
           display_board(board)
           print("{} wins".format(p2[0]))
           break
        clear_output()

display(inboard)