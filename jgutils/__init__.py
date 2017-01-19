#!/usr/bin/env python

"""
Some useful functions for doing handy stuff. According to @labjg, anyway..
"""

import os
import numpy as np

def mkdir(path):
    """Check if a directory exists, create it if not, and return the complete
    path with a guaranteed trailing forward slash.

    Args:
        path: Absolute path of desired directory, as a string.

    Returns:
        The absolute path with a guaranteed trailing '/', as a string.
    """
    path = os.path.abspath(path)
    if not path[-1] == '/':
        path += '/'
    if not os.path.exists(path):
        os.makedirs(path)
    return path

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

def find_peaks(data, minHeight=0, minDist=0, minWidth=0):
    """Return a height-ordered list of peak positions in a data series.

    This works by first finding the tallest peak in the series, then finding
    the second- and third-tallest and so on.  The position of the each peak is
    added to the returned list of peak positions only if that peak is: a) above
    the specified minimum height threshold; b) separated from previously-
    detected peaks by at least the specified minimum distance; and c) wider
    than the specified minimum full width at half maximum (FWHM).

    Args:
        data: the data series as a numpy array
        minHeight: Minimum height threshold
        minDist: Minimum separation threshold
        minWidth: Minimum FWHM threshold

    Returns:



    WORK IN PROGRESS


    """

