#!/usr/bin/python

"""
  Make Copies of points sorted by:
    x coordinate 
    y coordinate
  Use divide & conquer approach
    Get half points on left, half on right of line in the middle of graph. Xbar (median of the points by their x coordinate).
"""


def closest_pair(px,py):
    midx = len(px) / 2
    q = px[:midx]
    r = px[:midx]
