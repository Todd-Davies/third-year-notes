#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Simple example of page rank (as used for Word Sense Disambugation in COMP34411)
"""

# For reading from stdin and checking args
import sys
# For finding the max
import operator
# For error checking
import math

# Check we've got two words as command line arguments
if len(sys.argv) != 1:
  print "Usage: %s" % sys.argv[0]
  exit(-1)

# Make up a graph
graph = {"finance":["river"],
         "flying":["train-station","river","finance"],
         "train-station":["flying","river"],
         "river":["train-station","flying"]}

# The graph is like:
#
# Finance ------------> River
#   ▲                 /   ▲
#   |    -------------    |
#   |  /                  ▼
# Train-Station <-----> Flying
#

# Set the damping factor to 0.8
damping = 0.8

# Reserve 0.2 probability mass for personalisation
personalise_amnt = 0.3
# Set the personalisation terms (from a target sentence) to point to finance
personalise = {"money":["finance"],
               "loan":["finance"]}

def page_rank(graph, damping, personalise, personalise_amnt):
  starting_prob = 1.0 / len(graph)
  # Build the initial scores
  scores = {k: starting_prob for k, v in graph.items()}
  print scores
  prev_scores = None
  # Keep going while the scores aren't stable
  while not prev_scores or scores != prev_scores:
    # Move the current scores to the prev_scores and reset the current scores
    prev_scores = scores
    scores = {}
    # Find the new score for each key
    for k in graph.keys():
      # Compute the personalisation
      p = 0
      for extra in personalise.keys():
        if k in personalise[extra]:
          p += (personalise_amnt / len(personalise)) / len(personalise[extra])
      # Compute the damping addition
      d = (1.0 - damping) / len(graph.items())
      # Compute the input from other nodes
      s = 0
      for node in graph.keys():
        if k in graph[node]:
          s += prev_scores[node] / len(graph[node])
      # Multiply s to take out the amount we're using for damping and
      # personalisation
      s *= damping - personalise_amnt
      # Add the bits up to get the score
      scores[k] = p + d + s
    print scores
  print "Finished!"
  return scores

# Compute the scores
scores = page_rank(graph, damping, personalise, personalise_amnt)

# Print out the top score
print "Top score: %s" % max(scores.iteritems(), key=operator.itemgetter(1))[0]

# Check that the values sum to ~1
summation = reduce(lambda x, y: x + y, scores.values())
if summation < 0.99 or summation > 1.01:
  print "Something went wrong; sum = %f" % summation
