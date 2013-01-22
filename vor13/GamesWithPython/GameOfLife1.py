# Game of Life

CELL = 'O' # The cell character
BK = '+'   # The background Character
DED = 'X'  # The dead cell character

def getNewBoard():
	# Create a  new 200X60 data structure
	board = []
	for x in range(100):
		board.append([])
		for y in range(60):
			board[x].append(BK)

	return board




def drawBoard(board):
	
	hline = '    '
	for i in range(1, 10):
		hline += (' ' * 9) + str(i)
	
	print(hline)
	print('   ' + ('0123456789' * 10))

	for i in range(60):
		if i < 10 :
			extraSpace = ' '
		else:
			extraSpace = ''

		print('%s%s %s %s' % (extraSpace, i, getRow(board,i), i))

	print()
	print('   ' + ('0123456789' * 10))
	print(hline)




def getRow(board, row):
	# Return a string from the board data structure at a certain row.
	boardRow = ''
	for i in range(100):
		boardRow += board[i][row]
	return boardRow


def getBoardCopy(board):
	dupeBoard = []
	for x in board:
		dupeBoard.append(x)
	return dupeBoard

def insertCell(board, x, y):
	board[x][y] = CELL


def shouldLive(board, x, y):
	liveN = 0 #liveN stands for Live Neighbors
	if (board[x-1][y-1] == CELL):
		liveN += 1
	if (board[x][y-1] == CELL):
		liveN += 1
	if (board[x+1][y-1] == CELL):
		liveN += 1
	if (board[x-1][y] == CELL):
		liveN += 1
	if (board[x+1][y] == CELL):
		liveN += 1
	if (board[x-1][y+1] == CELL):
		liveN += 1
	if (board[x][y+1] == CELL):
		liveN += 1
	if (board[x+1][y+1] == CELL):
		liveN += 1
	
	if (liveN < 2):
		return False
	if (liveN > 3):
		return False
	else:
		return True


def iterate(board):
	newB = getNewBoard()
	for x in range(1,99):
		for y in range(1,59):
			if shouldLive(board, x, y):
				newB[x][y] = CELL
	return newB



# Testing

theBoard = getNewBoard()
drawBoard(theBoard)
insertCell(theBoard, 10,50)
drawBoard(theBoard)
newB = getBoardCopy(theBoard)
print('Drawing duplicateBoard')
drawBoard(newB)
insertCell(newB, 11,50)
insertCell(newB, 12,50)
insertCell(newB, 11,51)
insertCell(newB, 11,49)
drawBoard(newB)
print('Do you want to iterate')
input()
print()
print(CELL)
print()
print(newB[11][49])
print()
if newB[11][49] == CELL:
	print('bla')
print()
newB2 = iterate(newB)
drawBoard(newB2)
input()
while True:
	print('Iterate again?')
	input()
	newB2 = iterate(newB2)
	drawBoard(newB2)
	input()



