""" Q. 11

Input -> Roman numerals like XV, XVI, XIV, LV
Output -> 15, 16, 14, 55

Code Constraints :-
    Should work for all available roman numerals
    Should be pythonic
"""


ROMAN_VALUES = {
  'I' : 1,
  'V' : 5,
  'X' : 10,
  'L' : 50,
  'C' : 100,
  'D' : 500,
  'M' : 1000,
}

def toNonRetardNumber(rom_num):
  n = 0
  l = len(rom_num)
  for i in xrange(l - 1):
    if ROMAN_VALUES[rom_num[i]] < ROMAN_VALUES[rom_num[i+1]]:
      n -= ROMAN_VALUES[rom_num[i]]
    else:
      n += ROMAN_VALUES[rom_num[i]]
  n += ROMAN_VALUES[rom_num[l-1]]
  return n

print '{0:<5}:{1:<10}: '.format(15, 'XV'),  toNonRetardNumber('XV')
print '{0:<5}:{1:<10}: '.format(16, 'XVI'),  toNonRetardNumber('XVI')
print '{0:<5}:{1:<10}: '.format(15, 'XIV'),  toNonRetardNumber('XIV')
print '{0:<5}:{1:<10}: '.format(14, 'LV'),  toNonRetardNumber('LV')
print '{0:<5}:{1:<10}: '.format(55, 'I'),  toNonRetardNumber('I')
print '{0:<5}:{1:<10}: '.format(5, 'V'),  toNonRetardNumber('V')
print '{0:<5}:{1:<10}: '.format(41, 'XLI'),  toNonRetardNumber('XLI')
print '{0:<5}:{1:<10}: '.format(91, 'XCI'),  toNonRetardNumber('XCI')
print '{0:<5}:{1:<10}: '.format(999, 'CMXCIX'),  toNonRetardNumber('CMXCIX')
print '{0:<5}:{1:<10}: '.format(565, 'DLXV'),  toNonRetardNumber('DLXV')
print '{0:<5}:{1:<10}: '.format(384, 'CCCLXXXIV'),  toNonRetardNumber('CCCLXXXIV')
