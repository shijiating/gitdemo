# encoding: utf-8
# module lxml.etree
# from /usr/lib/python3/dist-packages/lxml/etree.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .FallbackElementClassLookup import FallbackElementClassLookup

class AttributeBasedElementClassLookup(FallbackElementClassLookup):
    """
    AttributeBasedElementClassLookup(self, attribute_name, class_mapping, fallback=None)
        Checks an attribute of an Element and looks up the value in a
        class dictionary.
    
        Arguments:
          - attribute name - '{ns}name' style string
          - class mapping  - Python dict mapping attribute values to Element classes
          - fallback       - optional fallback lookup mechanism
    
        A None key in the class mapping will be checked if the attribute is
        missing.
    """
    def __init__(self, attribute_name, class_mapping, fallback=None): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7fb820b27300>'


