"""Some slightly more advanced interactive features of IPython."""

# <demo> silent
import sys

print "Internal cleanup from previous demo runs"
!rm -f foo_* bar_*

# Make a few files we'll rename later
for i in range(5):
    f = 'foo_%s' % i
    !touch $f

# Let's quietly ensure that automagic is actually on at first
from IPython import ipapi
ip = ipapi.get()
ip.options.automagic = True

# <demo> stop

# You can also directly call the shell, even in loops, and capture shell output
# easily:

print "This command goes straight to the OS:"
!ls foo_*
print
print "Here, we capture the same command into the variable `files`:"
files =! ls foo_*
print
print "This loop calls into the shell with Python variables:"
for i,f in enumerate(files):
    new_name = 'bar_%03d' % i
    !mv $f $new_name

print "And the renamed files are:"
!ls bar_*

# <demo> stop
# We don't have time to cover it in detail, but the ipipe system has tons of
# very, very neat features:

from ipipe import *
# This will open a curses-based browser (q to exit):
iglob("*.py")

# And this dumps to the screen:
iglob("*.py") | idump

print
print "There's a lot more on the IPython site about ipipe!"

# <demo> stop
# Run provides easy access to information useful for developers.
# You can easily get a timed run of a program
%run -t wordfreqs.py new_design.lyx.gz

# <demo> stop
# Run your code under the profiler's control
%run -p wordfreqs.py new_design.lyx.gz

# <demo> stop
# Or the debugger's (also see %prun)
%run -d wordfreqs.py new_design.lyx.gz

# <demo> stop
# But code typically has bugs...
# IPython can show you exceptions with various levels of detail
# The xmode magic changes the exception reporting mode
xmode Plain
run error

# <demo> stop
# 'Context' is the default
xmode Context
run error

# <demo> stop
# And verbose provides a lot of detail, including variable values
xmode Verbose
run error

# <demo> stop
# You can do post-mortem debug of any crashed program:
%debug

# <demo> stop
# <demo> silent
print "Final cleanup of temporary files..."
!rm -f foo_* bar_*
