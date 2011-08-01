#log# Automatic Logger file. *** THIS MUST BE THE FIRST LINE ***
#log# DO NOT CHANGE THIS LINE OR THE TWO BELOW -* coding: UTF-8 *-
#log# opts = Struct({'__allownew': True, 'logfile': 'ipython_log.py'})
#log# args = []
#log# It is safe to make manual edits below here.
#log#-----------------------------------------------------------------------
ls
demo1_basic.py
!cat ../demo.array.programming.py
from IPython.demo import ClearIPDemo
execdemo = ClearIPDemo('demo1_basic.py', title='test')
execdemo
#[Out]# <IPython.demo.ClearIPDemo object at 0x101392f50>
execdemo()
# """A simple interactive demo of IPython's capabilities."""
#[Out]# "A simple interactive demo of IPython's capabilities."
# # 'the ? character provides help in many contexts:'
# ?
execdemo()
# # <demo> silent
# import sys
# # Let's quietly ensure that automagic is actually on
# from IPython import ipapi
# ip = ipapi.get()
# ip.options.automagic = True
execdemo()
%lsmagic
execdemo()
# # You can learn a lot about objects via ?, ?? and tab-completion
# import code
#[Out]# <module 'code' from '/System/Library/Frameworks/Python.framework/Versions/2.6/lib/python2.6/code.pyc'>
# code?
code
code?
execdemo()
# code??
execdemo()
# # You can also query individual objects
# code.interact?
execdemo()
# # Note the incorrect path for a function in a module, though:
# %pfile code.interact
# import inspect
# print 'File for `code`         :',inspect.getabsfile(code)
# print 'File for `code.interact`:',inspect.getabsfile(code.interact)
# print
# print "This is a bug in the stdlib, reported (yesterday) as:"
# print "http://python.org/sf/1666807"
execdemo()
# # Handy search facilities, useful with large objects/libraries
# import numpy
# numpy.*cos*?
execdemo()
# # What have we typed so far? Use the %hist magic.
# print "Normal invocation of history:"
# hist
execdemo()
# # You can also see your history without line numbers, for easy copy/paste
# hist -n
execdemo()
# # IPython can log everything you type, including outputs
# Sun, 31 Jul 2011 14:41:15
ls
# Sun, 31 Jul 2011 14:41:17
execdemo()
# Sun, 31 Jul 2011 14:41:18
# IPython can automatically call things for you
# Sun, 31 Jul 2011 14:41:18
def concat(a,b): return "Hello, "+a+" and "+b
# Sun, 31 Jul 2011 14:41:18
# This automatically puts parens for you:
# Sun, 31 Jul 2011 14:41:18
concat "Ladies","Gentlemen"
#[Out]# 'Hello, Ladies and Gentlemen'
# Sun, 31 Jul 2011 14:41:18
# And using ',' as the first char automatically quotes the arguments:
# Sun, 31 Jul 2011 14:41:18
,concat Ladies Gentlemen
#[Out]# 'Hello, Ladies and Gentlemen'
# Sun, 31 Jul 2011 14:44:28
execdemo()
# Sun, 31 Jul 2011 14:44:29
# You can easily access the OS
# Sun, 31 Jul 2011 14:44:29
ls
# Sun, 31 Jul 2011 14:44:32
execdemo()
# Sun, 31 Jul 2011 14:44:34
# And even make your own aliases
# Sun, 31 Jul 2011 14:44:34
alias lsext ls *.%s
# Sun, 31 Jul 2011 14:44:34
lsext py
# Sun, 31 Jul 2011 14:44:58
execdemo.back
#[Out]# <bound method ClearIPDemo.back of <IPython.demo.ClearIPDemo object at 0x101392f50>>
# Sun, 31 Jul 2011 14:45:03
execdemo()
# Sun, 31 Jul 2011 14:45:04
# The %run magic is the workhorse of a regular IPython workflow
# Sun, 31 Jul 2011 14:45:04
%run
# Sun, 31 Jul 2011 14:45:09
execdemo()
# Sun, 31 Jul 2011 14:45:12
# The arguments are passed to your program in sys.argv:
# Sun, 31 Jul 2011 14:45:12
print 'Using %run:'
# Sun, 31 Jul 2011 14:45:12
run args -foo -bar=3 --opt='hello Pycon'
# Sun, 31 Jul 2011 14:45:12
print
# Sun, 31 Jul 2011 14:45:12
print 'Calling a separate Python process:'
# Sun, 31 Jul 2011 14:45:12
!python args.py -foo -bar=3 --opt='hello Pycon'
# Sun, 31 Jul 2011 14:48:57
execdemo()
# Sun, 31 Jul 2011 14:48:59
# Variables defined in your program become available for further interactive
# Sun, 31 Jul 2011 14:48:59
# usage: 
# Sun, 31 Jul 2011 14:48:59
%run simple
# Sun, 31 Jul 2011 14:48:59
print
# Sun, 31 Jul 2011 14:48:59
print 'Now this is back in the interactive namespace:'
# Sun, 31 Jul 2011 14:48:59
y
#[Out]# 99
# Sun, 31 Jul 2011 14:48:59
s
#[Out]# 'a simple string'
# Sun, 31 Jul 2011 14:49:06
execdemo()
# Sun, 31 Jul 2011 14:49:21
history
# Sun, 31 Jul 2011 14:49:28
history -100
# Sun, 31 Jul 2011 14:51:33
ls
# Sun, 31 Jul 2011 14:51:55
execdemo = ClearIPDemo('demo2_adv.py', title='test')
# Sun, 31 Jul 2011 14:52:21
execdemo()
# Sun, 31 Jul 2011 14:52:21
"""Some slightly more advanced interactive features of IPython."""
#[Out]# 'Some slightly more advanced interactive features of IPython.'
# Sun, 31 Jul 2011 14:52:21
# <demo> silent
# Sun, 31 Jul 2011 14:52:21
import sys
# Sun, 31 Jul 2011 14:52:21
print "Internal cleanup from previous demo runs"
# Sun, 31 Jul 2011 14:52:21
!rm -f foo_* bar_*
# Sun, 31 Jul 2011 14:52:21
# Make a few files we'll rename later
# Sun, 31 Jul 2011 14:52:21
for i in range(5):
# Sun, 31 Jul 2011 14:52:21
    f = 'foo_%s' % i
