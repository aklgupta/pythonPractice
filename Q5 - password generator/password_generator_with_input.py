"""Q5.

Write a programme to generate a simple as well as a complex password.
Note: A simple password has only lowercase and uppercase alphabets whereas a
complex one has all alphabets, digits and special characters.
The problem should also implement the following functionalities:
1.) Min and max length of the password
2.) Min and max length of the uppercase characters.
3.) Min and max length of the lowercase characters.
4.) Min and max length of the digits.
5.) Min and max length of the special characters.
"""

import random

parameters = {
    'length': 25,
    'min_upper': 2,
    'max_upper': 5,
    'min_lower': 2,
    'max_lower': 5,
    'min_digit': 2,
    'max_digit': 10,
    'min_special': 1,
    'max_special': 5,
}


def get_upper():
  return chr(65 + random.randint(0, 25))


def get_lower():
  return chr(97 + random.randint(0, 25))


def get_digit():
  return chr(48 + random.randint(0, 9))


def get_special():
  # I am not making for all special chars...
  # (*_*)
  return chr(33 + random.randint(0, 15))


def main():

  # Initially storing password as a string
  password = []

  # Checking if Password length is too small
  if(
      parameters['min_lower'] + parameters['min_upper']
      + parameters['min_digit'] + parameters['min_special']
      >= parameters['length']
  ):
    print 'Mininum Inputs Exceed length of the Password'
    raw_input()
    exit()

  # Checking if Password length is too big
  if(
      parameters['max_lower'] + parameters['max_upper']
      + parameters['max_digit'] + parameters['max_special']
      < parameters['length']
  ):
    print 'Maximum Inputs are less than length of the Password'
    raw_input()
    exit()



  # Adding Minimum no. of chars of all types
  password.extend([get_lower() for _ in xrange(parameters['min_lower'])])
  password.extend([get_upper() for _ in xrange(parameters['min_upper'])])
  password.extend([get_digit() for _ in xrange(parameters['min_digit'])])
  password.extend([get_special() for _ in xrange(parameters['min_special'])])

  # Subtracting min_counts from max_counts
  parameters['max_lower'] -= parameters['min_lower']
  parameters['max_upper'] -= parameters['min_upper']
  parameters['max_digit'] -= parameters['min_digit']
  parameters['max_special'] -= parameters['min_special']

  while len(password) < parameters['length']:
    # Selecting any one char type randomly
    choices = ['max_lower', 'max_upper', 'max_digit', 'max_special']
    selection = random.choice(choices)

    # If that char type's limit has not been reached yet,
    # then add a char of that type
    if parameters[selection]:
      if selection == 'max_lower':
        ch = get_lower()
      elif selection == 'max_upper':
        ch = get_upper()
      elif selection == 'max_digit':
        ch = get_digit()
      elif selection == 'max_special':
        ch = get_special()
      password.extend(ch)
      parameters[selection] -= 1

  # Shuffling the chars position randomly
  random.shuffle(password)
  print ''.join(password)


if __name__ == '__main__':
  main()
