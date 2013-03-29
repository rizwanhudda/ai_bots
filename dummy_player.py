"""
state - (board peices : 3x3 matrix with each cell in (0, 1, 2), 
         turn : 1 or 2)
"""
# random comment
bstate = [ ]
for i in range(3):
  bstate.append(tuple(map(int, raw_input().split(' '))))
bstate = tuple(bstate)
turn = int(raw_input())
for r in range(3):
	for c in range(3):
		if bstate[r][c] == 0:
			print r, c
			import sys;sys.exit(0);
