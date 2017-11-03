"""Q7 - Word Break.

Given an input string and a dictionary of words, find out if the input string can be segmented into a space-separated sequence of dictionary words. See following examples for more details.

Consider the following dictionary
{ i, like, sam, sung, samsung, mobile, ice,
  cream, icecream, man, go, mango}

Input:  ilike
Output: Yes
The string can be segmented as "i like".

Input:  ilikesamsung
Output: Yes
The string can be segmented as "i like samsung"
or "i like sam sung".
"""

import re

ANSWER = []
WORD_DICT = ['i', 'like', 'sam', 'sung', 'samsung', 'mobile', 'ice', 'cream', 'icecream', 'man', 'go', 'mango']
INPUT_STR = 'ilike'
INPUT_STR = 'ilikesamsung'


def check_string(s=INPUT_STR, words=WORD_DICT, seg=[]):
  """Checks if the input string can be segmented into the given words.

  Args:
    s: Input String
    words: List of Words
    seg: Current Segments of Words

  Returns:
    seg: List of words
  """

  if not s:
    return seg

  for w in words:
    t_str = re.sub(r'^'+w, '', s)
    if t_str != s:
      t = seg[:]
      t.append(w)
      ANSWER.append(check_string(s=t_str, seg=t))


def main():
  # global WORD_DICT, INPUT_STR
  # WORD_DICT = input('Input a list of words, i.e. the Dictionary:')
  # INPUT_STR = raw_input('Input the string')

  check_string()
  flag = True
  for x in ANSWER:
    if x:
      print ' '.join(x)
      flag = False
  if flag:
    print 'No Answer'
  raw_input()

if __name__ == '__main__':
  main()
