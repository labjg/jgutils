# Some useful utility functions for doing handy stuff
# Useful according to James Gilbert (labjg), anyway..

import numpy as np


def rms(data):
    """Return RMS of a numpy array of values/samples"""
    return np.sqrt(np.mean(np.square(data)))

def getMag(x, y):
    return np.sqrt(np.square(x) + np.square(y))
