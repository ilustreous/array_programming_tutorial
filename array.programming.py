# <demo> silent
import sys
import datetime
import time
import util



DATE = 0
OPEN = 1
HIGH = 2
LOW = 3
CLOSE = 4
VOLUME = 5
ADJCLOSE = 6

def reloadutil():
    import __builtin__ as b
    b.dreload(util)

def counter():
    x = [-1]
    def function(message=''):
        x[0] = x[0] + 1
        thecount = x[0]
        sep = "-" * max(9, len(message))
        if not message == '':
            sep += '\n'
        print >> sys.stdout, '\n\n%(sep)s%(message)s\nslide: %(thecount)d' % vars()
        
    return function

verbose = True

slidecounter = counter()

slidecounter('Initial Setup')
# <demo> stop

import numpy as np

sqltable = 'prices' if util.is32bit() else 'sp500'

query = 'select * from %(sqltable)s order by date desc' % vars()


################
slidecounter() #
################
# <demo> stop

(symbols, prices) = util.gethistprices(query, numrows=1000, verbose=verbose)


################
slidecounter() #
################
# <demo> stop

print >> sys.stdout, "Number of dimensions: %d" % prices.ndim

print >> sys.stdout, "Array dimensions: %s" % str(prices.shape)

print >> sys.stdout, "Total size in bytes: %d" % prices.nbytes

print >> sys.stdout, "Dtype: %s" % prices.dtype

print >> sys.stdout, "Element size in bytes: %d" % prices.itemsize

print >> sys.stdout, "Pointer to bytes in memory: %s" % str(prices.__array_interface__['data'])

print >> sys.stdout, "Flags: %s" % str(prices.flags)

print >> sys.stdout, "Stride: %s" % str(prices.strides)


################
slidecounter() #
################
# <demo> stop

# get closing prices per day
closeprices = prices[:, :, ADJCLOSE].transpose()

# get volume per day
volumes = prices[:, :, VOLUME].transpose()

# dates
dates = prices[:, :, DATE].transpose()



################
slidecounter() #
################
# <demo> stop

dates = dates[:,0]

minprice = closeprices.min()

minprices = closeprices.min(axis=0)

maxprice = closeprices.max()

maxprices = closeprices.max(axis=0)

maxprices2 = closeprices.max(axis=1)



################
slidecounter() #
################
# <demo> stop

# plot prices volumes by dates
import matplotlib.pyplot as plt
from datetime import datetime as dt



################
slidecounter() #
################
# <demo> stop

numdays = 30
fig = plt.figure()
ax1 = fig.add_subplot(111)
COL = np.nonzero(maxprices >= maxprice) 
dates_formatted = [dt.fromtimestamp(s) for s in dates]
ax1.plot(dates_formatted, closeprices[:,COL[0][0]], 'b-')
ax1.set_ylabel('price', color='b')
for tl in ax1.get_yticklabels():
    tl.set_color('b')

ax1.set_xlabel('Date')

ax2 = ax1.twinx()
ax2.plot(dates_formatted, volumes[:,COL[0][0]], 'r')
ax2.set_ylabel('volume', color='r')
for tl in ax2.get_yticklabels():
    tl.set_color('r')



################
slidecounter() #
################
# <demo> stop



print 'The winner is %s' % symbols[maxprices >= maxprice][0]

################
slidecounter() #
################
# <demo> stop

# some other way to create arrays
arr_vals = np.zeros((4,3))
arr_vals = np.ones((4,3))
arr_vals = np.empty((4,3))
arr_vals = np.arange(12).reshape(4,3)
arr_vals = np.random.rand(4,3)



################
slidecounter() #
################
# <demo> stop

# arithmetic operations are computed elementwise

# compute the volatility of aapl, goog, nflx
price_relatives = closeprices[1:numdays] / closeprices[0:numdays-1, :]


################
slidecounter() #
################
# <demo> stop

returns = np.log(price_relatives)


################
slidecounter() #
################
# <demo> stop

avg_returns = np.sum(returns, axis=0) / len(price_relatives)


################
slidecounter() #
################
# <demo> stop

devs = returns - avg_returns


