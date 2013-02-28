import random
import sys
import os
import time


mswindows = (sys.platform == "win32")
clear = 'clear' # This is what linux uses to clear cmd screen.                                                               
if mswindows:
        clear = 'cls'   # This is what windows uses to clear the screen.                                                     

TITLE = ["""
          _______                                      
          \\      \\ _____    ____   ____   ____   ____  
          /   |   \\\\__  \\  /    \\ /    \\ /  _ \\ /    \\ 
         /    |    \\/ __ \\|   |  \\   |  (  <_> )   |  \\
         \____|__  (____  /___|  /___|  /\\____/|___|  /
                 \\/     \\/     \\/     \\/            \\/ 

     .........    This software is
    :~, *   * ~,  written by Bergur Thorgeirsson
    : ~, *   * ~. University of Iceland 2013
    :  ~........~
    : *:         :      ~'~,
    :  :         :    ~' *  ~,
    ~* :    *    : ,~' *    * ~,
     ~,:         :.~,*    *  ,~ :
      ~:.........::  ~, *  ,~   :
                  : *  ~,,~  *  :
                  :* * * :  *   :
                   ~, *  : *  ,~
                     ~,  :  ,~
                       ~,:,~

               /\         /\         /\         /\         /\         /\                
  ,.--.,     ,.--.,     ,.--.,      /##\       /  \      ,.--.,     ,.--.,     ,.--.,   
 (  0   )   (  0   )   (  0   )    /####\     /    \    (  X   )   (  X   )   (  X   )  
 | `  ` |   | `  ` |   | `  ` |   /######\   /      \   | `  ` |   | `  ` |   | `  ` |  
  ` ^^ `   / ` ^^ ` \ / ` ^^ ` \ /########\ /        \ / ` ^^ ` \ / ` ^^ ` \   ` ^^ `   
|    0    |    1     |    2     |    3     |    4     |    5     |    6     |    7     | """]


DICEPICS = ['''

          ~'~,
        ~'    ~,
     ,~'   *     ~,
    .~,        ,~ :
    :* ~,    ,~   :
    :    ~,,~     :
    :*   * :*   * :
     ~,    :    ,~
       ~,* :  ,~
         ~,:,~     ''','''

          ~'~,
        ~' *  ~,
     ,~'         ~,
    .~,        ,~ :
    :* ~,  * ,~   :
    :    ~,,~     :
    :  *   :   *  :
     ~,    :    ,~
       ~,* :  ,~
         ~,:,~     ''','''

          ~'~,
        ~' *   ~,
     ,~'   *     ~,
    .~,        ,~ :
    :  ~,  * ,~ * :
    : *  ~,,~ *   :
    :* * * :*    *:
     ~, *  :   *,~
       ~,  : *,~
         ~,:,~     ''','''

          ~'~,
        ~' *   ~,
     ,~'       * ~,
    .~,*       ,~ :
    :  ~,  * ,~ * :
    : *  ~,,~ *   :
    :* * * :*    *:
     ~, *  :   *,~
       ~,  : *,~
         ~,:,~     ''','''

          ~'~,
        ~'*    ~,
     ,~'   *   * ~,
    .~, *      ,~ :
    :  ~,   *,~ * :
    : *  ~,,~ *   :
    :      :*    *:
     ~, *  :   *,~
       ~,* : *,~
         ~,:,~     ''','''

          ~'~,
        ~' *  ~,
     ,~' *    * ~,
    .~,*    *  ,~ :
    :  ~, *  ,~   :
    : *  ~,,~  *  :
    :* * * :  *   :
     ~, *  : *  ,~
       ~,  :  ,~
         ~,:,~     ''']

ROLLINGDICEPICS = ['''

          ~'~,
        ~'**** ~,
     ,~'*********~,
    .~,********,~ :
    :**~,****,~***:
    :****~,,~*****:
    :******:******:
     ~,****:****,~
       ~,**:**,~
         ~,:,~     ''','''

          ~'~,
        ~'**** ~,
     ,~'*********~,
    .~,********,~ :
    :  ~,****,~***:
    :    ~,,~*****:
    :      :******:
     ~,    :****,~
       ~,  :**,~
         ~,:,~     ''','''

          ~'~,
        ~'     ~,
     ,~'         ~,
    .~,        ,~ :
    :  ~,    ,~***:
    :    ~,,~*****:
    :      :******:
     ~,    :****,~
       ~,  :**,~
         ~,:,~     ''','''

          ~'~,
        ~'     ~,
     ,~'         ~,
    .~,        ,~ :
    :**~,    ,~   :
    :****~,,~     :
    :******:      :
     ~,****:    ,~
       ~,**:  ,~
         ~,:,~     ''','''

          ~'~,
        ~'**** ~,
     ,~'*********~,
    .~,********,~ :
    :  ~,****,~   :
    :    ~,,~     :
    :      :      :
     ~,    :    ,~
       ~,  :  ,~
         ~,:,~     ''']

