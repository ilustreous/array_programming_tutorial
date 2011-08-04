.. stdcal::

==================
Standard Deviation
==================




The answer is here::
 
 from stdcalc import *

Let's load up some data but import these first::

 import util

 import numpy as np

Now let's load it up ::

 sqltable = 'sp500_small' if util.is32bit() else 'sp500'
 
 query = 'select * from %(sqltable)s order by date desc' % vars()
 
 (symbols, prices) = util.gethistprices(query, numrows=1000, verbose=True)

Get the closing prices::

 ADJCLOSE = 6
 
 closeprices = prices[:, :, ADJCLOSE].transpose()

Do calculation the array programming style::

 std_1 = stdcalc1(closeprices)

Do the calculation the array programming style (one-liner)::

 std_2 = stdcalc2(closeprices)

Do the calculation using numpy's std funciton::

 std_np = stdcalcnp(closeprices)

Do the calculation the pythonic way::

 std_reg = stdcalcregall(symbols, closeprices)

Compare results std_1 vs std2, are they equal?::

 # is std_1 the same as std_2
 is_std1_2_same = np.allclose(std_1, std_2)

Compare results std_1 vs std_np, are they equal?::

 # is std_1 the same as std_np 
 is_std1_np_same = np.allclose(std_1, std_np)

Compare results std_reg vs std_np, are they equal?::

 # is std_reg the same as std_np
 is_stdreg_np_same = np.allclose(std_np, np.array(std_reg))
 

They are all equal in value, but probably not in speed.
Let's now profile/time it to see which is faster::

 import cProfile

Profiling the function "stdcalc1"::

 std_1_prof = cProfile.Profile()
 std_1_prof.runcall(stdcalc1, closeprices)
 std_1_prof.dump_stats('stdcalc1.stats')
 
Profiling the function "stdcalc2"::

 std_2_prof = cProfile.Profile()
 std_2_prof.runcall(stdcalc2, closeprices)
 std_2_prof.dump_stats('stdcalc2.stats')
 
Profiling the function "stdcalcnp"::

 std_np_prof = cProfile.Profile()
 std_np_prof.runcall(stdcalcnp, closeprices)
 std_np_prof.dump_stats('stdcalcnp.stats')

Profiling the function "stdcalcreg"::

 std_reg_prof = cProfile.Profile()
 std_reg_prof.runcall(stdcalcregall, symbols, closeprices)
 std_reg_prof.dump_stats('stdcalcreg.stats')
