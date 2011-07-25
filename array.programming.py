import sys
import datetime
import time

DATE = 0
OPEN = 1
HIGH = 2
LOW = 3
CLOSE = 4
VOLUME = 5
ADJCLOSE = 6
SUSQPROXY = {'http': 'http://http-proxy.susq.com:80'}

def epochsec2datetime(epochsec):
    return datetime.datetime.fromtimestamp(epochsec)

def testprices():
    x = np.array([ 35.438,35.75 ,35.875 ,36.938 ,39.313 
                  ,39.125 ,42.5 ,42.313 ,45.5 ,46.688 ,46.125 
                  ,43.75 ,45.375 ,46.594 ,46.938 ,46.188 
                  ,44.5 ,45.875 ,45.75 ,44.625 
                  ,45 ,45.5 ,48.375 ,51 ,47.75])
    y =           np.vstack([x,x])
    prices = y.transpose()
    return prices

def gethistdataforsymbols(syms, lookback=60):

    histdatas = []
    for sym in syms:
        print >> sys.stdout, 'Getting hist data from yahoo: %s' % sym
        histdatas.append(gethistdatafromyahoo(sym)[0:lookback])
    return histdatas

def gethistdatafromyahoo(sym, proxydict=None):
    #header: Date,Open,High,Low,Close,Volume,Adj Close

    import urllib

    url = "http://ichart.finance.yahoo.com/table.csv?s=%s&d\
            =6&e=19&f=2011&g=d&a=8&b=7&c=1984&ignore=.csv" % sym
    proxies = proxydict
    fh = urllib.urlopen(url, proxies=proxies)
    try:
        rows = []
        fh.readline()
        for row in fh.readlines():
            row = row.strip().split(",")
            
            row[0] = time.mktime(datetime.datetime.strptime(row[0],
                '%Y-%m-%d').timetuple())
            rows.append(row)
        return rows
    finally:
        fh.close()

def readfile(file_):
    #header: Date,Open,High,Low,Close,Volume,Adj Close
    import csv
    import datetime
    rows = []
    with open (file_, 'r') as fh:
        reader = csv.reader(fh)
        reader.next()
        for row in reader:
            if len(row) <= 0:
                continue
            row[0] = time.mktime(datetime.datetime.strptime(row[0],
                '%Y-%m-%d').timetuple())
            rows.append(row)
    return rows[0:60]

def readfiles(globpattern):
    import glob
    csvfiles = glob.glob(globpattern)
    files = []
    for csvfile in csvfiles:
        file_ = readfile(csvfile) 
        files.append(file_)
    
    return files


import numpy as np

isyahoo = False

symbols = np.array(['AAPL', 'GOOG', 'NFLX'], dtype=str)
if isyahoo:
    # read in all files (aapl, goog, nflx)
    histdata = gethistdataforsymbols(symbols)
else:
    histdata = readfiles('*.csv')

# create an ndarray from the allfiles sequence
arr_files = np.array(histdata, dtype = float)

print >> sys.stdout, "Number of dimensions: %d" % arr_files.ndim

print >> sys.stdout, "Array dimensions: %s" % str(arr_files.shape)

print >> sys.stdout, "Total size in bytes: %d" % arr_files.nbytes

print >> sys.stdout, "Dtype: %s" % arr_files.dtype

print >> sys.stdout, "Element size in bytes: %d" % arr_files.itemsize

print >> sys.stdout, "Stride: %s" % str(arr_files.strides)

# get closing prices per day
prices = arr_files[:, :, CLOSE].transpose()

# get volume per day
volumes = arr_files[:, :, VOLUME].transpose()

# dates
dates = arr_files[:, :, DATE].transpose()
dates = dates[:,0]

minprice = prices.min()

minprices = prices.min(axis=0)

maxprice = prices.max()

maxprices = prices.max(axis=0)

#doesn't mean much but
mps = prices.max(axis=1)

# plot prices volumes by dates
import matplotlib.pyplot as plt
from datetime import datetime as dt

fig = plt.figure()
ax1 = fig.add_subplot(111)
AAPL_COL = 1
dates_formatted = [dt.fromtimestamp(s) for s in dates]
ax1.plot(dates_formatted, prices[:,AAPL_COL], 'b-')
ax1.set_ylabel('price', color='b')
for tl in ax1.get_yticklabels():
    tl.set_color('b')

ax1.set_xlabel('Date')

ax2 = ax1.twinx()
ax2.plot(dates_formatted, volumes[:,AAPL_COL], 'r')
ax2.set_ylabel('volume', color='r')
for tl in ax2.get_yticklabels():
    tl.set_color('r')

# some other way to create arrays
arr_vals = np.zeros((4,3))
arr_vals = np.ones((4,3))
arr_vals = np.empty((4,3))
arr_vals = np.random.rand(4,3)
arr_vals = np.arange(12).reshape(4,3)

# arithmetic operations are computed elementwise

# compute the volatility of aapl, goog, nflx
price_relatives = prices[1:] / prices[0:-1, :]

returns = np.log(price_relatives)

avg_returns = np.sum(returns, axis=0) / len(price_relatives)

devs = returns - avg_returns

devs_sqr= devs ** 2

sum_devs_sqr = np.sum(devs_sqr, axis=0)

variances = sum_devs_sqr / len(price_relatives)

stdevs = variances ** .5

ann_devs = stdevs * (252 ** .5)

# vol for symbol
someindex = (symbols=='AAPL').nonzero()

ann_devs[(symbols=='AAPL').nonzero()][0]

ann_devs[(symbols=='GOOG').nonzero()][0]

ann_devs[(symbols=='NFLX').nonzero()][0]

