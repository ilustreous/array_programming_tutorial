"""A simple interactive demo of IPython's capabilities."""

# 'the ? character provides help in many contexts:'
?
# <demo> stop

# <demo> silent
import sys

# Let's quietly ensure that automagic is actually on
from IPython import ipapi
ip = ipapi.get()
ip.options.automagic = True

# <demo> stop

# IPython's magic commands are very useful, and fully user-configurable:
# This will show you all currently available magics:
lsmagic

# <demo> stop
# You can learn a lot about objects via ?, ?? and tab-completion
import code
code?

# <demo> stop
code??

# <demo> stop
# You can also query individual objects
code.interact?

# <demo> stop
# Note the incorrect path for a function in a module, though:
%pfile code.interact

import inspect
print 'File for `code`         :',inspect.getabsfile(code)
print 'File for `code.interact`:',inspect.getabsfile(code.interact)
print
print "This is a bug in the stdlib, reported (yesterday) as:"
print "http://python.org/sf/1666807"

# <demo> stop
# Handy search facilities, useful with large objects/libraries
import numpy
numpy.*cos*?

# <demo> stop
# What have we typed so far? Use the %hist magic.
print "Normal invocation of history:"
hist

# <demo> stop
# You can also see your history without line numbers, for easy copy/paste
hist -n

# <demo> stop
# IPython can log everything you type, including outputs
logstart -o -r -t

# <demo> stop
# IPython can automatically call things for you
def concat(a,b): return "Hello, "+a+" and "+b

# This automatically puts parens for you:
concat "Ladies","Gentlemen"


# And using ',' as the first char automatically quotes the arguments:
,concat Ladies Gentlemen

# <demo> stop
# You can easily access the OS
ls

# <demo> stop
# And even make your own aliases
alias lsext ls *.%s
lsext py

# <demo> stop
# The %run magic is the workhorse of a regular IPython workflow
%run?

# <demo> stop
# The arguments are passed to your program in sys.argv:
print 'Using %run:'
run args -foo -bar=3 --opt='hello Pycon'
print
print 'Calling a separate Python process:'
!python args.py -foo -bar=3 --opt='hello Pycon'

# <demo> stop
# Variables defined in your program become available for further interactive
# usage: 
%run simple
print
print 'Now this is back in the interactive namespace:'
y
s
