# encoding: utf-8
# module _sre
# from (built-in)
# by generator 1.147
# no doc
# no imports

# Variables with simple values

CODESIZE = 4

copyright = ' SRE 2.2.2 Copyright (c) 1997-2002 by Secret Labs AB '

MAGIC = 20140917
MAXGROUPS = 2147483647
MAXREPEAT = 4294967295

# functions

def compile(*args, **kwargs): # real signature unknown
    pass

def getcodesize(*args, **kwargs): # real signature unknown
    pass

def getlower(*args, **kwargs): # real signature unknown
    pass

# classes

class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    @classmethod
    def create_module(cls, *args, **kwargs): # real signature unknown
        """ Create a built-in module """
        pass

    @classmethod
    def exec_module(cls, *args, **kwargs): # real signature unknown
        """ Exec a built-in module """
        pass

    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module instead.
        """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'create_module': <classmethod object at 0x7fb256f6bd68>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, 'module_repr': <staticmethod object at 0x7fb256f6bc88>, 'find_module': <classmethod object at 0x7fb256f6bd30>, 'get_code': <classmethod object at 0x7fb256f6be10>, 'find_spec': <classmethod object at 0x7fb256f6bcc0>, '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '__module__': '_frozen_importlib', 'get_source': <classmethod object at 0x7fb256f6be80>, 'load_module': <classmethod object at 0x7fb256f6bf28>, 'is_package': <classmethod object at 0x7fb256f6bef0>, 'exec_module': <classmethod object at 0x7fb256f6bda0>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

__spec__ = None # (!) real value is "ModuleSpec(name='_sre', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