################
slidecounter() #
################
# <demo> stop

devs_sqr= devs ** 2


################
slidecounter() #
################
# <demo> stop

sum_devs_sqr = np.sum(devs_sqr, axis=0)


################
slidecounter() #
################
# <demo> stop

variances = sum_devs_sqr / len(price_relatives)


################
slidecounter() #
################
# <demo> stop

stdevs = variances ** .5


################
slidecounter() #
################
# <demo> stop

ann_devs = stdevs * (252 ** .5)


################
slidecounter() #
################
# <demo> stop

# vol for symbol
someindex = (symbols=='aapl').nonzero()

ann_devs[(symbols=='aapl').nonzero()][0]

ann_devs[(symbols=='goog').nonzero()][0]

ann_devs[(symbols=='nflx').nonzero()][0]

################
slidecounter() #
################
# <demo> stop

# symbols greater than 50 vol
symbols[np.nonzero(ann_devs > .5),:]

# symbols less than .25 vol
symbols[np.nonzero(ann_devs < .25),:]


################
slidecounter() #
################
# <demo> stop



# Compare imperative programming with array programming
import nikkei
percent_change = lambda data: np.diff(data, axis=0) / data[0:-1]

print """

nikkei.percent_change??

"""

################
slidecounter() #
################
# <demo> stop

def seriesplot(data):
    fig = plt.figure()
    ax4 = fig.add_subplot(111)
    ax4.plot(data)

print """

nikkei.seriesplot??

"""


################
slidecounter() #
################
# <demo> stop

def yyyymmdd2epochsec(yyyymmdd):

    return time.mktime(datetime.datetime.strptime(str(yyyymmdd) ,'%Y%m%d').timetuple())


qd2epoch = yyyymmdd2epochsec


epoch2dt = util.epoch2datetime



################
slidecounter() #
################
# <demo> stop

def returnsplot(d1, d2, data, dates):
    #dates in yyyymmdd format
    plotvals = data[np.logical_and(dates > qd2epoch(d1), dates < qd2epoch(d2))]
    seriesplot(percent_change(plotvals))

print """

nikkei.returnsplot??

"""


################
slidecounter() #
################
# <demo> stop

def densityplot(data):
    import pylab
    dailyreturns = percent_change(data)
    fig = plt.figure()
    ax5 = fig.add_subplot(111)
    ax5.hist(dailyreturns, bins=200, normed=True)
    m, M = np.min(dailyreturns), np.max(dailyreturns)
    mu = np.mean(dailyreturns)
    sigma = np.std(dailyreturns)
    grid = np.linspace(m, M, 100)
    densityvalues = pylab.normpdf(grid, mu, sigma)
    ax5.plot(grid, densityvalues, 'r-')
    ax5.show()

print """

nikkei.densityplot??

"""

################
slidecounter() #
################
# <demo> stop

def monthly_returns(data, dates):
    e2d = np.vectorize(epoch2dt)
    d2m = np.vectorize(lambda x: x.month)
    ms = d2m(e2d(dates))
    (uniqvals, posfirstuniq, index) = np.unique(ms, True, True)
    seriesplot(data[posfirstuniq])

print """

nikkei.monthly_returns??

"""

################
slidecounter() #
################
# <demo> stop


# <demo> silent

stop_here_for_problem = """Compute the standard deviation by symbol.

1) Imperative Programming style
2) Array Programming style

Bonus:
    1) Compute the standard deviation in the array 
       programming style in 1 line.
    2) Create a box-and-wisker plot for GOOG

Take 15-20 min to work it out. 

Work with neighbors, use the internet.

BUT don't use np.stdev use it to check your answer!!!

"""

print stop_here_for_problem

################
slidecounter() #
################
# <demo> stop

price_from_mean = closeprices - closeprices.mean(axis=0)



################
slidecounter() #
################
# <demo> stop

abs_price_from_mean = np.abs(price_from_mean)



################
slidecounter() #
################
# <demo> stop

abs_price_squared = abs_price_from_mean ** 2



################
slidecounter() #
################
# <demo> stop

mean_price_squred = np.mean( abs_price_squared, axis=0 )



