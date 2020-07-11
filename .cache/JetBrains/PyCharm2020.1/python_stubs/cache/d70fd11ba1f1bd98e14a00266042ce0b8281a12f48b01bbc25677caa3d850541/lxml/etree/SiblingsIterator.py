# encoding: utf-8
# module lxml.etree
# from /usr/lib/python3/dist-packages/lxml/etree.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from ._ElementMatchIterator import _ElementMatchIterator

class SiblingsIterator(_ElementMatchIterator):
    """
    SiblingsIterator(self, node, tag=None, preceding=False)
        Iterates over the siblings of an element.
    
        You can pass the boolean keyword ``preceding`` to specify the direction.
    """
    def __init__(self, node, tag=None, preceding=False): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7fb820af4fc0>'


