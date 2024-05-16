# @ moyja

########################################################################################################################

import time

########################################################################################################################

def clockface(seconds):
    # returns time appropriately in hh : mm : ss, mm : ss, or ss format
    seconds = int(seconds)
  
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
  
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
                return '<1s'
            else:
                return str(seconds)
        else:
            return str(minutes) + ':' + secstr
    else:
        return houstr + ':' + minstr + ':' + secstr
    
def xbar(p, name = 'sexbar'):
    # note that p must be zero to start
    global pastpoint
    L = 60
    
    if p > 1 or p < 0:
        raise Exception('bar out of bounds')
    elif p == 0:        
        tic(name = name)
        pastpoint = 0
    elif L*p - pastpoint > .5:
        pastpoint = int(rint(L*p))
        elapsed = toc(print_time = False, name = name)
        remaining = (1/p-1)*elapsed
        now_time = clockface(elapsed)
        fut_time = clockface(remaining)
        bar = ' '*(7-len(now_time)) + now_time + '  '
        if pastpoint == L:
            print('\r' + bar + 'X' + ' '*(L-4) + chr(187) + '--X      ')
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
    MY_TIMES[name] = time.time()
    time_diff =  MY_TIMES[name] - last_time
  
    if print_time:
        print('TIME: ', name, ' :  delta  = ', time_diff)
    return MY_TIMES[name] - hold
    
def toc(print_time = True, name = 'yommytime'):
    time_diff =  time.time() - MY_TIMES[name]
  
    if print_time:
        print('TIME: ', name, ' :  delta  = ', time_diff)
    return time_diff

########################################################################################################################
