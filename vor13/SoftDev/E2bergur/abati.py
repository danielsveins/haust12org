import random
import sys
import os
import time
from functions import * 
from pics import *

mswindows = (sys.platform == "win32")
clear = 'clear' # This is what linux uses to clear cmd screen.                                                               
if mswindows:
        clear = 'cls'   # This is what windows uses to clear the screen.                                                     



# This is the start of the game.
os.system(clear)
print(TITLE[0])
print
choice = raw_input("Would you like to play? (yes or no)")
if not choice[0] in ['y','Y']:
	sys.exit()


while True:

	GameOver = False
	os.system(clear)
	currentP = doStartRoll()  # currentP represents [Player currntly choosing move, roll] 
	
	nxt = [EO,O,O,W,B,X,X,EX]
	drawboard(nxt)
	print( "The winner of the start roll " + currentP[0] + " can now move a piece the difference of the rolles " + str(currentP[1]) + " if it is a legal move.")
	moves = getLegalMoves(nxt,currentP[1],currentP[0])
	while(moves[0] == []):
		print("There are no legal moves, turn is forfeit")
		if(currentP[0] == 'PO'):
			currentP[0] = 'PX'
			print("Now rolling for PX...")
			time.sleep(1.5)
			currentP[1] = roll() + 1
			moves = getLegalMoves(nxt,currentP[1],currentP[0])
                        if(moves[0] != []):
				drawboard(nxt)
		else:
			currentP[0] = 'PO'   
			print("Now rolling for PO...")
			time.sleep(1.5)
			currentP[1] = roll() + 1
                        moves = getLegalMoves(nxt,currentP[1],currentP[0])
			if(moves[0] != []):
				drawboard(nxt)
	
	
	print(currentP[0] + " Your options are.")
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
		print(currentP[0] + " Your options are.")
		for x in range(len(moves[0])):
			print(str(x) + ". move to possision " + str(moves[0][x]) + " from possision " + str(moves[1][x]) +".")
		

	nxt = Move(nxt,moves[2][int(choice)],moves[0][int(choice)] ,currentP[0])
	
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
	
