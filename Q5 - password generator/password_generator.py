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
    'length': 0,
    'min_upper': 0,
    'max_upper': 0,
    'min_lower': 0,
    'max_lower': 0,
    'min_digit': 0,
    'max_digit': 0,
    'min_special': 0,
    'max_special': 0,
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
  password_type = input('Enter 1 for simple password, 2 for complex')
  parameters['length'] = input('Length of Passowrd')
  parameters['min_upper'] = input('Min no of Upper Characters')
  parameters['max_upper'] = input('Max no of Upper Characters')
  parameters['min_lower'] = input('Min no of Lower Characters')
  parameters['max_lower'] = input('Max no of Lower Characters')
  if password_type == 2:
    parameters['min_digit'] = input('Min no of Digits')
    parameters['max_digit'] = input('Max no of Digits')
    parameters['min_special'] = input('Min no of Special Characters')
    parameters['max_special'] = input('Max no of Special Characters')

  # Making sure that at least one of each type exists
  parameters['min_upper'] = 1 if parameters['min_upper'] == 0 and parameters['max_upper'] > 0 else parameters['min_upper']
  parameters['min_lower'] = 1 if parameters['min_lower'] == 0 and parameters['max_lower'] > 0 else parameters['min_lower']
  if password_type == 2:
    parameters['min_digit'] = 1 if parameters['min_digit'] == 0 and parameters['max_digit'] > 0 else parameters['min_digit']
    parameters['min_special'] = 1 if parameters['min_special'] == 0 and parameters['max_special'] > 0 else parameters['min_special']

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
