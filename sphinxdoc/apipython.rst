.. _ipython:

=======
IPython
=======


Go through `Setup <pythonsetup.html>`_ if you haven't done so already.


Tools
=====

- Yes, we are using windows, `unfortunately`.

  - But that's ok - to help alleviate

    - Spyder_.: **S** cientific **Py** thon **D** evelopment **E** nvi **r** onment::

        > spyder


    - Using the exisiting command prompt is fine too but spyder is akin to 
      Matlab if people are familiar with it.

    - Console2_: for people who just want a better console.

- Editor

  - vi (`vim <http://www.vim.org/>`_, `gvim <http://gvim.en.softonic.com>`_)

Why Python/IPython ?
====================

**We're not building applications, we're building data.**

To build data we have to interactive with it first.

Python/IPython have the qualities for good interactive programming:
 
 - Dynamic code evaluation
 - No variable declaration
 - Powerful introspection
 - Object model
 - Functional model
 - String processing
 - Module system

- Growing ecosystem for the programming language and scientific computing

- Product development = edit/compile/run loop

- Exploratory computing = execute/explore loop


- our glue language between
  
  - soqrates
 
  - fido
  
  - condor scheduler
 
  - map-reduce architecture
 
  - scipy
 
  - numpy
 
  - matplotlib
 
  - hdf5

- Tight feedback loop between trader->developer->quant. 
   
- Enables us to work collabratively. 
    
  - We are able to gather around 1 ipython session and explore our simulation's results and evolve our trading strategies accordingly. 
 
- IPython Shell mode used as a bash shell replacement but we still have the freedom use the canonical unix, it's actually easier.

  - grep
  - awk
  - sed
  - find
  - xargs



============
IPython Demo
============

Walk through of IPython.

 - start up ipython::
   
    > ipython

 - When loaded up::

    > run demo.ipython.py


.. _Spyder: http://packages.python.org/spyder/
.. _Console2: http://sourceforge.net/projects/console/ 

