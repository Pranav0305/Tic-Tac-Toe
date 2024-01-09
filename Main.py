from tkinter import *
import random
import time

root = Tk()
root.title("tic-tac-toe")
turn = 0
comp = random.randint(0,1)

board = [["","",""],["","",""],["","",""]]
buttonsArr = [[],[],[]]

playerScore = 0
aiScore = 0

fillerLabel = Label(root,text="PLAYER - X")
fillerLabel.grid(row=4,column=1)

fillerLabel1 = Label(root,text="COMP - O")
fillerLabel1.grid(row=5,column=1)

# Scoreboard
scoreText = "YOU  " + str(str(playerScore) + " - " + str(aiScore)) + "  COMP"
scoreLabel = Label(root,text= scoreText)
scoreLabel.grid(row=0,column=1)

class BoardButton:
    x = 0
    y = 0
    button = Button()
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.button = Button(root,padx=50,pady=40,text=" ",command=self.clickBoardButton)
        self.button.grid(row=self.x,column=self.y)
    
    def clickBoardButton(self):
        global playerScore
        global aiScore
        global board
        if board[self.x-1][self.y] == 'X' or board[self.x-1][self.y] == 'O':
            return
        s = "X"
        global turn

        board[self.x-1][self.y] = s
        label = Label(root,text=s)
        label.grid(row=self.x,column=self.y)
        turn += 1
        if checkWinner() == 'X':
            print("YOU WIN")
            displayEnd("YOU WIN")

            playerScore += 1
            updateScoreboard()

            root.after(1000,clear_board)
            return
        if turn >= 9:
            print("DRAW")
            displayEnd("DRAW")
            root.after(1000,clear_board)
            return
        # print(checkWinner())
        # play_easy("O")
        # play_medium("O")
        play_hard("O")
        if checkWinner() == 'O':
            print("GAME OVER")
            displayEnd("GAME OVER")
            aiScore += 1
            updateScoreboard()
            root.after(1000,clear_board)
            return
        if turn >= 9:
            print("DRAW")
            displayEnd("DRAW")
            root.after(1000,clear_board)
            return
    
    def compPlay(self,s):
        global turn
        board[self.x-1][self.y] = s
        label = Label(root,text=s)
        label.grid(row=self.x,column=self.y)
        turn += 1
        
# notify player about game result
def displayEnd(message):
    messageList = message.split()
    try:
        label1 = Label(root,text = messageList[0])
        label1.grid(row=6,column=1)
        label1.after(1500,label1.destroy)
        
        label2 = Label(root,text = messageList[1])
        label2.grid(row=7,column=1)
        label2.after(1500,label2.destroy)
    except:
        pass

def clear_board():
    global board
    global buttonsArr
    global turn
    global comp
    
    turn = 0
    for i in range(3):
        for j in range(3):
            board[i][j] = ""

    for i in range(3):
        for j in range(3):
            gridButton = BoardButton(i+1,j)
            buttonsArr[i].append(gridButton)
            
    #check first player
    comp = random.randint(0,1)
    if comp == 1:
        play_hard("O")
        turn = 1

def checkWinner():
    #check rows
    for i in board:
        x = 0
        o = 0
        for j in i:
            x += (j == 'X')
            o += (j == 'O')
        if x == 3:
            return 'X'
        if o == 3:
            return 'O'

    #check cols
    for i in range(3):
        x = 0
        o = 0
        for j in range(3):
            x += (board[j][i] == 'X')
            o += (board[j][i] == 'O')
        if x == 3:
            return 'X'
        if o == 3:
            return 'O'
    
    #check diagonals
    if board[0][0] == board[1][1] and board[2][2] == board[1][1]:
        return board[0][0]
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        return board[0][2]
    
    # return

def updateScoreboard():
    global scoreLabel
    scoreText = "YOU  " + str(str(playerScore) + " - " + str(aiScore)) + "  COMP"
    scoreLabel = Label(root,text= scoreText)
    scoreLabel.grid(row=0,column=1)

def play_easy(s):
    # print("Hello")
    global board
    global buttonsArr
    available = []
    for i in range(3):
        for j in range(3):
            # print(board[i][j])
            if board[i][j] == 'X' or board[i][j] == 'O':
                continue
            available.append([i,j])
    # print(available)
    if len(available) <= 0:
        return
    ind = random.randint(0,len(available)-1)
    board[available[ind][0]][available[ind][1]] = s
    buttonsArr[available[ind][0]][available[ind][1]].compPlay(s)
    
