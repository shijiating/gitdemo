# encoding: utf-8
# module lxml.etree
# from /usr/lib/python3/dist-packages/lxml/etree.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
""" The ``lxml.etree`` module implements the extended ElementTree API for XML. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

from .SchematronError import SchematronError

class SchematronParseError(SchematronError):
    """ Error while parsing an XML document as Schematron schema. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass


