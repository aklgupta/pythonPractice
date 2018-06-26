"""Q 15 - Countdown

Input a integer N from user
Print numbers N to 0 in a single line, however, each number should be printed at an interval of 1 second.

eg.
Input: 5
Output: 5 4 3 2 1 0
(The output is generated over a time of 5 seconds, printing one number per second)
"""

import time

N = input("Enter a number: ")
for i in xrange(N, -1, -1):
  print i, 
  time.sleep(1)
