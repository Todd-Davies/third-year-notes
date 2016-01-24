#!/usr/bin/python

# For log
import math

graph = {0 : [1,3,4],
         1 : [0,2],
         2 : [1,3],
         3 : [0,2],
         4 : [0]}

def is_reachable(start, end, graph, steps):
  print "is_reachable(%d, %d, graph, %d)" % (start, end, steps)
  if steps == 0:
    return start == end or (end in graph[start])
  else:
    for adj in graph[start]:
      if is_reachable(start, adj, graph, steps - 1):
        if is_reachable(adj, end, graph, steps - 1):
          return True
    return False

print is_reachable(0, 3, graph, int(math.log(len(graph), 2))) # True
print is_reachable(4, 2, graph, int(math.log(len(graph), 2))) # False