################
slidecounter() #
################
# <demo> stop

std_prices = np.sqrt( mean_price_squred)



################
slidecounter() #
################
# <demo> stop

# oneliner to get std of prices
std_prices2 = np.sqrt( np.mean( np.abs(closeprices - closeprices.mean(axis=0)) ** 2 , axis=0 ))



################
slidecounter() #
################
# <demo> stop

# lets boxplot to visualize the stdev
fig  = plt.figure()
ax3 = fig.add_subplot(111)
ax3.boxplot(closeprices[:, ann_devs.argsort()[-1]], notch=0, sym='+', vert=1, whis=1.5, positions=None
        , widths=None, patch_artist=False)

ax3.set_title(symbols[ann_devs.argsort()][-1])


################
slidecounter() #
################
# <demo> stop

# <demo> silent
memory_copy = """
When working with large datasets it's a must
to know how how arry copies work, when it happens,
why it happens..



You're only one operation from doubling your memory
and then you'll be sad.
"""
print memory_copy



################
slidecounter() #
################
# <demo> stop


capacity = 1e3 if util.is32bit() else 1e8

arr1 = np.ones(capacity)

# -1 means 'numpy please figure out the correct dimension'
arr1.shape = (-1, 50)



################
slidecounter() #
################
# <demo> stop


# Assignments do not create copy of arrays
arr2 = arr1

arr1 is arr2



################
slidecounter() #
################
# <demo> stop


# Function calls do not copy arrays, mutable objects are passed by reference
def myid(some_array):
    return id(some_array)

x = id(arr1)
y = myid(arr2)

x == y



################
slidecounter() #
################
# <demo> stop


# views on arrays
# new view on the same data
arr1_view = arr1.view()



################
slidecounter() #
################
# <demo> stop

# not the same
arr1_view is arr1

# the same
arr1_view.base is arr1



################
slidecounter() #
################
# <demo> stop

# doesn't own the data
arr1_view.flags.owndata



################
slidecounter() #
################
# <demo> stop

# changes shape
arr1_view.shape = (-1, 2)

# base is stil the same
arr1_view.base is arr1



################
slidecounter() #
################
# <demo> stop

# change data in view
arr1_view[0,0] = 50

# change data in both
arr1_view[0,0] == arr1[0,0]



################
slidecounter() #
################
# <demo> stop


# simple slicing creates a view of the array
arr2_view = arr1[1:10, 50:60]

# same base
arr2_view.base is arr1



################
slidecounter() #
################
# <demo> stop

arr2_reversed = arr2_view[::-1]



################
slidecounter() #
################
# <demo> stop

# named record
adtype = np.dtype([('a',int), ('b', int), ('c', int), ('d', int)])
arr_named = np.array([(3,3,4,5),(3,34,34,5)], dtype=adtype)



################
slidecounter() #
################
# <demo> stop

# creates a view
arr_named1 = arr_named['a']



################
slidecounter() #
################

# <demo> stop
 
# copy data
arr1_copy = arr1.copy()



################
slidecounter() #
################
# <demo> stop

# owns the data
arr1_copy.flags.owndata



################
slidecounter() #
################
# <demo> stop

# not equal
arr1_copy is arr1

# not equal
arr1_copy.base is arr1



################
slidecounter() #
################
# <demo> stop

# change value
arr1_copy[0,0] = 30

# does not change value of arr1
arr1_copy[0,0] == arr1[0,0]



################
slidecounter() #
################
# <demo> stop

# advanced slicing is slicing using boolean array or integer array
b = np.arange(10)

b.shape = (5, 2)

# not advanced
# selects the 3rd row x 2nd col
b[2,1]



################
slidecounter() #
################
# <demo> stop

# advanced
# selects 3rd column and 2nd col
b[(2, 1),]



################
slidecounter() #
################
# <demo> stop

# select 3rd and 5th row and 
# from the sub 2-dim array
# select the 0th column and 1st col
# from the second row
b[[2,4],[0,1]]



################
slidecounter() #
################
# <demo> stop

# assign to advanced selections
b[[2,4], [0,1]] = 400



