import random
import sys
import os
import time


mswindows = (sys.platform == "win32")
clear = 'clear' # This is what linux uses to clear cmd screen.                                                               
if mswindows:
        clear = 'cls'   # This is what windows uses to clear the screen.                                                     



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

BOARDLINES = ['    /\     ','   /  \    ','  /    \   ',' /      \  ','/        \ ' ]


BLINES = ['    /\     ','   /  \    ','  /    \   ',' /      \  ','/        \ ' ]

WLINES = ['    /\     ','   /##\    ','  /####\   ',' /######\  ','/########\ ' ]

XLINES = ['    /\     ','  ,.--.,  ',' (  X   )  ',' | `  ` |   ','/ ` ^^ ` \ ' ]

OLINES = ['    /\     ','  ,.--.,  ',' (  0   )  ',' | `  ` |   ','/ ` ^^ ` \ ' ]

ELINES = ['           ','          ','           ','            ','           ' ]


B = ['    /\     ','   /  \    ','  /    \   ',' /      \  ','/        \ ' ]

W = ['    /\     ','   /##\    ','  /####\   ',' /######\  ','/########\ ' ]

X = ['    /\     ','  ,.--.,   ',' (  X   )  ',' | `  ` |  ','/ ` ^^ ` \ ' ]

O = ['    /\     ','  ,.--.,   ',' (  0   )  ',' | `  ` |  ','/ ` ^^ ` \ ' ]

EO = ['           ','  ,.--.,   ',' (  0   )  ',' | `  ` |  ','  ` ^^ `   ' ]

EX = ['           ','  ,.--.,   ',' (  X   )  ',' | `  ` |  ','  ` ^^ `   ' ]

E = ['           ','           ','           ','           ','           ' ]

EO2 = ['           ','  ,.--.,   ',' (  02  )  ',' | `  ` |  ','  ` ^^ `   ' ]

EX2 = ['           ','  ,.--.,   ',' (  X3  )  ',' | `  ` |  ','  ` ^^ `   ' ]


EO3 = ['           ','  ,.--.,   ',' (  03  )  ',' | `  ` |  ','  ` ^^ `   ' ]

EX3 = ['           ','  ,.--.,   ',' (  X3  )  ',' | `  ` |  ','  ` ^^ `   ' ]

EMPTYS = [EX3,EO3,EX2,EO2,EX,EO,E,B,W]

OSPACES = [EO3,EO2,EO,O]

XSPACES = [EX3,EX2,EX,X]

EMPTYBOARD = [E,W,B,W,B,W,B,E]

def blines():
    return BOARDLINES


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
        elif (move <= 0) and (board[move - roll] in XSPACES):
            return True
        else:
            return False

def getLegalMoves(board,roll,player):
    # must output the possibilities, e.g. for going out of the board, in effect changing 
    # the roll, for example if a 6 is rolled, roll 6 move 0 for PX could be changed to
    # roll 5 move 0, so a roll out of board, can be changed to other roll aceiving out of board.
    if (player == 'PO'):
        for x in board:
            if x in OSPACES:
                # t.b.c.


# This is still unfinnished.
def playAgain():
    print("Play Again? (y/n)")

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
                newboard[move - roll] = EMPTYBOARD[move - roll]
                if isWon(newboard,'PO'):
                    print(" Player PO has won.")
                    drawboard(newboard)
                    playAgain()
                    return newboard
                else:
                    drawboard(newboard)
                    return newboard
            # move to Emptyspace, not ot of board.
            elif (board[move] in EMPTYS):
                newboard[move - roll] = EMPTYBOARD[move - roll]
                newboard[move] = O
                drawboard(newboard)
                return newboard
            # moves on an enemy piece.
            else:
                newboard[move] = O
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

        elif (player == 'PX'):
            # moves out of board.
            if (move <= 0):
                newboard[move + roll] = EMPTYBOARD[move + roll]
                if isWon(newboard,'PX'):
                    print(" Player PX has won.")
                    drawboard(newboard)
                    playAgain()
                    return newboard
                else:
                    drawboard(newboard)
                    return newboard
            # move to Emptyspace, not out of board.
            elif (board[move] in EMPTYS):
                newboard[move + roll] = EMPTYBOARD[move + roll]
                newboard[move] = X
                drawboard(newboard)
                return newboard
            # moves on an enemy piece.
            else:
                newboard[move] = X
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
def makeMove(board,roll,move,player):
    if (player == 'PO'):
        if (board[move - roll] == EO3:
                board[move - roll] = EO2
            board[move] 
        elif (board[move - roll] == EO2:
                board[move - roll] = EO
        else:
                  board[move - roll] = EMPTYBOARD[move - roll]
              
'''    
drawboard(GS)












