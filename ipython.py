#Adapted from scipy conference talk by f.perez and b.graner (Texas '07)

# <demo> silent
import sys

from IPython import ipapi
ip = ipapi.get()
ip.options.automagic = True


print "The '?' provides help in many contexts"
# <demo> stop


# <demo> silent
print """Magic commands are very useful. 

They provide support for altering the behavior of IPython 
and system features/programs. 

Use %lsmagic to list all magic commands.

Use '?' for help on what specific magic commands do. 

"""
# <demo> stop

# <demo> silent
print r"""Learn about objects with '?' and '??' and tab completion.
    - '?' will show doc strings.
    - '??' will show source code.

# import code

# code?

# code??

# code. <tab>

"""
# <demo> stop


# <demo> silent
print """Learn about functions too.

# code.Command<tab>
 
# code.CommandCompiler?

# code.CommandCompiler??

"""
# <demo> stop


# <demo> silent
print """Searching for a function in a large code base.

# import numpy

# numpy.*cos*?

"""
# <demo> stop

# <demo> silent
print """Let's see what commands we have used by checking our history.

# hist 

or 

# hist -n (no line numbers)

"""
# <demo> stop


# <demo> silent
print """Let's execute a command from history

# x = 4

# x += 1

# hist

# exec In[somenumber]

"""
# <demo> stop

# <demo> silent
print """Log what you type.

# logstart -o -r -t mylog.txt append

Do logstart? for agument details.

Run a bunch of python commands. 

# \"cat\" your log file to see what it logged.

# stop log with the \"logstop\" magic command
"""
# <demo> stop

# <demo> silent
def concat(a, b):
    return a + b

print """Puts parens around for you.

# concat 'hello', 'world'

comma in front of concat will quote words.

# ,concat hello world

"""
# <demo> stop


# <demo> silent
print """%run magic command for running python scripts.

# run -i args 'these' 'are' 'passed' 'to' 'args.py'

"""
# <demo> stop

# <demo> silent
print """%run magic command for running python scripts.

Variables from simple.py are put into your ipython session

# run -i simple

"""
# <demo> stop



# <demo> silent

import os

if not os.path.exists('ipython_scratch'):
    os.mkdir('ipython_scratch')

for i in range(5):
    f = 'ipython_scratch/foo_%s' % i
    open(f, 'w').close()

print """capture file information.

# files = !ls ipython_scratch/foo_*

"""
# <demo> stop


# <demo> silent

print """Can capture shell ouput inside of a loop.

for i,f in enumerate(files):
    new_name = f.replace('foo', 'bar')
    # !cp $f $new_name   # remove the '#' in front of this line
"""

# <demo> stop



# <demo> silent
print """Let's go back to run command.

With the run command we can time our programs.

# run -t ipython_tutorial/wordfreqs.py ipython.py


"""
# <demo> stop

# <demo> silent
print """ With the run command we can profile our programs.

# run -p ipython_tutorial/wordfreqs.py ipython.py


"""
# <demo> stop

# <demo> silent
print """ With the run command we can debug our programs.
Break point and go up and down the stack.

# run -d -b37 ipython_tutorial/wordfreqs.py ipython.py

"""
# <demo> stop

# <demo> silent
print """xmode can change the debug level

# xmode Plain
# xmode Context (default)
# xmode Verbose 

# run ipython_tutorial/error.py with each of these modes.

"""
# <demo> stop
