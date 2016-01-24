#!/usr/bin/python

graph = {0 : [1,3,4],
         1 : [0,2],
         2 : [1,3],
         3 : [0,2],
         4 : [0]}

def build_matrix(graph):
  # Matrix size
  m_size = len(graph)
  # Initialise a matrix of all -1's
  matrix = [[-1 for x in range(m_size)] for x in range(m_size)]
  # Set the matrix values
  for row in graph.keys():
    for col in graph.keys():
      matrix[row][col] = (1 if (col in graph[row]) else 2)
  # Make a list for the solution
  solution = []
  # TODO: Solve TSP here
  print matrix

build_matrix(graph)