BOARDPICS = ['''

    /\
   /##\
  /####\
 /######\
/########\ ''','''

    /\
   /  \
  /    \
 /      \
/        \ ''','''

    /\
  ,.--., 
 (  X   )
 | `  ` |
/ ` ^^ ` \ ''','''

    /\
  ,.--., 
 (  0   )
 | `  ` |
/ ` ^^ ` \ ''']


B = ['    /\     ','   /  \    ','  /    \   ',' /      \  ','/        \ ' ]

W = ['    /\     ','   /##\    ','  /####\   ',' /######\  ','/########\ ' ]

X = ['    /\     ','  ,.--.,   ',' (  X   )  ',' | `  ` |  ','/ ` ^^ ` \ ' ]

O = ['    /\     ','  ,.--.,   ',' (  0   )  ',' | `  ` |  ','/ ` ^^ ` \ ' ]

EO = ['           ','  ,.--.,   ',' (  0   )  ',' | `  ` |  ','  ` ^^ `   ' ]

EX = ['           ','  ,.--.,   ',' (  X   )  ',' | `  ` |  ','  ` ^^ `   ' ]

E = ['           ','           ','           ','           ','           ' ]

EO2 = ['           ','  ,.--.,   ',' (  02  )  ',' | `  ` |  ','  ` ^^ `   ' ]

EX2 = ['           ','  ,.--.,   ',' (  X2  )  ',' | `  ` |  ','  ` ^^ `   ' ]


EO3 = ['           ','  ,.--.,   ',' (  03  )  ',' | `  ` |  ','  ` ^^ `   ' ]

EX3 = ['           ','  ,.--.,   ',' (  X3  )  ',' | `  ` |  ','  ` ^^ `   ' ]

EMPTYS = [EX3,EO3,EX2,EO2,EX,EO,E,B,W]

OSPACES = [EO3,EO2,EO,O]

XSPACES = [EX3,EX2,EX,X]

EMPTYBOARD = [E,W,B,W,B,W,B,E]


GS = [EO,O,O,W,B,X,X,EX]

# Prints out the board
def drawboard(GameState):
    #sys.stdout.write('.')
    for y in range(5):
        for x in GameState:
            sys.stdout.write(x[y])

        print
    print("|    0    |    1     |    2     |    3     |    4     |    5     |    6     |    7     |")

# determines if the space has adjecents, ie. is part of a prime 
def adjecents(board,space):
    if board[space] in OSPACES:
        if board[space - 1] in OSPACES:
            return True
        elif board[space + 1] in OSPACES:
            return True
        else:
            return False
    elif board[space] in XSPACES:
        if board[space - 1] in XSPACES:
            return True
        elif board[space + 1] in XSPACES:
            return True
        else:
            return False

# detirmines if a move is legal.
# board is the game state list, roll and move are integers, and player is PO or PX. 
# returns True if move is legal otherwise False
def moveLegal(board,roll,move,player):
    if player == 'PO':
        if (move - roll) not in [0,1,2,3,4,5,6,7]:
            return False
        elif (board[move] in EMPTYS) and (board[move - roll] in OSPACES):
            return True
        elif (board[move] in XSPACES) and board[move - roll] in OSPACES and not adjecents(board,move): 
            return True
        elif (move >= 7) and (board[move - roll] in OSPACES):
            return True
        else:
            return False

    elif player == 'PX':
        if (move + roll) not in [0,1,2,3,4,5,6,7]:
            return False
        elif (board[move] in EMPTYS) and (board[move + roll] in XSPACES):
            return True
        elif (board[move] in OSPACES) and board[move + roll] in XSPACES and not adjecents(board,move): 
            return True
        elif (move <= 0) and (board[move + roll] in XSPACES):
            return True
        else:
            return False

def getLegalMoves(board,roll,player):
    # must output the possibilities, e.g. for going out of the board, in effect changing 
    # the roll, for example if a 6 is rolled, roll 6 move 0 for PX could be changed to
    # roll 5 move 0, so a roll out of board, can be changed to other roll aceiving out of board.
	mvList = []
	startList = []
        newRollList = []
	if (player == 'PO'):
		for x in range(len(board)):
			if board[x] in OSPACES:
				if ((roll + x) > 7):
					mvList.append(7)
					startList.append(x)
			else:
				if (board[x] not in OSPACES) and  moveLegal(board,roll,x,'PO'):
					mvList.append(x)
					startList.append(x - roll)
	elif (player == 'PX'):
		for x in range(len(board)):
			if board[x] in XSPACES:
				if ((x - roll) < 0):
					mvList.append(0)
					startList.append(x)
			else:
				if (board[x] not in XSPACES) and  moveLegal(board,roll,x,'PX'):
					mvList.append(x)
					startList.append(x + roll)
        for x in range(len(mvList)):
           newRollList.append(abs(mvList[x]-startList[x])) 


        return [mvList,startList,newRollList]