# Sun, 31 Jul 2011 14:52:21
    !touch $f
# Sun, 31 Jul 2011 14:52:21
# Let's quietly ensure that automagic is actually on at first
# Sun, 31 Jul 2011 14:52:21
from IPython import ipapi
# Sun, 31 Jul 2011 14:52:21
ip = ipapi.get()
# Sun, 31 Jul 2011 14:52:21
ip.options.automagic = True
# Sun, 31 Jul 2011 14:55:36
execdemo()
# Sun, 31 Jul 2011 14:55:43
# You can also directly call the shell, even in loops, and capture shell output
# Sun, 31 Jul 2011 14:55:43
# easily:
# Sun, 31 Jul 2011 14:55:43
print "This command goes straight to the OS:"
# Sun, 31 Jul 2011 14:55:43
!ls foo_*
# Sun, 31 Jul 2011 14:55:43
print
# Sun, 31 Jul 2011 14:55:43
print "Here, we capture the same command into the variable `files`:"
# Sun, 31 Jul 2011 14:55:43
files = _ip.magic("sc -l = ls foo_*")
# Sun, 31 Jul 2011 14:55:43
print
# Sun, 31 Jul 2011 14:55:43
print "This loop calls into the shell with Python variables:"
# Sun, 31 Jul 2011 14:55:43
for i,f in enumerate(files):
# Sun, 31 Jul 2011 14:55:43
    new_name = 'bar_%03d' % i
# Sun, 31 Jul 2011 14:55:43
    !mv $f $new_name
