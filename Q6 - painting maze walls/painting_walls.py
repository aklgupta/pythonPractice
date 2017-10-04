"""Team Python Q6.

You are a maze keeper, and are suppose to paint a maze.
However, you are to paint only those walls of the maze that are visible i.e. if a particular side of a wall is inaccessible in the maze, you need not paint it.
Write a python program to input the maze and count the number of sides that need to be painted.

You need to accept an input maze as a matrix of hashes(#) and period(.)
Hashes = walls
Periods = empty spaces or path
Each row in the matrix will have the same no of columns.
Min. no. of ROWS and min. no of columns if 1.
You can traverse only horizontally or vertically in the maze.
"""

SAMPLE_INPUT = ['##', '##']
SAMPLE_INPUT = ['##..#', '#.#.#', '#.#.#', '#####']
SAMPLE_INPUT = ['######', '#.....', '#.####', '#.#..#', '#.##.#', '#....#', '######']
SAMPLE_INPUT = ['######', '#.....', '#..#..', '#.....', '######']
SAMPLE_INPUT = ['#.#.#.#', '.#.#.#.', '#.#.#.#', '.#.#.#.']

MAZE = []
PATHS = []
ROWS = COLS = 0


def create_path():
  """Define the Accessible path.
  """
  global PATHS, ROWS, COLS, MAZE

  for i in xrange(ROWS):
    if MAZE[i][0] == '.':
      PATHS[i][0] = 1
    if MAZE[i][COLS - 1] == '.':
      PATHS[i][COLS - 1] = 1

  for j in xrange(COLS):
    if MAZE[0][j] == '.':
      PATHS[0][j] = 1
    if MAZE[ROWS - 1][j] == '.':
      PATHS[ROWS - 1][j] = 1

  rows = ROWS - 1
  cols = COLS - 1

  for _ in xrange(ROWS*COLS):
    for i in range(1, rows):
      for j in range(1, cols):
        if MAZE[i][j] == '.' and (PATHS[i+1][j] == 1 or PATHS[i-1][j] == 1 or
                                  PATHS[i][j+1] == 1 or PATHS[i][j-1] == 1):
          PATHS[i][j] = 1

  for t in PATHS:
    print t


def count_faces():
  """Count Paintable faces.

  Returns:
    count
  """
  global PATHS, ROWS, COLS, MAZE
  count = 0

  for i in xrange(ROWS):
    for j in xrange(COLS):
      if MAZE[i][j] != '#':
        continue

      # If 1st or Last row
      if i == 0 or i == ROWS - 1:
        count += 1

      # If 1st or Last column
      if  j == 0 or j == COLS - 1:
        count += 1

      # Check Up
      if i > 0 and PATHS[i-1][j] == 1:
        count += 1

      # Check Down
      if i < ROWS - 1 and PATHS[i+1][j] == 1:
        count += 1

      # Check Left
      if j > 0 and PATHS[i][j-1] == 1:
        count += 1

      # Check Right
      if j < COLS - 1 and PATHS[i][j+1] == 1:
        count += 1

  return count


def main():
  global PATHS, ROWS, COLS, MAZE
  # maze = input('Input the maze as a list')
  MAZE = SAMPLE_INPUT
  PATHS = [[0 for _ in x] for x in MAZE]
  ROWS = len(MAZE)
  COLS = len(MAZE[0])
  create_path()
  count = count_faces()
  print count



if __name__ == '__main__':
  main()
