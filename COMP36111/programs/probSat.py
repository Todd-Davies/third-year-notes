from functools import partial
import random

# Important definitions!
T = True
F = False

# (x or ~y)
clause1 = [('x',T),('y',F)]
# (z or y)
clause2 = [('z',T),('y',T)]
# (~x or ~y)
clause3 = [('x',F),('z',F)]
# x = 1, y = 1, z = 0
assignment1 = {'x':T, 'y':T, 'z':F}

def evalClause(clause, assignment):
  """
  Evaluates a single clause
  """
  values = map(lambda x: x[1] == assignment[x[0]], clause)
  return reduce(lambda x, y: x or y, values)

def sat(clauses, assignment):
  """
  Evaluates a list of clauses
  """
  evaluateAsn = partial(evalClause, assignment=assignment)
  return reduce(lambda x, y: x and y, map(evaluateAsn, clauses))

def genClause(k, literals, out=[]):
  """
  Generates a random (satisfiable) clause of length k from the literals you give
  it.
  """
  if k == 0 or literals == []:
    return out
  else:
    literal = literals.pop(0)
    out.append((literal, bool(random.getrandbits(1))))
    genClause(k - 1, literals, out)
    literals.append(literal)
    return out

def genManyClauses(m, k, literals, out=[]):
  """
  Generates m clauses
  """
  if m == 0:
    return out
  else:
    out.append(genClause(k, literals))
    return genManyClauses(m - 1, k, literals, out)

def genTruthAssignment(literals):
  """
  Generates a random truth assignment
  """
  randomAssignment = lambda literal: (literal, bool(random.getrandbits(1)))
  return dict(map(randomAssignment, literals))

def genLiterals(n):
  """
  Generates a list of n literals
  """
  return map(lambda x: chr(97 + x), range(0, n))

def numEvalTrue(n, k, m, iterations):
  """
  Generates m random clauses of length k from n literals, generates a truth
  value and records if it was true
  Does this 'iterations' times
  """
  out = 0
  for i in range(0, iterations):
    literals = genLiterals(n)
    print literals
    assignment = genTruthAssignment(literals)
    print assignment
    print "\n"
    clauses = genManyClauses(m, k, literals)
    print clauses
    if sat(clauses, assignment):
      out += 1
  return out