# Sun, 31 Jul 2011 14:55:43
print "And the renamed files are:"
# Sun, 31 Jul 2011 14:55:43
!ls bar_*
# Sun, 31 Jul 2011 14:58:27
!ls foo*
# Sun, 31 Jul 2011 14:58:31
!ls foo_*
# Sun, 31 Jul 2011 14:58:38
ls
# Sun, 31 Jul 2011 15:02:38
ls
# Sun, 31 Jul 2011 15:02:41
execdemo()
# Sun, 31 Jul 2011 15:02:43
# We don't have time to cover it in detail, but the ipipe system has tons of
# Sun, 31 Jul 2011 15:02:43
# very, very neat features:
# Sun, 31 Jul 2011 15:02:43
from ipipe import *
# Sun, 31 Jul 2011 15:02:44
# This will open a curses-based browser (q to exit):
# Sun, 31 Jul 2011 15:02:44
iglob("*.py")
#[Out]# ipipe.iglob('*.py')
# Sun, 31 Jul 2011 15:02:51
# And this dumps to the screen:
# Sun, 31 Jul 2011 15:02:51
iglob("*.py") | idump
#[Out]# <ipipe.idump object at 0x101c27d50>
# Sun, 31 Jul 2011 15:02:51
print
# Sun, 31 Jul 2011 15:02:51
print "There's a lot more on the IPython site about ipipe!"
# Sun, 31 Jul 2011 15:03:05
execdemo()
# Sun, 31 Jul 2011 15:03:13
# Run provides easy access to information useful for developers.
# Sun, 31 Jul 2011 15:03:13
# You can easily get a timed run of a program
# Sun, 31 Jul 2011 15:03:13
%run -t wordfreqs.py new_design.lyx.gz
# Sun, 31 Jul 2011 15:03:27
execdemo()
# Sun, 31 Jul 2011 15:03:28
# Run your code under the profiler's control
# Sun, 31 Jul 2011 15:03:28
%run -p wordfreqs.py new_design.lyx.gz
# Sun, 31 Jul 2011 15:03:34
execdemo()
# Sun, 31 Jul 2011 15:03:36
# Or the debugger's (also see %prun)
# Sun, 31 Jul 2011 15:03:36
%run -d wordfreqs.py new_design.lyx.gz
# Sun, 31 Jul 2011 15:03:42
execdemo()
# Sun, 31 Jul 2011 15:03:50
# But code typically has bugs...
# Sun, 31 Jul 2011 15:03:50
# IPython can show you exceptions with various levels of detail
# Sun, 31 Jul 2011 15:03:50
# The xmode magic changes the exception reporting mode
# Sun, 31 Jul 2011 15:03:50
xmode Plain
# Sun, 31 Jul 2011 15:03:50
run error
# Sun, 31 Jul 2011 15:03:56
execdemo()
# Sun, 31 Jul 2011 15:03:58
# 'Context' is the default
# Sun, 31 Jul 2011 15:03:58
xmode Context
# Sun, 31 Jul 2011 15:03:58
run error
# Sun, 31 Jul 2011 15:04:03
execdemo()
# Sun, 31 Jul 2011 15:04:04
# And verbose provides a lot of detail, including variable values
# Sun, 31 Jul 2011 15:04:04
xmode Verbose
# Sun, 31 Jul 2011 15:04:04
run error
# Sun, 31 Jul 2011 15:04:07
execdemo()
# Sun, 31 Jul 2011 15:04:09
# You can do post-mortem debug of any crashed program:
# Sun, 31 Jul 2011 15:04:09
%debug
# Sun, 31 Jul 2011 15:04:38
execdemo()
# Sun, 31 Jul 2011 15:04:38
# <demo> silent
# Sun, 31 Jul 2011 15:04:38
print "Final cleanup of temporary files..."
# Sun, 31 Jul 2011 15:04:38
!rm -f foo_* bar_*
# Sun, 31 Jul 2011 15:05:16
run demo3_qt4.py
# Sun, 31 Jul 2011 15:05:23
import PyQt4
# Sun, 31 Jul 2011 15:05:44
run demo4_pylab.py