# symbols greater than 50 vol
symbols[np.nonzero(ann_devs > .5),:]

# symbols less than .25 vol
symbols[np.nonzero(ann_devs < .25),:]

# do a box plot here

#show them all the pieces with a set of dummy data
# then have them do the stdev
# computes the standard devations of prices
# maybe have the class do this one?
price_from_mean = prices - prices.mean(axis=0)

abs_price_from_mean = np.abs(price_from_mean)

abs_price_squared = abs_price_from_mean ** 2

mean_price_squred = np.mean( abs_price_squared, axis=0 )

std_prices = np.sqrt( mean_price_squred)

# oneliner to get std of prices
std_prices2 = np.sqrt( np.mean( 
    np.abs(prices - prices.mean(axis=0)) ** 2 , axis=0 ))


# lets boxplot to visualize the stdev
fig  = plt.figure()
ax3 = fig.add_subplot(111)
ax3.boxplot(prices, notch=0, sym='+', vert=1, whis=1.5, positions=None
        , widths=None, patch_artist=False)

# compare existing code to numpy version of it
# --------------------------------------------
# what's the take away?
# wanted to show how imperative programming compares to array programming
# denser code and conveys the meaning quite literally
# works on columns of data not just one one sequence, so it scales well
# much more efficient b/c all the hard things are taken care of in
# very robust/tested c code

percent_change = lambda data: np.diff(data, axis=0)/data[0:-1]

def seriesplot(data):
    fig = plt.figure()
    ax4 = fig.add_subplot(111)
    ax4.plot(data)

def yyyymmdd2epochsec(yyyymmdd):
    return time.mktime(datetime.datetime.strptime(str(yyyymmdd)
                                                  ,'%Y%m%d').timetuple())

qd2epoch = yyyymmdd2epochsec
epoch2dt = epochsec2datetime

def returnsplot(d1, d2, data, dates):
    #dates in yyyymmdd format
    plotvals = data[np.logical_and(dates > qd2epoch(d1), dates < qd2epoch(d2))]
    seriesplot(percent_change(plotvals))

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

def monthly_returns(data, dates):
    e2d = np.vectorize(epoch2dt)
    d2m = np.vectorize(lambda x: x.month)
    ms = d2m(e2d(dates))
    (uniqvals, posfirstuniq, index) = np.unique(ms, True, True)
    seriesplot(data[posfirstuniq])

# when working with big data it's good
# to understand at least conceptually
# memory management.
# - when arrays are copied
# - when arrays are referenced
# - when arrays are destroyed
# operations
#   - slicing
#   - passing an array to a function (altering a value/not altering a value)
#   - assigning array to another variable and changing a value

arr1 = np.ones(1e8)
arr1.shape = (-1, 50)

# Assignments do not create copy of arrays
arr2 = arr1

arr1 is arr2

# Function calls do not copy arrays, mutable objects are passed by reference
def myid(some_array):
    return id(some_array)

x = id(arr1)
y = myid(arr2)

x == y

# views on arrays
# new view on the same data
arr1_view = arr1.view()

# not the same
arr1_view is arr1

# the same
arr1_view.base is arr1

# doesn't own the data
arr1_view.flags.owndata

# changes shape
arr1_view.shape = (-1, 2)

# base is stil the same
arr1_view.base is arr1

# change data in view
arr1_view[0,0] = 50

# change data in both
arr1_view[0,0] == arr1[0,0]

# simple slicing creates a view 
# of the array
arr2_view = arr1[1:10, 50:60]

# same base
arr2_view.base is arr1

arr2_reversed = arr2_view[::-1]

# named record
adtype = np.dtype([('a',int), ('b', int), ('c', int), ('d', int)])
arr_named = np.array([(3,3,4,5),(3,34,34,5)], dtype=adtype)

# creates a view
arr_named1 = arr_named['a']

# copy data
arr1_copy = arr1.copy()

# owns the data
arr1_copy.flags.owndata

# not equal
arr1_copy is arr1

# not equal
arr1_copy.base is arr1

# change value
arr1_copy[0,0] = 30

# does not change value of arr1
arr1_copy[0,0] == arr1[0,0]

# advanced slicing is slicing using boolean array or integer array
# instead of using a slice
# "advanced slicing" using ndarrays creates a copy of the data
b = np.arange(10)
b.shape = (5, 2)

# not advanced
# selects the 3rd row x 2nd col
b[2,1]

# advanced
# selects 3rd column and 2nd col
b[(2, 1),]

# select 3rd and 5th row and 
# from the sub 2-dim array
# select the 0th column and 1st col
# from the second row
b[[2,4],[0,1]]

# assign to advanced selections
b[[2,4], [0,1]] = 400

# boolean indexing
b > 399

y = b[b > 399]

y.flags


# broadcasting rules
#    [0 1 2 3] 
#  + [3]
# 
# ==
# 
#   [0,1,2,3]
#   [3,3,3,3]
# = [3,4,5,6]

#[1,1,1,1]
#[1,1,1,1] + [1,2,3]
#[1,1,1,1]
#
#[1,1,1,1]   [1
#[1,1,1,1] +  2
#[1,1,1,1]    3]
#
#
#[1,1,1,1] + [1,1,1,1]
#[1,1,1,1] + [2,2,2,2]
#[1,1,1,1] + [3,3,3,3]
# = 
#[2,2,2,2]
#[3,3,3,3]
#[4,4,4,4]

# Compare dims starting from the last
# Match when either dimension is 
# one or None or if dimensions are equal

# Scalar
# ( ,)
# (3,)
# ----
# (3,1)

#2d
# (3, 4)
# (3, 1)
# -----
# (3, 4)

#3d
# (3, 5, 2)
# (      8)
# ---------
#  xxx

