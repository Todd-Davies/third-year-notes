#!/bin/python2.7

"""
Basic implementation of Thompson's NFA -> DFA algorithm
"""

from functools import reduce
from pprint import pprint

nfa = {
  0 : {"" : {1}},
  1 : {"a": {0,2}, "b" : {0}},
  2 : {"a": {3}, "b":{3}},
  3 : {}
}

accepting = {3}

def accept_nfa(nfa, acceptingStates, inputStr, currentState=0):
  if inputStr == None or len(inputStr) == 0:
    return currentState in acceptingStates
  char = inputStr[0]
  transitions = nfa[currentState][char] if char in nfa[currentState] else {}
  epsilons = nfa[currentState][""]  if "" in nfa[currentState] else {}
  for nextState in transitions:
    if accept_nfa(nfa, acceptingStates, inputStr[1:], nextState):
      return True
  for nextState in epsilons:
    if accept_nfa(nfa, acceptingStates, inputStr, nextState):
      return True
  return False

def e_closure(nfa, states, seen = []):
  if str(states) in seen:
    return set()
  out = set(states)
  for state in states:
    immediateClosure = nfa[state][""] if "" in nfa[state] else set()
    neighbourClosures = set()
    for s in immediateClosure:
      neighbourClosures = neighbourClosures.union(e_closure(nfa, [s], seen + [str(states)]))
    out = out.union(immediateClosure.union(neighbourClosures))
  return out

def move(nfa, states, transition):
  out = set()
  for state in states:
    if transition in nfa[state]:
      out = out.union(nfa[state][transition])
  return out

def mapping(input_set, names):
  if repr(input_set) not in names:
    current = max(list(names.values()) + [-1]) + 1
    names[repr(input_set)] = current
  return chr(ord('a') + names[repr(input_set)])

def nfa_subset(nfa, initial):
  names = {}
  output = {}
  input_symbols = map(lambda x: nfa[x].keys(), nfa.keys())
  input_symbols = set(reduce(lambda x, y: set(x).union(set(y)), input_symbols))
  input_symbols.remove("")
  DStates = [e_closure(nfa, initial)]
  marked = []
  unmarked = filter(lambda x: x not in marked, DStates)
  while len(unmarked) > 0:
    t = unmarked.pop()
    marked.append(t)
    for symbol in input_symbols:
      u = e_closure(nfa, move(nfa, t, symbol))
      if u not in DStates:
        DStates.append(u)
      if symbol != "" and not t == set():
        if mapping(t, names) in output:
          output[mapping(t, names)][symbol] = mapping(u, names)
        else:
          output[mapping(t, names)] = {symbol:mapping(u, names)}
    unmarked = filter(lambda x: x not in marked, DStates)
  print names
  print map(lambda x: (x, chr(ord('a') + x)), names.values())
  return output

pprint(nfa_subset(nfa, [0]))