# This is still unfinnished.
def playAgain():
	choice = raw_input("Play Again? (y/n)")
	if not choice[0] in ['y','Y']:
		return False

# determines if game is won for player on board.
def isWon(board,player):
    if (player == 'PO'):
        w = 0
        for x in board:
            if (x in OSPACES):
                w = 1
        if (w == 0):
            return True
        else:
            return False
    elif (player == 'PX'):
        w = 0
        for x in board:
            if (x in XSPACES):
                w = 1
        if (w == 0):
            return True
        else:
            return False

def Move(board,roll,move,player):
	newboard = board
	if not moveLegal(board,roll,move,player):
		print("This move is not Legal")
		drawboard(board)
		return board
	else:
		if (player == 'PO'):
			# moves out of board.
			if (move >= 7):
				if (newboard[move-roll] == EO3):
					newboard[move-roll] = EO2
				elif(newboard[move-roll] == EO2):
					newboard[move-roll] = EO
				else:
					newboard[move - roll] = EMPTYBOARD[move - roll]
				
				drawboard(newboard)
				return newboard
			# move to Emptyspace, not ot of board.
			elif (board[move] in EMPTYS):
				if (newboard[move-roll] == EO3):
					newboard[move-roll] = EO2
				elif(newboard[move-roll] == EO2):
					newboard[move-roll] = EO
				else:
					newboard[move - roll] = EMPTYBOARD[move - roll]
                
				newboard[move] = O
				drawboard(newboard)
				return newboard
			# moves on an enemy piece.
			else:
				newboard[move] = O
				if (newboard[move-roll] == EO3):
					newboard[move-roll] = EO2
				elif(newboard[move-roll] == EO2):
					newboard[move-roll] = EO
				else:
					newboard[move - roll] = EMPTYBOARD[move - roll]
				# uppgrade PX home base.
				if board[7] == EX2:
					newboard[7] = EX3
					drawboard(newboard)
					return newboard
				elif board[7] == EX:
					newboard[7] = EX2
					drawboard(newboard)
					return newboard
				elif board[7] == E:
					newboard[7] = EX
					drawboard(newboard)
					return newboard


		elif(player == 'PX'):
			# moves out of board.
			if (move <= 0):
				if (newboard[move+roll] == EX3):
					newboard[move+roll] = EX2
				elif(newboard[move+roll] == EX2):
					newboard[move+roll] = EX
				else:
					newboard[move + roll] = EMPTYBOARD[move + roll]
                
				drawboard(newboard)
				return newboard
			# move to Emptyspace, not out of board.
			elif (board[move] in EMPTYS):
				if (newboard[move+roll] == EX3):
					newboard[move+roll] = EX2
				elif(newboard[move+roll] == EX2):
					newboard[move+roll] = EX
				else:
					newboard[move + roll] = EMPTYBOARD[move + roll]

				newboard[move] = X
				drawboard(newboard)
				return newboard
			# moves on an enemy piece.
			else:
				newboard[move] = X
				if (newboard[move+roll] == EX3):
					newboard[move+roll] = EX2
				elif(newboard[move+roll] == EX2):
					newboard[move+roll] = EX
				else:
					newboard[move + roll] = EMPTYBOARD[move + roll]

				# uppgrade PO home base.
				if board[0] == EO2:
					newboard[0] = EO3
					drawboard(newboard)
					return newboard
				elif board[0] == EO:
					newboard[0] = EO2
					drawboard(newboard)
					return newboard
				elif board[0] == E:
					newboard[0] = EO
					drawboard(newboard)
					return newboard



def roll():
    for x in range(15):
        time.sleep(0.1)
        print(ROLLINGDICEPICS[x % 5])
        #os.system(clear)

    time.sleep(0.25)
    x = random.randint(0,5)
    print(DICEPICS[x])
    return x


def doStartRoll():
	fin = 0 # start roll finished.
	while(fin == 0):
		print("Rolling for Start Player PO or PX")
		time.sleep(1)
		POroll = roll()
		print(str(POroll + 1) + " Is the roll of Player O")
		PXroll = random.randint(0,5)
		print(DICEPICS[PXroll])
		print(str(PXroll + 1) + " Is the roll of Player X")
		if(PXroll == POroll):
			continue
		fin = 1
	rollWinner = 'PO'
	if(PXroll > POroll):
		rollWinner = 'PX'

	return [rollWinner,abs(POroll - PXroll)]



