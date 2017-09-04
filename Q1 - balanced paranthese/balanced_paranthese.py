"""Team Practice Q1.



Given a string expression s, write a program to test whether the pairs and the orders of “{“,”}”,”(“,”)”,”[“,”]” are correct in s.
     
Sample Input:
s = “[()]{}{[()(){}[]]()}”
Output:
True
    
Sample Input:
s = “[(])”
Output:
False


Assume that the user input string is not allowed to contain any charater other than the following:
[]{}()
"""

def main():
  matches = {
      ']': '[',
      '}': '{',
      ')': '(',
  }
  open_seq = []
  # s = '[()]{}{[()(){}[]]()}'
  s = raw_input('Enter the string: ').strip()
  perfect = True

  for ch in s:
    if ch in matches:
      n = len(open_seq)
      if n == 0 or open_seq[n-1] != matches[ch]:
        perfect = False
        break
      else:
        open_seq.pop()
    else:
      open_seq.append(ch)
  # end for

  if not open_seq and perfect:
    print 'All parentheses match properly'
  else:
    print 'Parentheses don\'t math properly'
# end main

if __name__ == '__main__':
  main()