################
slidecounter() #
################
# <demo> stop

# boolean indexing
b > 399



################
slidecounter() #
################
# <demo> stop

y = b[b > 399]



################
slidecounter() #
################
# <demo> stop

y.flags



################
slidecounter() #
################
# <demo> stop

e = b.T
b.strides
e.strides


################
slidecounter() #
################
# <demo> stop


# <demo> silent
recarry_sql = """
Recarray/Sql Comparison
------------------------

numpy has views that can be built on top of the ndarray - just 
a different view on it (some_array.view()). 

Elements do NOT need to be homogeneous single types. They can
be made up of heterogeneous types they just need to be of 
the same size.

Recarrys are analogous to columns in a spreadsheet. 

The recarray gives us the ability to access data via attributes

some_rec_array.date

rather than a dictionary lookup

some_rec_array['date']

"""



################
slidecounter() #
################
# <demo> stop


rec_arr = util.sqlite2rec(query='select * from %(sqltable)s' % vars(), verbose=verbose)



################
slidecounter() #
################
# <demo> stop

import struct
struct.unpack('<d4s4did', rec_arr.data[0:56])



################
slidecounter() #
################
# <demo> stop

import matplotlib.mlab as mlab

# groupby
recnumrecs = mlab.rec_groupby(rec_arr, ('sym',), (('sym', len, 'symcount'), ))
sqlnumrecs = util.sqlquery('select sym, count(1) from %(sqltable)s group by sym' % vars())



################
slidecounter() #
################
# <demo> stop

sqlavgs = util.sqlquery('select sym, avg(open), avg(high), avg(low), avg(close),\
                        avg(volume), avg(adjclose) from %(sqltable)s group by sym' % vars())
recavgs = mlab.rec_groupby(rec_arr, ('sym', ), (('open', np.average, 'avgopen')
                                                    ,('high', np.average, 'avghigh')
                                                    ,('low', np.average, 'avglow')
                                                    ,('close', np.average, 'avgclose')
                                                    ,('volume', np.average, 'avgvolume')
                                                    ,('adjclose', np.average, 'avgadjclose')))



################
slidecounter() #
################
# <demo> stop

# sort
sqlsort = util.sqlquery('select * from %(sqltable)s order by sym, volume, close' % vars())
sortidx = np.lexsort([rec_arr.close, rec_arr.volume, rec_arr.sym])
sorted_rec_arr = rec_arr[sortidx]



################
slidecounter() #
################
# <demo> stop

# filtering
sqlfilter1 = util.sqlquery('select * from %(sqltable)s where close > 250 and close < 375' % vars())
recfilter1 = rec_arr[(rec_arr.close > 250) & (rec_arr.close < 375)]



################
slidecounter() #
################
# <demo> stop

#joins
simplejoin = """
select * 
  from
(select * 
   from  %(sqltable)s
  where sym = 'aapl') a
,(select * 
    from %(sqltable)s
   where sym = 'goog')  b
where a.date = b.date
""" % vars()
sqljoin = util.sqlquery(simplejoin)

aapl = rec_arr[rec_arr.sym=='aapl']
goog = rec_arr[rec_arr.sym=='goog']
recjoin = mlab.rec_join(['date'], aapl, goog, jointype='inner')



################
slidecounter() #
################
# <demo> stop

# union (rec_append_fields)
simpleunion = """
select * 
  from %(sqltable)s
 where sym = 'aapl'
union
select * 
  from %(sqltable)s 
 where sym = 'goog'
order by sym, date desc
""" % vars()
sqlunion = util.sqlquery(simpleunion)



################
slidecounter() #
################
# <demo> stop

from numpy.lib import recfunctions as recfunc
recunion = recfunc.stack_arrays((aapl, goog)
                                ,usemask=False
                                ,asrecarray=True
                                ,autoconvert=True)



################
slidecounter() #
################
# <demo> stop

# sub selection
simpleselection = "select close, volume from  %(sqltable)s where sym = 'aapl'"
selected = util.sqlquery(simpleselection)
recselect = rec_arr[['close', 'volume']]



################
slidecounter() #
################
# <demo> stop

