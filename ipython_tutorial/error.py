#!/usr/bin/env python
"""
File with deliberate errors to demonstrate IPython debugging.
"""

import time
import sys

# In addition to using %debug, one can also insert calls to a tracer to
# activate the interactive debugger at any given location in a code.
from IPython.Debugger import Tracer; debug_here = Tracer()

from numpy import *

def Ramp(result, size, start, end):    
    step = (end-start)/(size-1)
    for i in xrange(size):
        result[i] = start + step*i

def mul(x,y):
    return x*y

def RampNum(result, size, start, end):
    #debug_here()  # use this to force a debugger to start here

    bug = zeros(size+1)
    step = (end-start)/(size-1-bug)
    #step = (end-start)/(size-1)
    result[:] = mul(arange(size),step) + start

def main():
    # Test parameters
    size = 100000
    reps = 10
    print 'size:',size
    print 'reps:',reps

    # Pure Python code
    t0=time.clock()
    array_num = zeros(size,'d')
    for i in xrange(reps):
        RampNum(array_num, size, 0.0, 1.0)
    RNtime = time.clock()-t0
    print 'RampNum time:', RNtime

    # Numpy version
    array_normal = [0]*size
    t0=time.clock()
    for i in xrange(reps):
        Ramp(array_normal, size, 0.0, 1.0)
    Rtime = time.clock()-t0
    print 'Ramp time:', Rtime

    # Summary
    try:
        speedup = Rtime/RNtime
    except ZeroDivisionError:
        speedup = 'inf'
    print 'speedup:',speedup

if __name__ == '__main__':
    main()