def maxInd(l):
    ans = 0
    tmp = 0
    for i in range(len(l)):
        if l[i] > tmp:
            ans = i
            tmp = l[i];
    return ans
    
def play_medium(s):
    global board
    global buttonsArr
    
    #check opponent winning
    #check rows
    rows_arr = []
    for i in range(3):
        x = board[i].count('X')
        rows_arr.append(x)
    rows_ind = maxInd(rows_arr)
    
    #check columns
    cols_arr = []
    for i in range(3):
        x = 0
        for j in range(3):
            if board[j][i] == 'X':
                x += 1
        cols_arr.append(x)
    cols_ind = maxInd(cols_arr)
    
    #check diagonals
    diag_01 = [[0,0],[1,1],[2,2]]
    diag_02 = [[0,2],[1,1],[2,0]]
    x1 = 0
    x2 = 0
    for i in diag_01:
        if board[i[0]][i[1]] == 'X':
            x1 += 1
    for i in diag_02:
        if board[i[0]][i[1]] == 'X':
            x2 += 1
            
    l = [] # square to prevent win
    
    if x1 == 2:
        for i in diag_01:
            if board[i[0]][i[1]] == 'X' or board[i[0]][i[1]] == 'O':
                continue
            l = i
            break
        
    if x2 == 2:
        for i in diag_02:
            if board[i[0]][i[1]] == 'X' or board[i[0]][i[1]] == 'O':
                continue
            l = i
            break

    # prevent win by diagonal
    if len(l) != 0:
        # print(l)
        board[l[0]][l[1]] = s
        buttonsArr[l[0]][l[1]].compPlay(s)
        return
    
    # prevent win by row
    if rows_arr[rows_ind] == 2:
        for i in range(3):
            if board[rows_ind][i] == 'X' or board[rows_ind][i] == 'O':
                continue
            l = [rows_ind,i]
            break
        
    if len(l) != 0:
        # print(l)
        board[l[0]][l[1]] = s
        buttonsArr[l[0]][l[1]].compPlay(s)
        return 
    
    # prevent win by column
    if cols_arr[cols_ind] == 2:
        for i in range(3):
            if board[i][cols_ind] == 'X' or board[i][cols_ind] == 'O':
                continue
            l = [i,cols_ind]
            break
        
    if len(l) != 0:
        # print(l)
        board[l[0]][l[1]] = s
        buttonsArr[l[0]][l[1]].compPlay(s)
        return
        
    
    play_easy(s)
    

def play_hard(s):
    global board
    global buttonsArr
    
    #find win
    
    #check rows
    l = [] # winning coords
    for i in range(3):
        x = board[i].count(s)
        if x == 2:
            # print(i)
            for j in range(3):
                if board[i][j] == 'X' or board[i][j] == 'O':
                    continue
                l = [i,j]
                break
        if len(l) > 0:
            break
    
    if len(l) != 0:
        # print(l)
        board[l[0]][l[1]] = s
        buttonsArr[l[0]][l[1]].compPlay(s)
        return
    
    # check columns
    for i in range(3):  
        x = 0
        for j in range(3):
            if board[j][i] == 'O':
                x += 1
        if x == 2:
            for j in range(3):
                if board[j][i] == 'X' or board[j][i] == 'O':
                    continue
                l = [j,i]
                break
        if len(l) > 0:
            break
        
    if len(l) != 0:
        # print(l)
        board[l[0]][l[1]] = s
        buttonsArr[l[0]][l[1]].compPlay(s)
        return    
    
    # check diagonals
    diag_01 = [[0,0],[1,1],[2,2]]
    diag_02 = [[0,2],[1,1],[2,0]]
    o1,o2 = 0,0
    
    for i in diag_01:
        if board[i[0]][i[1]] == s:
            o1 += 1
            
    for i in diag_02:
        if board[i[0]][i[1]] == s:
            o2 += 1
    
    if o1 == 2:
        for i in diag_01:
            if board[i[0]][i[1]] == 'X' or  board[i[0]][i[1]] == 'O':
                continue
            l = i
            break
        
    if o2 == 2:
        for i in diag_02:
            if board[i[0]][i[1]] == 'X' or  board[i[0]][i[1]] == 'O':
                continue
            l = i
            break
        
    if len(l) != 0:
        # print(l)
        board[l[0]][l[1]] = s
        buttonsArr[l[0]][l[1]].compPlay(s)
        return    
            
    play_medium(s)
        

# set up board
for i in range(3):
    for j in range(3):
        gridButton = BoardButton(i+1,j)
        buttonsArr[i].append(gridButton)

#check first player
if comp == 1:
    play_hard("O")

root.mainloop()
