"""Team Python Prac Q3.

Write a function updateInventory() that takes two 2D arrays as parameters,
curInv and newInv.
Compare and update the current inventory stored in a 2D array against the
second 2D array of a new inventory. Update the current existing inventory item
quantities (in cuIn). If an item cannot be found, add the new item and quantity
into the inventory array. The returned inventory array should be in
alphabetical order by item.


Sample Input

​​curInv = [[21, "Bowling Ball"], [2, "Dirty Sock"], [1, "Hair Pin"], [5, "Microphone"]]

newInv = [[2, "Hair Pin"], [3, "Half-Eaten Apple"], [67, "Bowling Ball"], [7, "Toothpaste"]]

updateInventory(curInv, newInv)

Sample Output

​​[[88, "Bowling Ball"], [2, "Dirty Sock"], [3, "Hair Pin"], [3, "Half-Eaten Apple"], [5, "Microphone"], [7, "Toothpaste"]]
"""


def main():
  curInv = input('Enter current inventory: ')
  newInv = input('Enter new inventory: ')
  updateInventory(curInv, newInv)

def updateInventory(curInv, newInv):
  temp = {}
  for item in curInv:
    temp[item[1]] = item[0]

  for item in newInv:
    temp[item[1]] = temp[item[1]] + item[0] if item[1] in temp else item[0]

  curInv = []
  for key in sorted(temp):
    curInv.append([key, temp[key]])
  print curInv
  return curInv


if __name__ == '__main__':
  main()
