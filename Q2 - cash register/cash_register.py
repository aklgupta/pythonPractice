"""Team Practice Question 2.

Design a cash register drawer function ​​checkCashRegister that accepts purchase price as the first argument (price), payment as the second argument (cash), and cash-in-drawer (cid) as the third argument.​ ​cid is a 2D array listing available currency.

Return the string "Insufficient Funds" if cash-in-drawer is less than the change due. Return the string "Closed" if cash-in-drawer is equal to the change due.​ ​Otherwise, return change in coin and bills, sorted in highest to lowest order.

​Sample Input:
​​price = 19.50
cash =20.00
cid = [["PENNY", 1.01], ["NICKEL", 2.05], ["DIME", 3.10], ["QUARTER", 4.25], ["ONE", 90.00], ["FIVE", 55.00], ["TEN", 20.00], ["TWENTY", 60.00], ["ONE HUNDRED", 100.00]])

Sample Output :
​​[ [ 'QUARTER', 0.5 ] ]

"""

import collections

currencies_map = {
  'ONE HUNDRED': 100,
  'TWENTY': 20,
  'TEN': 10,
  'FIVE': 5,
  'ONE': 1,
  'QUARTER': 0.25,
  'DIME': 0.1,
  'NICKEL': 0.05,
  'PENNY': 0.01,
}

def main():
  price = input('Enter total price/bill: ')
  cash = input('Enter the amount of cash given: ')
  cid = input('Enter a list of list, cash in drawer: ')
  checkCashRegister(price, cash, cid)


def checkCashRegister(price, cash, cid):
  change = 0
  change_req = cash - price
  temp_cid = {}
  for c in cid:
    change += c[1]
    temp_cid[c[0]] = c[1]
  cid = temp_cid

  if change < change_req:
    print 'Insufficient Funds'
    return

  if change == change_req:
    print 'Closed'
    return

  currencies = collections.OrderedDict(sorted(currencies_map.items(), key=lambda t: t[1], reverse=True))
  denomination = collections.OrderedDict()
  collected = 0
  for key in currencies:
    if key in cid:
      while cid[key] and collected + currencies[key] <= change_req:
        collected += currencies[key]
        denomination[key] = denomination[key] + 1 if key in denomination else 1
        cid[key] -= currencies[key]

  result = []
  for k, v in denomination.items():
    print k, ' x ', v, ' = ', currencies[k]*v
    result.append([k, currencies[k]*v])

  print result


if __name__ == '__main__':
  main()
