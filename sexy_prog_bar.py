# @ moyja

# I think I may need to do something so when i run this on gpu it doesnt have to spend all this time finding the global variables

########################################################################################################################

import time

########################################################################################################################

MY_TIMES = {}
PAST_POINTS = {}

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
    if name not in PAST_POINTS:
        PAST_POINTS[name] = 1

    L = 50
    num_updates = 10000
    if p > 1 or p < 0:
        raise Exception('bar out of bounds')
    
    if p < PAST_POINTS[name]: # implying that we are starting a new bar
        tic(name = name)
        PAST_POINTS[name] = p
    elif p - PAST_POINTS[name] > 1 / num_updates:
        PAST_POINTS[name] = p
        tick = int(L * p)
        elapsed = toc(print_time = False, name = name)
        remaining = (1 / p - 1)*elapsed
        now_time = clockface(elapsed)
        fut_time = clockface(remaining)

        bar = '  ' + now_time + '  '
        
        if tick >= L - 1:
            bar += 'X' + ' '*(L-6) + chr(187) + '--X'
        elif tick >= 4:
            bar += '>' + ' '*(tick - 5) + chr(187) + '-->' + ' '*(L - 2 - tick) + '<'
        elif tick == 3:
            bar += '>' + '-->' + ' '*(L-5) + '<'
        elif tick == 2:
            bar += '>' + '->' + ' '*(L-4) + '<'
        elif tick == 1:
            bar += '>' + '>' + ' '*(L-3) + '<'
        elif tick == 0:
            bar += '>' + ' '*(L-2) + '<'

        print('\r' + bar + '  ' + fut_time + '  ', end = '')

def tic(print_time = False, name = 't'):
    if name not in MY_TIMES:
        MY_TIMES[name] = time.time()

    last_time = MY_TIMES[name]
    MY_TIMES[name] = time.time()
    time_diff =  MY_TIMES[name] - last_time
  
    if print_time:
        if time_diff < 1:
            print('TIME: ', name, ' = ', time_diff)
        else:
            print('TIME: ', name, ' = ', clockface(time_diff))

    return time_diff
    
def toc(print_time = True, name = 't'): 
    time_diff =  time.time() - MY_TIMES[name]
  
    if print_time:
        if time_diff < 1:
            print('TIME: ', name, ' = ', time_diff)
        else:
            print('TIME: ', name, ' = ', clockface(time_diff))

    return time_diff

########################################################################################################################

