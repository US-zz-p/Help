"""A pypi demonstration vehicle.

.. moduleauthor:: Andrew Carter <andrew@invalid.com>

"""

from . import useful_1


def start1():
    ''' This starts this module running ... '''


def start2():
    ' This starts this module running ... '


def start3():
    ''' This starts this module running 1 ... '''

    ''' This starts this module running 2 ... '''

    ''' This starts this module running 3 ... '''


def start4():
    ' This starts this module running 1 ... '

    ' This starts this module running 2 ... '

    ' This starts this module running 3 ... '


def source_code():
    '''
    .. code-block:: python
       :emphasize-lines: 3,5

       def some_function():
           interesting = False
           print 'This line is highlighted.'
           print 'This one is not...'
           print '...but this one is.'
        '''


def source_code2():
    '''
    .. literalinclude:: ../usp/test_sphinx/pyplots/ellipses.py
       :language: python
       :emphasize-lines: 2,6-7,11-14
       :linenos:
    '''
    # :lines: 1,3,5-10,20-
    # http://www.sphinx-doc.org/en/stable/markup/code.html


print('Main')
