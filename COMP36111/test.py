sizeSet = {}
mapping = {}

def makeSet(a):
  mapping[a] = [a]
  sizeSet[a] = 1

def find(a):
  return mapping[a]

def union(a,b):
  aSet = find(a)
  bSet = find(b)
  # If the elements are in the same set, return
  if aSet[0] == bSet[0]:
    return aSet
  if sizeSet[aSet[0]] < sizeSet[bSet[0]]:
    (s,l) = (aSet, bSet)
  else:
    (s,l) = (bSet, aSet)
  l.extend(s)
  sizeSet[l[0]] = sizeSet[l[0]] + sizeSet[s[0]]
  for element in s:
    mapping[element] = l
  return l

makeSet(1)
makeSet(2)
makeSet(3)
makeSet(4)

find(1)
find(2)
find(3)
find(4)

union(1,2)
union(2,3)
union(1,3)

