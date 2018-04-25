a = [
  [1,2,3],
  [4,5,6],
  [7,8,9],
]

a = [
  [1,5],
  [5,1],
]

d1 = 0
d2 = 0
n = len(a)

for i in xrange(n):
  d1 += a[i][i]
  d2 += a[i][n - i - 1]


print d1, d2
