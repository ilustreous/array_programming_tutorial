"""A simple Qt demo to show IPython's support for non-blocking GUIs.

The same thing can be done with GTK, WX, Qt3 and Qt4 (in addition to Tk, which
Python supports out of the box).
"""

import qt

w = qt.QPushButton( 'A trivial Qt app: a button.', None )
qt.qApp.setMainWidget( w )
w.show()

# <demo> stop
# Note that IPython keeps on working:
print "hello world"

# <demo> stop
# Now, change the text on the widget.
w.setText("Hello PyCon 2007")
