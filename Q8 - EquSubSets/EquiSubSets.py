a = [1, 5, 11, 5]

L = len(a)
N = sum(a)/2
X = 0;

subs = []

def suber(x = 0):
  global subs, X, L, N, a
  
  if x >= L:
    return
  
  n = len(subs)
  for i in xrange(n):
    subs.append(list(subs[i]))
    subs[i + n].append(a[x])
  subs.append([a[x]])
  x += 1
  suber(x)


  
suber()

for x in subs:
  if sum(x) == N:
    print "ans", x
