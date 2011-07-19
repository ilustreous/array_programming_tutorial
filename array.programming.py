# <demo> silent
import sys
import os
from sys import getrefcount

outline = """
Topics
------
  - Numpy
  - Matplotlib
  - Recarray
"""
print >> sys.stdout, outline
# <demo> stop

# <demo> stop
import numpy as np
# <demo> stop

# <demo> stop
# create a list sequence in python
vals = np.array([1,2,3,4,5,6,7,8,9,10,11,12])

# construct an ndarray from the list
arr_vals = np.array(vals)
# <demo> stop


# <demo> stop
# sequence of sequences
vals = [ [ 1,  2,  3]
        ,[ 4,  5,  6]
        ,[ 7,  8,  9]
        ,[10, 11, 12]]

# Creates a 2-dimensional matrix
arr_vals = np.array(vals)
# <demo> stop

# <demo> stop
# can inspect lots of metadata from it's attributes
print >> sys.stdout, str(arr_vals)
print >> sys.stdout, "\n\nElement size in bytes: %d\n\n" % arr_vals.itemsize
# <demo> stop

# <demo> stop
# can inspect lots of metadata from it's attributes
print >> sys.stdout, str(arr_vals)
print >> sys.stdout, "\n\nTotal size in bytes: %d\n\n" % arr_vals.nbytes
# <demo> stop

# <demo> stop
# can inspect lots of metadata from it's attributes
print >> sys.stdout, str(arr_vals)
print >> sys.stdout, "\n\nNumber of dimensions: %d\n\n" % arr_vals.ndim
# <demo> stop

# <demo> stop
# can inspect lots of metadata from it's attributes
print >> sys.stdout, str(arr_vals)
print >> sys.stdout, "\n\nArray dimensions: %s\n\n" % str(arr_vals.shape)
# <demo> stop

# <demo> stop
# can inspect lots of metadata from it's attributes
print >> sys.stdout, str(arr_vals)
print >> sys.stdout, "\n\nDtype: %s\n\n" % arr_vals.dtype
# <demo> stop

# <demo> stop
# can inspect lots of metadata from it's attributes
print >> sys.stdout, str(arr_vals)
print >> sys.stdout, "\n\nStride: %s\n\n" % str(arr_vals.strides)
# <demo> stop

# <demo> stop
# <demo> stop

# <demo> silent
print >> sys.stdout, """

Other useful ways to create arrays
----------------------------------
 - zeros
 - ones
 - empty
 - rand
 - arange

"""
# <demo> stop

# <demo> stop
arr_val = np.zeros((4,3))
print >> sys.stdout, arr_val
# <demo> stop

# <demo> stop
arr_val = np.ones((4,3))
print >> sys.stdout, arr_val
# <demo> stop

# <demo> stop
arr_val = np.empty((4,3))
print >> sys.stdout, arr_val
# <demo> stop

# <demo> stop
arr_val = np.random.rand(4,3)
print >> sys.stdout, arr_val
# <demo> stop

# <demo> stop
arr_val = np.arange(12).reshape(4,3)
print >> sys.stdout, arr_val
# <demo> stop


# <demo> silent
print >> sys.stdout, """

Basic Operations
----------------

"""
# <demo> stop

# <demo> silent 

print >> sys.stdout, """
Arithmetic operators on arrays apply elementwise.
A new array is created and filled with the result


arr_val ^ 2

"""
print >> sys.stdout, "%s \n\n^\n\n %s\n\n=\n\n" % (arr_val, arr_val)
print >> sys.stdout, "%s\n\n" % arr_val ** 2
# <demo> stop

# <demo> silent 
print >> sys.stdout, "\n\narr_val + arr_val\n\n"
print >> sys.stdout, "%s \n\n+\n\n %s\n\n=\n\n" % (arr_val, arr_val)
print >> sys.stdout, "%s\n\n" % (arr_val + arr_val)
# <demo> stop

# <demo> silent
print >> sys.stdout, "\n\narr_val * arr_val\n\n"
print >> sys.stdout, "%s \n\n*\n\n %s\n\n=\n\n" % (arr_val, arr_val)
print >> sys.stdout, "%s\n\n" % (arr_val * arr_val)
print >> sys.stdout, """

Unlike in many matrix languages, the product operator "*" operates
elementwise. Matrix product is performed using the dot function
or creating matrix objects.

"""
# <demo> stop


# <demo> silent 
print >> sys.stdout, """
It is possible to perform some operations inplace so that new arrays
are not created.
"""
# <demo> stop

# <demo> stop
cpy_arr_val = arr_val.copy()
cpy_arr_val *= 2
print >> sys.stdout, "\n\n%s\n\n" % cpy_arr_val
# <demo> stop

# <demo> stop
print >> sys.stdout, """
When operating on arrays of different types,
the type of the resulting array corresponds to
the more percise one - Upcasting
"""
# <demo> stop

# <demo> stop
ns = np.ones((4,3), dtype=np.int32)
ds = np.zeros((4,3), dtype=np.float64)
ws = ns + ds
print >> sys.stdout, "ns\n\n=%s\n\nds=\n\n%s\n\nws=\n\n%s\n\n" % (ns, ds, ws)
print >> sys.stdout, "\n\ndtype\nns = %s\nds = %s\nws = %s\n\n" %  (ns.dtype, ds.dtype,
                                                       ws.dtype)

# <demo> stop

# <demo> stop
print >> sys.stdout, """unary operations like sum, max, min are methods on the
ndarray"""
print >> sys.stdout, "max = %d" % arr_val.max()
print >> sys.stdout, "min = %d" % arr_val.min()
print >> sys.stdout, "sum = %d" % arr_val.sum()
# <demo> stop

# <demo> stop
print >> sys.stdout, """unary operations like sum, max, min are methods on the
ndarray"""
print >> sys.stdout, "max = %s" % arr_val.max(axis=1)
print >> sys.stdout, "max = %s" % arr_val.max(axis=0)
print >> sys.stdout, "min = %s" % arr_val.min(axis=1)
print >> sys.stdout, "min = %s" % arr_val.min(axis=0)
print >> sys.stdout, "sum = %s" % arr_val.sum(axis=1)
print >> sys.stdout, "sum = %s" % arr_val.sum(axis=0)
# <demo> stop

# <demo> stop
print >> sys.stdout, """
Universal functions
NumPy provides familiar mathematical functions
, sin, cos, exp, etc. But in NumPy these functinions are called 
"universal functions"(ufunc). The reason for having such a name, 
within NumPy these functions operated on an array object elementwise, 
producing array as an output

they also have functions on them - reduce, etc...
"""

print >> sys.stdout, "%s\n\n" % np.sin(arr_val)
print >> sys.stdout, "%s\n\n" % np.sqrt(arr_val)
print >> sys.stdout, "%s\n\n" % np.average(arr_val)
print >> sys.stdout, "%s\n\n" % np.exp(arr_val)
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
