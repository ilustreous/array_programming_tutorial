"""A simple Qt demo to show IPython's support for non-blocking GUIs.

The same thing can be done with GTK, WX, Qt3 and Qt4 (in addition to Tk, which
Python supports out of the box).
"""

# wiggly is part of the Qt4 tutorials
from wiggly import Dialog, QtGui

app = QtGui.QApplication()
dialog = Dialog()
dialog.show()
app.exec_()

# <demo> stop

# Note that IPython keeps on working:
print "hello world"

# <demo> stop

# Now, change the text on the widget.
dialog.lineEdit.setText('Hello PyCon2007!')
