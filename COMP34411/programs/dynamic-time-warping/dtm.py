#!/usr/bin/python

# For reading from stdin and checking args
import sys

# Check we've got two words as command line arguments
if len(sys.argv) != 3:
  print "Usage: %s <word> <word>" % sys.argv[0]
  exit(-1)

# Pad the words with a placeholder to represent the empty string
word1 = 'X' + sys.argv[1]
word2 = 'X' + sys.argv[2]

# Initialise a matrix of all -1's
matrix = [[-1 for x in range(len(word2))] for x in range(len(word1))] 
# Set the comparison of empty strings to 0
matrix[0][0] = 0

# Define what each transformation costs. Swap = 3, add = 2, del = 2
diffMap = {(-1,-1):3,(0,-1):2,(-1,0):2}

def getLowestCell(matrix, i, j):
  """
  Get the offset with the lowest valued cell inside
  """
  isSet = False
  smallest = 0
  coords = diffMap.get(0)
  # For each offset entry
  for diff in diffMap.keys():
    # Compute the coords
    x = i + diff[0]
    y = j + diff[1]
    # If we're within the bounds
    if x >= 0 and x < len(word2) and y >= 0 and y < len(word1):
      # Get the cell value
      element = matrix[y][x]
      # If its smaller than our best, or its the first one
      if element < smallest or not isSet:
        # Set it to smallest
        smallest = element
        coords = diff;
        isSet = True
  # Return the offset that had the lowest value
  return coords

def printMatrix(matrix):
  """
  Pretty prints the matrix
  """
  print "   " + "  ".join(word2)
  x = 0
  for line in matrix:
    output = ""
    output += word1[x] + " "
    x += 1
    for num in line:
      output += "%2d " % num
    print output

# Iterate through the words
for j in range(0, len(word1)):
  for i in range(0, len(word2)):
    # Ignore (0,0), we did that at the beginning
    if i == 0 and j == 0:
      continue
    else:
      # Find the lowest neighbour (above left, left or above)
      coords = getLowestCell(matrix, i, j)
      # If the letter is equal, and it was diagonal
      if word1[j] == word2[i] and coords == (-1,-1):
        # Same value
        matrix[j][i] = matrix[j + coords[1]][i + coords[0]]
      else:  
        # Else, value plus the cost
        matrix[j][i] = matrix[j + coords[1]][i + coords[0]] + diffMap[coords]
    # Wait for the user input, then print the matrix
    try:
      input("Press enter")
    except SyntaxError:
      pass
    finally:
      printMatrix(matrix)