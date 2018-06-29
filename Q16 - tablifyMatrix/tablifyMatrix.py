"""Q16

Write a function that accepts any NxM matrix (list of lists) as an input, and then displays it in a tabular form as :
1 - Use hyphen(-) for horizontal lines
2 - Use pipe (|) for vertical lines
3 - All cells in the table should be off the same size
4 - The content in each cell should be padded with at least 1 space on both sides
5 - All cells should be center aligned
 
Eg.
 
Input:
[[1, 22], [333, 4444]]
 
Output:
---------------
|  1   |  22  |
---------------
| 333  | 4444 |
---------------
 
 
Input:
[["Name", "Age"], ["ABC", 32], ["xyz", 5]]
 
Output:
---------------
| Name | Age  |
---------------
| ABC  |  32  |
---------------
| xyz  |  5   |
---------------
"""

a = [[1, 22], [333, 4444]]
a = [['Name', 'Age'], ['ABC', 32], ['xyz', 5]]

def tablifyMatrix(a):
  max = 0
  for x in a:
    for y in x:
      max = len(str(y)) if len(str(y)) > max else max
  
  hr = '-' * ((max+3) * len(a[0]) + 1)
  print hr

  for x in a:
    print '|',
    for y in x:
      print ('{0:^'+str(max)+'}').format(y), '|',
    print '\n', hr

tablifyMatrix(a)
