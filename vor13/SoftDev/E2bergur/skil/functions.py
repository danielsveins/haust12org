import random
import sys
import os
import time
from pics import *


# Prints out the board
def drawboard(GameState):
    #sys.stdout.write('.')
    for y in range(5):
        for x in GameState:
            sys.stdout.write(x[y])

        print
    print("|    0    |    1     |    2     |    3     |    4     |    5     |    6     |    7     |")

# determines if the space has adjecents, ie. is part of a prime, doesn't rly apply for ends themselves, -> causes call out of array bounds
# but ends help form a prime, has no behavior for being called where there are no pieces. 
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
'''
Determines if a move is legal
Before: board is a list representing the game state
        roll is the last roll of the dice, an integer
        move is the proposed move, an integer
        Player is the player to make the move, string 'PO' or 'PX'

After: moveLegal returns True if there is a move on the board for player player
       traveling exactly roll spaces and ending in move space.

 notice that this function
       does not atempt to deal with the case of a move exceeding the length of the 
       board, this situation is dealt with in the (getLegalMoves function),
       which presents players with their possible moves.
'''
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

'''
 getLegalMoves

Given a game state a player 'PO' or 'PX' and a roll this function
determines all the leagal moves, and returns them in a form of a 
list of three lists, with the moves the starting point and the roll
respectively, the original roll is modified in the case where it is 
possible to move out of the board, That is when a piece moves out to 
saftey.

Before:  board is a list representing the game state
         roll is an integer, representing the original last roll
         player is a string 'PO' or 'PX', representing the player

After:

        returns a list of three lists of integers, with the moves the 
        starting point and the roll respectively, the original roll is 
        modified in the case where it is  possible to move out of the 
        board, That is when a piece moves out to saftey
'''
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


# Asks players if the want to play again
# After: returns Boolean, True for play again e.c.t.
def playAgain():
	choice = raw_input("Play Again? (y/n)")
	if not choice[0] in ['y','Y']:
		return False
        else:
            return True


'''
  isWon
# determines if game is won for player on board.

Before: board is a list representing the game state
        player is a string 'PO' or 'PX' representing the Player
        for whom the determination is bieng made, weather that
        given player has whon the game.

After> Returns True if it is the case that there are no piecess
       of the type used by player left on the board. otherwis 
       returns false 
'''
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

'''
   Move

This function makes a move on a board if it is legal

before: board is a list representing the game state
        roll is an integer representing the last dice roll
        move is an integer representing the proposed move
        player is a string, 'PO' or 'PX' representing the players

After: 
        returns newboard, a board were the proposed move has been made
        if the move is legal, otherwise it retues board. and prints
        -This move is not Legal -

note:   The printing -This move not Legal- is plobably a depreciated part now 
        do to the getLegalMoves function along with the game loop now in 
        effect filtering out all the illegal moves befor this function is
        ever called.

'''

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


'''
This is a function that rolls the dice.
Shows some asci art animation. and returns
a number 0-5
'''
def roll():
    # Ath. skilar fra 0 til 5 (>
    for x in range(15):
        time.sleep(0.1)
        print(ROLLINGDICEPICS[x % 5])
        #os.system(clear)

    time.sleep(0.25)
    x = random.randint(0,5)
    print(DICEPICS[x])
    return x

"""
This function does the starting roll portion of the game.
"""
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

'''
 getNextMove

This is a dialogue really, that aquires the next
move from a player/user. 

and returns a list representing the new game state
'''
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
			moves = getLegalMoves(board,currentP2[1],currentP2[0])
                        if(moves[0] != []):
				drawboard(board)
	
	print(currentP2[0] + " Your options are.")
	for x in range(len(moves[0])):
		print(str(x) + ". move to position " + str(moves[0][x]) + " from position " + str(moves[1][x]) +".")
	var = len(moves[0])
	
        
        chosen = False
	
	while not chosen:
            while True:
                choice = raw_input("Choose the number coresponding to your choice of move.")
                if choice.isdigit():
                    break
                else:
                    print("Try again.")
        
            choice = int(choice)
            if choice in range(var):
		chosen = True        
        
            else:
		print("your choice is not in " + str(range(var)) + " choose again.")
		print(currentP2[0] + " Your options are.")
		for x in range(len(moves[0])):
			print(str(x) + ". move to possision " + str(moves[0][x]) + " from possision " + str(moves[1][x]) +".")
		
	nxt = Move(board,moves[2][int(choice)],moves[0][int(choice)] ,currentP2[0])
	return nxt
