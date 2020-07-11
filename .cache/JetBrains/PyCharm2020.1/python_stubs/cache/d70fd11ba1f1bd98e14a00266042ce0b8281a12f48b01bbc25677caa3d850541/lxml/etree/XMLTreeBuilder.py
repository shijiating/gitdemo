# encoding: utf-8
# module lxml.etree
# from /usr/lib/python3/dist-packages/lxml/etree.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .XMLParser import XMLParser

class XMLTreeBuilder(XMLParser):
    """
    ETCompatXMLParser(self, encoding=None, attribute_defaults=False,                  dtd_validation=False, load_dtd=False, no_network=True,                  ns_clean=False, recover=False, schema=None,                  huge_tree=False, remove_blank_text=False, resolve_entities=True,                  remove_comments=True, remove_pis=True, strip_cdata=True,                  target=None, compact=True)
    
        An XML parser with an ElementTree compatible default setup.
    
        See the XMLParser class for details.
    
        This parser has ``remove_comments`` and ``remove_pis`` enabled by default
        and thus ignores comments and processing instructions.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7fb820b27750>'


