# @ moyja

########################################################################################################################

# 1: imports

import contextlib
import collections
import copy
import gc
import glob
import itertools as it
import matplotlib as mpl
import matplotlib.cm as mcm
import matplotlib.colors as mpc
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as nra
import numpy.linalg as nla
import os
import pandas as pd
import pickle as pk
#import pynverse
import re
import scipy as sp
import scipy.linalg as sla
import scipy.sparse as sps
import sys
import time

from collections import Counter, defaultdict
from copy import deepcopy
from matplotlib.animation import FuncAnimation
from matplotlib.pyplot import imshow, plot

from numpy import ( angle, arange, arccos, array, arcsin, arctan, arctan2, arctanh, argsort,
                   clip, concatenate, conj, cos, cosh, cumsum, diag, diagonal,
                   einsum, exp, eye, fill_diagonal, flip, imag, ix_, kron,
                   linspace, log, logical_and, logical_not, logical_or, logical_xor, logspace,
                   mean, median, meshgrid, nan_to_num, ones, pi, quantile, real, repeat, rint,
                   sin, sinh, sqrt, std, swapaxes,
                   tan, tanh, tile, trace, unique, vectorize, where, zeros )
from numpy.linalg import norm
from numpy.random import binomial, rand, randint, randn

#from pynverse import inversefunc

from queue import PriorityQueue

from scipy.linalg import null_space, orth, sqrtm
from scipy.sparse import csgraph, csr_array, diags, eye as speye, kron as sparkron, lil_array
from scipy.special import comb, erf, erfinv, expit, factorial, logsumexp, lambertw
from scipy.stats import entropy

########################################################################################################################

# 2: clocks

def clockface(seconds):
    seconds = int(seconds)
    hours = seconds//3600
    seconds -= 3600 * hours
    minutes = seconds//60
    seconds -= 60 * minutes
    houstr = str(hours)
    minstr = str(minutes)
    secstr = str(seconds)
    if seconds <= 9:
        secstr = '0' + secstr
    if minutes <= 9:
        minstr = '0' + minstr
    if hours == 0:
        if minutes == 0:
            if seconds == 0:
                return ''
            else:
                return str(seconds)
        else:
            return str(minutes) + ':' + secstr
    else:
        return houstr + ':' + minstr + ':' + secstr
'''    
def initialize_clock():
    global MY_TIMES
    global pastpoint
    MY_TIMES = {}
    pastpoint = 0
''' 
def oof_bar(i, N):
    # note that a must be zero to start
    global last_oof
    if i == 0:
        tic(name = 'oof')
        last_oof = .0
    elif i == N-1:
        print()
    elif i/N > last_oof + .001:
        last_oof = i/N
        print('\r' + str(i) + ' / ' + str(N) + ' | t = ' + str(toc(1, name = 'oof')), end ='\r')
    
def nubar(p, barname = 'bar'):
    # note that a must be zero to start
    global pastpoint
    L = 60
    
    if p > 1:
        raise Exception('bar out of bounds')
        
    elif p == 0:        
        tic(name = barname)
        pastpoint = 0

    elif L*p - pastpoint > .5:
        pastpoint = int(rint(L*p))
        elapsed = toc(out_state = 1, name = barname)
        remaining = (1/p-1)*elapsed
        now_time = clockface(elapsed)
        fut_time = clockface(remaining)
        bar = ' '*(7-len(now_time)) + now_time + '  '
        if pastpoint == L:
            print('\r' + bar + 'X' + ' '*(L-4) + chr(187) + '--X      ')
            #MY_TIMES.pop(barname)
        else:
            if pastpoint >= 4:
                bar += '>' + ' '*(pastpoint-4) + chr(187) + '-->' + ' '*(L-1-pastpoint) + '<'
            elif pastpoint == 3:
                bar += '>' + '-->' + ' '*(L-4) + '<'
            elif pastpoint == 2:
                bar += '>' + '->' + ' '*(L-3) + '<'
            elif pastpoint == 1:
                bar += '>' + '>' + ' '*(L-2) + '<'
            elif pastpoint == 0:
                bar += '>' + ' '*(L-1) + '<'
            print('\r' + bar + '  ' + fut_time + '    ', end ='\r')


def tic(out_state = 0, name = 'yommytime'):
    # out_state = 0 if silent, 1 if returning elapsed time, 2 if printing elapsed time
    global MY_TIMES
    
    if 'MY_TIMES' not in globals():
        MY_TIMES = {}
    
    if out_state == 0:
        MY_TIMES[name] = time.time()
    elif out_state == 1:
        hold = MY_TIMES[name]
        MY_TIMES[name] = time.time()
        return MY_TIMES[name] - hold
    elif out_state == 2:
        hold = MY_TIMES[name]
        MY_TIMES[name] = time.time()
        print('TIME: ', name, ' :  delta  = ', MY_TIMES[name] - hold)
    else:
        raise Exception('unidentified outstate')
        

def toc(out_state = 2, name = 'yommytime'):
    # out_state = 0 if silent, 1 if returning elapsed time, 2 if printing elapsed time
    if out_state == 1:
        return(time.time() - MY_TIMES[name])
    elif out_state == 2:
        print('TIME: ', name, ' = ', time.time() - MY_TIMES[name])
    else:
        raise Exception('unidentified outstate')

########################################################################################################################