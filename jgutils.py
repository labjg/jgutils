#!/usr/bin/env python

"""
Some useful functions for doing handy stuff. According to @labjg, anyway..
"""

import numpy as np

def rms(data):
    """Return RMS of a numpy array of values/samples.

    Args:
        data: A numpy array of values/samples

    Returns:
        The RMS value of the input values.
    """
    return np.sqrt(np.mean(np.square(data)))

def mag(x, y):
    """Return the magnitude of two orthogonal components.

    Args:
        x: First component
        y: Second component

    Returns:
        The magnitude of the two orthogonal components.
    """
    return np.sqrt(np.square(x)+np.square(y))

def euclidean(xy1, xy2):
    """Return the Euclidean distance between two pairs of (x,y) coordinates.
    
    Args:
        xy1: First pair of coordinates as a tuple (x,y)
        xy2: Second pair of coordinates as a tuple (x,y)

    Returns:
        The Euclidean distance, in whatever unit the inputs were in.
    """
    delta_x = xy1[0] - xy2[0]
    delta_y = xy1[1] - xy2[1]
    delta = np.sqrt(np.square(delta_x) + np.square(delta_y))
    return delta