def getNextMove(board,roll1,player):
	moves = getLegalMoves(board,roll1,player)
	currentP2 = []
	currentP2.append(player)
	currentP2.append(roll1)
	while(moves[0] == []):
		print("There are no legal moves, turn is forfeit")
		if(currentP2[0] == 'PO'):
			currentP2[0] = 'PX'
			print("Now rolling for PX...")
			time.sleep(1.5)
			r1 = roll()
			currentP2[1] = r1 + 1
			moves = getLegalMoves(board,currentP2[1],currentP2[0])
                        if(moves[0] != []):
				drawboard(board)
		else:
			currentP2[0] = 'PO'
			print("Now rolling for PO...")
			time.sleep(1.5)
			r1 = roll()
			currentP2[1] = r1 + 1
			moves = getLegalMoves(board,currentP[1],currentP[0])
                        if(moves[0] != []):
				drawboard(board)
	
	print(currentP[0] + " Your options are.")
	for x in range(len(moves[0])):
		print(str(x) + ". move to position " + str(moves[0][x]) + " from position " + str(moves[1][x]) +".")
	var = len(moves[0])
	choice = int(raw_input("Choose the number coresponding to your choice of move."))
	chosen = False
	if choice in range(var):
		chosen = True
	while not chosen:
		print("your choice is not in " + str(range(var)) + " choose again.")
		print(currentP[0] + " Your options are.")
		for x in range(len(moves[0])):
			print(str(x) + ". move to possision " + str(moves[0][x]) + " from possision " + str(moves[1][x]) +".")
		choice = int(raw_input("Choose the number coresponding to your choice of move."))
		if choice in range(var):
			chosen = True

	nxt = Move(GS,moves[2][int(choice)],moves[0][int(choice)] ,currentP[0])
	return nxt
	

# This is the start of the game.
os.system(clear)
print(TITLE[0])
print
choice = raw_input("Would you like to play? (yes or no)")
if not choice[0] in ['y','Y']:
	sys.exit()


while True:

	GameOver = False
	currentP = doStartRoll()  # currentP represents [Player currntly choosing move, roll] 
	drawboard(GS)
	nxt = GS
	print( "The winner of the start roll " + currentP[0] + " can now move a piece the difference of the rolles " + str(currentP[1]) + " if it is a legal move.")
	moves = getLegalMoves(GS,currentP[1],currentP[0])
	while(moves[0] == []):
		print("There are no legal moves, turn is forfeit")
		if(currentP[0] == 'PO'):
			currentP[0] = 'PX'
			print("Now rolling for PX...")
			time.sleep(1.5)
			currentP[1] = roll() + 1
			moves = getLegalMoves(GS,currentP[1],currentP[0])
                        if(moves[0] != []):
				drawboard(nxt)
		else:
			currentP[0] = 'PO'   
			print("Now rolling for PO...")
			time.sleep(1.5)
			currentP[1] = roll() + 1
                        moves = getLegalMoves(GS,currentP[1],currentP[0])
			if(moves[0] != []):
				drawboard(nxt)
	
	
	print(currentP[0] + " Your options are.")
	for x in range(len(moves[0])):
		print(str(x) + ". move to position " + str(moves[0][x]) + " from position " + str(moves[1][x]) +".")
	var = len(moves[0])
	choice = int(raw_input("Choose the number coresponding to your choice of move."))
	chosen = False
	if choice in range(var):
		chosen = True
	while not chosen:
		print("your choice is not in " + str(range(var)) + " choose again.")
		print(currentP[0] + " Your options are.")
		for x in range(len(moves[0])):
			print(str(x) + ". move to possision " + str(moves[0][x]) + " from possision " + str(moves[1][x]) +".")
		choice = int(raw_input("Choose the number coresponding to your choice of move."))
		if choice in range(var):
			chosen = True

	nxt = Move(GS,moves[2][int(choice)],moves[0][int(choice)] ,currentP[0])
	
	if(currentP[0] == 'PX'):
		currentP[0] = 'PO'
	elif(currentP[0] == 'PO'):
		currentP[0] = 'PX'


	# The actual game Loop starts here, excuding the begining game
	while(not GameOver):
		os.system(clear)
		drawboard(nxt)
		contin = raw_input("Do you want to roll the dice " + currentP[0] + " ?  (yes or no)")
		if not contin[0] in ['y','Y']:
			ok = playAgain()
			if(ok):
				GameOver = True
				
			else:
				sys.exit()
		else:
			currentP[1] = roll() + 1
			drawboard(nxt)
			nxt = getNextMove(nxt,currentP[1],currentP[0])
			if(isWon(nxt,currentP[0])):
				drawboard(nxt)
				print("Congradulations " + currentP[0] + " you have won the game.")
				nxt = GS
				GameOver = True
			   
			elif(currentP[0] == 'PO'):
				currentP[0] = 'PX'
			elif(currentP[0] == 'PX'):
				currentP[0] = 'PO'
			
		

	if(not playAgain()):
		sys.exit()
	else:
		continue

