import sys

DATE = 0
OPEN = 1
HIGH = 2
LOW = 3
CLOSE = 4
VOLUME = 5
ADJCLOSE = 6

def testprices():
    x = np.array([ 35.438 ,35.75 ,35.875 ,36.938 ,39.313 ,39.125 ,42.5 ,42.313 ,45.5 ,46.688 ,46.125 ,43.75 ,45.375 ,46.594 ,46.938 ,46.188 ,44.5 ,45.875 ,45.75 ,44.625 ,45 ,45.5 ,48.375 ,51 ,47.75])
    y = np.vstack([x,x])
    prices = y.transpose()
    return prices

def gethistdataforsymbols(syms, lookback=60):

    histdatas = []
    for sym in syms:
        print >> sys.stdout, 'Getting hist data from yahoo: %s' % sym
        histdatas.append(gethistdatafromyahoo(sym)[0:lookback])
    return histdatas

def gethistdatafromyahoo(sym):
    #header: Date,Open,High,Low,Close,Volume,Adj Close

    import urllib
    import datetime
    import time

    url = "http://ichart.finance.yahoo.com/table.csv?s=%s&d=6&e=19&f=2011&g=d&a=8&b=7&c=1984&ignore=.csv" % sym
    proxies = None #{'http': 'http://http-proxy.susq.com:80'}
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
    import time
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

# read in all files (aapl, goog, nflx)
#histdata = readfiles('*.csv')
symbols = np.array(['AAPL', 'GOOG', 'NFLX'], dtype=str)
histdata = gethistdataforsymbols(symbols)

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
dates_formatted = [dt.fromtimestamp(s) for s in dates[:, AAPL_COL]]
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
std_prices2 = np.sqrt( np.mean( np.abs(prices - prices.mean(axis=0))**2 , axis=0 ))


# lets boxplot to visualize the stdev
fig  = plt.figure()
ax3 = fig.add_subplot(111)
ax3.boxplot(prices, notch=0, sym='+', vert=1, whis=1.5, positions=None
        , widths=None, patch_artist=False)

