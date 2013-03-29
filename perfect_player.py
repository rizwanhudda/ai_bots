"""state - board peices : 3x3 matrix with each cell in (0, 1, 2)"""
import itertools
scores = { }

# returns the new state after changing r,c th peice
def getBoardState(bstate, r, c, turn):
  state = [ ]
	for _r in range(3):
		row = [ ]
		for _c in range(3):
			if _r == r and _c == c:
				row.append(turn)
			else:
				row.append(bstate[_r][_c])
		state.append(tuple(row))
	return tuple(state)
	
def isWinning(bstate, turn):
	for a in range(3):
		ar = True
		ac = True
		for b in range(3):
			if bstate[a][b] != turn: #a^th row is not filled
				ar = False
			if bstate[b][a] != turn: #a^th col is not filled
				ac = False
		if ar or ac: return True # a^th row/col is filled
	
	# top left - bottom right diagonal is filled
	if bstate[0][0] == turn and bstate[1][1] == turn and bstate[2][2] == turn:
		return True
	
	# bottom left - top right diagonal is filled
	if bstate[0][2] == turn and bstate[1][1] == turn and bstate[2][0] == turn:
		return True
	return False

def allUsed(bstate):
	# check if any of the cell is empty
	for r, c in itertools.product(range(3), range(3)):
		if bstate[r][c] == 0: return False
	return True

def getScore(bstate, turn):

def nextMove(bstate, turn):
	# map : score of opponent -> position of last peice placed
	moves = { }
	# try placing the next peice at each empty position
	for r, c in itertools.product(range(3), range(3)):
		if bstate[r][c] == 0:
			bstate = getBoardState(bstate, r, c, turn)
			oppScore = getScore(bstate, 3 - turn)
			moves[oppScore] = (r, c)
			bstate = getBoardState(bstate, r, c, 0)
	# return the move which leads to the opponent scoring the least
	for oppScore in range(3):
		if moves.has_key(oppScore): return moves[oppScore]

bstate = [ ]
for i in range(3):
	bstate.append(tuple(map(int, raw_input().split(' '))))
bstate = tuple(bstate)
turn = int(raw_input())
move = nextMove(bstate, turn)
print move[0], move[1]
