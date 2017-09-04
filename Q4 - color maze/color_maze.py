"""Team Python Practice Question 4.


Write a function that traverse a color maze by following a sequence of colors. For example this maze can be solved by the sequence 'orange -> green'. Then you would have something like this 
For the mazes you always pick a spot on the bottom, in the starting color and try to get to the first row. Once you reach the first row, you are out of the maze. You can move horizontally and vertically, but not diagonally. It is also allowed to move on the same node more then once.

Sample Input
Sequence
O G

Maze
B O R O Y
O R B G R
B O G O Y 
Y G B Y G 
R O R B R

Sample output
/ / / O /
/ / / G /
/ O G O / 
/ G / / / 
/ O / / /

"""

import copy

MAZE = []
SEQ = []
SOL = []
N = 0  # No of rows in maze
M = 0  # No of cols in maze
S = 0  # Sequence Length


def main():
  """Main Function.

  Calls other function to work for it... :D
  """

  # input the MAZE, SEQunece, and gereates a blank SOLution
  get_inputs()

  failed = True
  for i in xrange(M):
    if get_sol(copy.deepcopy(SOL), [['' for _ in x] for x in SOL], -1, [N-1, i]):
      failed = False
      print '\n'*3, 'SOLUTION:'
      for row in SOL:
        for e in row:
          print e,
        print ''
      break
  if failed:
    print '\n'*3, 'FAILED, No Solution Found'


def get_inputs():
  """Input."""
  global SOL, MAZE, SEQ, M, N, S

  # Input Maze
  MAZE = input('Enter a list of list as input matrix: ')
  N = M = len(MAZE)

  # Create Blank Solution
  SOL = [['/' for _ in x] for x in MAZE]

  # Get Sequence to use
  S = int(raw_input('Enter length of Sequence: '))
  for i in xrange(S):
    col = raw_input('Enter Color Letter: ').upper()
    SEQ.append(col)

  print '\n', 'Maze:'
  for i in xrange(N):
    for j in xrange(M):
      print MAZE[i][j],
    print ''

  print '\n', 'Sequence:'
  print SEQ


def get_sol(cur_sol, when_reached, seq_pos, last_pos):
  """Sols."""
  global SOL
  seq_pos = 0 if seq_pos == S-1 else seq_pos + 1
  i, j = last_pos

  # print MAZE[i][j], SEQ[seq_pos], MAZE[i][j] == SEQ[seq_pos]
  if MAZE[i][j] == SEQ[seq_pos]:

    # Check if we are entering an infinite loop
    if str(seq_pos) in when_reached[i][j]:
      return False

    # Updated current temp solution, and mark the path used
    cur_sol[i][j] = SEQ[seq_pos]
    when_reached[i][j] += str(seq_pos)

    # If we reached the top
    if i == 0:
      SOL = cur_sol
      return True

    # Go Up
    if i > 0 and get_sol(copy.deepcopy(cur_sol), when_reached, seq_pos, [i-1, j]):
      return True

    # Go Down
    if i < N-1 and get_sol(copy.deepcopy(cur_sol), when_reached, seq_pos, [i+1, j]):
      return True

    # Go Left
    if j > 0 and get_sol(copy.deepcopy(cur_sol), when_reached, seq_pos, [i, j-1]):
      return True

    # Go Right
    if j < M-1 and get_sol(copy.deepcopy(cur_sol), when_reached, seq_pos, [i, j+1]):
      return True

  # Return False if no sol found
  return False

if __name__ == '__main__':
  main()
