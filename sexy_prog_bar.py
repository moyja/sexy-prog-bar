# @ moyja

########################################################################################################################

# 1: imports

import numpy as np
import time

from numpy import ( angle, arange, arccos, array, arcsin, arctan, arctan2, arctanh, argsort,
                   clip, concatenate, conj, cos, cosh, cumsum, diag, diagonal,
                   einsum, exp, eye, fill_diagonal, flip, imag, ix_, kron,
                   linspace, log, logical_and, logical_not, logical_or, logical_xor, logspace,
                   mean, median, meshgrid, nan_to_num, ones, pi, quantile, real, repeat, rint,
                   sin, sinh, sqrt, std, swapaxes,
                   tan, tanh, tile, trace, unique, vectorize, where, zeros )

########################################################################################################################

# 2: clocks

def clockface(seconds):
    # returns time appropriately in hh : mm : ss, mm : ss, or ss format
  
    seconds = int(seconds)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    if hours == 0:
        if minutes == 0:
            if seconds == 0:
                return '<1s'
            else:
                return str(seconds)
        else:
            return str(minutes) + ':' + secstr
    else:
        return houstr + ':' + minstr + ':' + secstr

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
    
def xbar(p, barname = 'bar'):
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


def tic(print_time = False, name = 'yommytime'):
    global MY_TIMES
    if 'MY_TIMES' not in globals():
        MY_TIMES = {}

    last_time = MY_TIMES[name]
    MY_TIMES[name] = time.perf_counter()
    time_diff =  MY_TIMES[name] - last_time
  
    if print_time:
        print('TIME: ', name, ' :  delta  = ', time_diff)
    return MY_TIMES[name] - hold
    
def toc(print_time = True, name = 'yommytime'):
    time_diff =  time.perf_counter() - MY_TIMES[name]
  
    if print_time:
        print('TIME: ', name, ' :  delta  = ', time_diff)
    return time_diff

########################################################################################################################
