"""Q17
"""

import hashlib
import os

# path = input("Enter Path: ")
path = '/home/guakhil/Desktop/TEMP/DupeFiles'

candidates = {}

def cleanDict(d):
  keys = []
  for k in d:
    if len(d[k]) < 2:
      keys.append(k)

  for x in keys:
    del d[x]

print path
# Filter on Size
for root, dirs, files in os.walk(path):
  for f in files:
    size = os.path.getsize(os.path.join(root, f))
    if size not in candidates: candidates[size] = []
    candidates[size].append(f)
  # print candidates, '\n'*3

cleanDict(candidates)

# Filter on increasing chunks of Content
for i in xrange(1, 6):
  chunkSize = 10**i
  new_candidtes = {}
  for key in candidates:
    while len(candidates[key]):
      file = candidates[key].pop()
      with open(os.path.join(path, file), 'rb') as f:
        chunkKey = hashlib.md5(f.read(chunkSize)).hexdigest()
        if chunkKey not in new_candidtes: new_candidtes[chunkKey] = []
        new_candidtes[chunkKey].append(file)
  # print new_candidtes, '\n'*3
  candidates = new_candidtes
  cleanDict(candidates)

# Final Verdict
final = {}
for key in candidates:
  while len(candidates[key]):
    file = candidates[key].pop()
    md5 = hashlib.md5()
    with open(os.path.join(path, file), 'rb') as f:
      while True:
        data = f.read(128)
        if not data: break
        md5.update(data)
    new_key =  md5.hexdigest()
    if new_key not in final: final[new_key] = []
    final[new_key].append(file)

cleanDict(final)
output = []
for group_key in final:
  print 'Group:\n', '\n'.join(final[group_key]), '\n'
  output.append(final[group_key])
print output