#----------------------------------------------------
#outline = """
#Topics
#------
#  - Numpy
#  - Matplotlib
#  - Recarray
#"""
#print >> sys.stdout, outline
## <demo> stop
#
## <demo> stop
#import numpy as np
## <demo> stop
#
## <demo> stop
## create a list sequence in python
#vals = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
#
## construct an ndarray from the list
#arr_vals = np.array(vals)
## <demo> stop
#
#
## <demo> stop
## sequence of sequences
#vals = [ [ 1,  2,  3]
#        ,[ 4,  5,  6]
#        ,[ 7,  8,  9]
#        ,[10, 11, 12]]
#
## Creates a 2-dimensional matrix
#arr_vals = np.array(vals)
## <demo> stop
#
## <demo> stop
## can inspect lots of metadata from it's attributes
#print >> sys.stdout, str(arr_vals)
#print >> sys.stdout, "\n\nElement size in bytes: %d\n\n" % arr_vals.itemsize
## <demo> stop
#
## <demo> stop
## can inspect lots of metadata from it's attributes
#print >> sys.stdout, str(arr_vals)
#print >> sys.stdout, "\n\nTotal size in bytes: %d\n\n" % arr_vals.nbytes
## <demo> stop
#
## <demo> stop
## can inspect lots of metadata from it's attributes
#print >> sys.stdout, str(arr_vals)
#print >> sys.stdout, "\n\nNumber of dimensions: %d\n\n" % arr_vals.ndim
## <demo> stop
#
## <demo> stop
## can inspect lots of metadata from it's attributes
#print >> sys.stdout, str(arr_vals)
#print >> sys.stdout, "\n\nArray dimensions: %s\n\n" % str(arr_vals.shape)
## <demo> stop
#
## <demo> stop
## can inspect lots of metadata from it's attributes
#print >> sys.stdout, str(arr_vals)
#print >> sys.stdout, "\n\nDtype: %s\n\n" % arr_vals.dtype
## <demo> stop
#
## <demo> stop
## can inspect lots of metadata from it's attributes
#print >> sys.stdout, str(arr_vals)
#print >> sys.stdout, "\n\nStride: %s\n\n" % str(arr_vals.strides)
## <demo> stop
#
## <demo> stop
## <demo> stop
#
## <demo> silent
#print >> sys.stdout, """
#
#Other useful ways to create arrays
#----------------------------------
# - zeros
# - ones
# - empty
# - rand
# - arange
#
#"""
## <demo> stop
#
## <demo> stop
#arr_val = np.zeros((4,3))
#print >> sys.stdout, arr_val
## <demo> stop
#
## <demo> stop
#arr_val = np.ones((4,3))
#print >> sys.stdout, arr_val
## <demo> stop
#
## <demo> stop
#arr_val = np.empty((4,3))
#print >> sys.stdout, arr_val
## <demo> stop
#
## <demo> stop
#arr_val = np.random.rand(4,3)
#print >> sys.stdout, arr_val
## <demo> stop
#
## <demo> stop
#arr_val = np.arange(12).reshape(4,3)
#print >> sys.stdout, arr_val
## <demo> stop
#
#
## <demo> silent
#print >> sys.stdout, """
#
#Basic Operations
#----------------
#
#"""
## <demo> stop
#
## <demo> silent 
#
#print >> sys.stdout, """
#Arithmetic operators on arrays apply elementwise.
#A new array is created and filled with the result
#
#
#arr_val ^ 2
#
#"""
#print >> sys.stdout, "%s \n\n^\n\n %s\n\n=\n\n" % (arr_val, arr_val)
#print >> sys.stdout, "%s\n\n" % arr_val ** 2
## <demo> stop
#
## <demo> silent 
#print >> sys.stdout, "\n\narr_val + arr_val\n\n"
#print >> sys.stdout, "%s \n\n+\n\n %s\n\n=\n\n" % (arr_val, arr_val)
#print >> sys.stdout, "%s\n\n" % (arr_val + arr_val)
## <demo> stop
#
## <demo> silent
#print >> sys.stdout, "\n\narr_val * arr_val\n\n"
#print >> sys.stdout, "%s \n\n*\n\n %s\n\n=\n\n" % (arr_val, arr_val)
#print >> sys.stdout, "%s\n\n" % (arr_val * arr_val)
#print >> sys.stdout, """
#
#Unlike in many matrix languages, the product operator "*" operates
#elementwise. Matrix product is performed using the dot function
#or creating matrix objects.
#
#"""
## <demo> stop
#
#
## <demo> silent 
#print >> sys.stdout, """
#It is possible to perform some operations inplace so that new arrays
#are not created.
#"""
## <demo> stop
#
## <demo> stop
#cpy_arr_val = arr_val.copy()
#cpy_arr_val *= 2
#print >> sys.stdout, "\n\n%s\n\n" % cpy_arr_val
## <demo> stop
#
## <demo> stop
#print >> sys.stdout, """
#When operating on arrays of different types,
#the type of the resulting array corresponds to
#the more percise one - Upcasting
#"""
## <demo> stop
#
## <demo> stop
#ns = np.ones((4,3), dtype=np.int32)
#ds = np.zeros((4,3), dtype=np.float64)
#ws = ns + ds
#print >> sys.stdout, "ns\n\n=%s\n\nds=\n\n%s\n\nws=\n\n%s\n\n" % (ns, ds, ws)
#print >> sys.stdout, "\n\ndtype\nns = %s\nds = %s\nws = %s\n\n" %  (ns.dtype, ds.dtype,
#                                                       ws.dtype)
#
## <demo> stop
#
## <demo> stop
#print >> sys.stdout, """unary operations like sum, max, min are methods on the
#ndarray"""
#print >> sys.stdout, "max = %d" % arr_val.max()
#print >> sys.stdout, "min = %d" % arr_val.min()
#print >> sys.stdout, "sum = %d" % arr_val.sum()
## <demo> stop
#
## <demo> stop
#print >> sys.stdout, """unary operations like sum, max, min are methods on the
#ndarray"""
#print >> sys.stdout, "max = %s" % arr_val.max(axis=1)
#print >> sys.stdout, "max = %s" % arr_val.max(axis=0)
#print >> sys.stdout, "min = %s" % arr_val.min(axis=1)
#print >> sys.stdout, "min = %s" % arr_val.min(axis=0)
#print >> sys.stdout, "sum = %s" % arr_val.sum(axis=1)
#print >> sys.stdout, "sum = %s" % arr_val.sum(axis=0)
## <demo> stop
#
## <demo> stop
#print >> sys.stdout, """
#Universal functions
#NumPy provides familiar mathematical functions
#, sin, cos, exp, etc. But in NumPy these functinions are called 
#"universal functions"(ufunc). The reason for having such a name, 
#within NumPy these functions operated on an array object elementwise, 
#producing array as an output
#
#they also have functions on them - reduce, etc...
#"""
#
#print >> sys.stdout, "%s\n\n" % np.sin(arr_val)
#print >> sys.stdout, "%s\n\n" % np.sqrt(arr_val)
#print >> sys.stdout, "%s\n\n" % np.average(arr_val)
#print >> sys.stdout, "%s\n\n" % np.exp(arr_val)
# <demo> stop

#----------------------------------------------------------------------

## <demo> silent
#memoryblock = """
#
#ndarray object
#--------------
# 1) Metadata
# 2) Data Buffer
#
#Metadata: - element's size in bytes
#          - total size in bytes
#          - the number of dimensions and size of dimensions
#          - dtype: the interpretation of the basic data elements
#          - array order (C or Fortan)
#          - the stride between elements
#          
#Data Buffer: A contiguous (and fixed) block of memory 
#             containing fixed sized data items.
#             Typically what people think of as the 
#             actual arrays of data in C or Fortran.
#"""
#print >> sys.stdout, memoryblock
## <demo> stop
## give shape to the array (4 rows x 3 columns)
#arr_vals.shape = (4,3)
#
## set second row to 15s
#arr_vals[1] = np.random.randn()
## <demo> stop
#
## <demo> auto
#arr_vals
## <demo> stop
#
## <demo> silent
#print >> sys.stdout, """
#Data Buffer Object
#------------------
#
#ndarray''s buffer object attribute
#
#buffer object points to the start of the array''s data
#
#i.e. arr_vals.data
#
#"""
## <demo> stop
#
#
##next show arr_vals.data and how stride works with the 
##underlying binary data 
#
##show how data is referenced around when you slice or assign to another
##variable but the metadata can change - effectively creates another view
##on top of the underlying data buffer
#
#b = arr_vals[0]
#b[:] = 8
#
##show how the metadata has changed between arr_vals and b
