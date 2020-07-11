# encoding: utf-8
# module typing.io
# from /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/scipy/signal/_upfirdn_apply.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
""" Wrapper namespace for IO generic classes. """

# imports
import typing as __typing


# no functions
# classes

class IO(__typing.Generic):
    """
    Generic base class for TextIO and BinaryIO.
    
        This is an abstract, generic version of the return of open().
    
        NOTE: This does not distinguish between the different possible
        classes (text vs. binary, read vs. write vs. read/write,
        append-only, unbuffered).  The TextIO and BinaryIO subclasses
        below capture the distinctions between text vs. binary, which is
        pervasive in the interface; however we currently do not offer a
        way to track the other distinctions in the type system.
    """
    def close(self): # reliably restored by inspect
        # no doc
        pass

    def closed(self): # reliably restored by inspect
        # no doc
        pass

    def fileno(self): # reliably restored by inspect
        # no doc
        pass

    def flush(self): # reliably restored by inspect
        # no doc
        pass

    def isatty(self): # reliably restored by inspect
        # no doc
        pass

    def read(self, n=-1): # reliably restored by inspect
        # no doc
        pass

    def readable(self): # reliably restored by inspect
        # no doc
        pass

    def readline(self, limit=-1): # reliably restored by inspect
        # no doc
        pass

    def readlines(self, hint=-1): # reliably restored by inspect
        # no doc
        pass

    def seek(self, offset, whence=0): # reliably restored by inspect
        # no doc
        pass

    def seekable(self): # reliably restored by inspect
        # no doc
        pass

    def tell(self): # reliably restored by inspect
        # no doc
        pass

    def truncate(self, size=None): # reliably restored by inspect
        # no doc
        pass

    def writable(self): # reliably restored by inspect
        # no doc
        pass

    def write(self, s): # reliably restored by inspect
        # no doc
        pass

    def writelines(self, lines): # reliably restored by inspect
        # no doc
        pass

    def __enter__(self): # reliably restored by inspect
        # no doc
        pass

    def __exit__(self, type, value, traceback): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    mode = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    name = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _abc_cache = None # (!) real value is '<_weakrefset.WeakSet object at 0x7f26007268d0>'
    _abc_negative_cache = None # (!) real value is '<_weakrefset.WeakSet object at 0x7f2600726940>'
    _abc_negative_cache_version = 46
    _abc_registry = None # (!) real value is '<_weakrefset.WeakSet object at 0x7f2600726898>'
    __abstractmethods__ = frozenset({'close', 'closed', 'readable', 'name', 'isatty', 'read', '__enter__', 'readlines', '__exit__', 'readline', 'writable', 'seek', 'truncate', 'seekable', 'write', 'mode', 'tell', 'writelines', 'flush', 'fileno'})
    __args__ = None
    __extra__ = None
    __next_in_mro__ = object
    __origin__ = None
    __parameters__ = (
        None, # (!) real value is '~AnyStr'
    )
    __slots__ = ()


class BinaryIO(__typing.IO):
    """ Typed version of the return of open() in binary mode. """
    def write(self, s): # reliably restored by inspect
        # no doc
        pass

    def __enter__(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    _abc_cache = None # (!) real value is '<_weakrefset.WeakSet object at 0x7f2600726c18>'
    _abc_negative_cache = None # (!) real value is '<_weakrefset.WeakSet object at 0x7f2600726c88>'
    _abc_negative_cache_version = 46
    _abc_registry = None # (!) real value is '<_weakrefset.WeakSet object at 0x7f2600726be0>'
    __abstractmethods__ = frozenset({'close', 'closed', 'readable', 'name', 'isatty', 'read', '__enter__', 'readlines', '__exit__', 'readline', 'writable', 'seek', 'truncate', 'write', 'seekable', 'mode', 'tell', 'writelines', 'flush', 'fileno'})
    __args__ = None
    __extra__ = None
    __next_in_mro__ = object
    __origin__ = None
    __parameters__ = ()
    __slots__ = ()


class TextIO(__typing.IO):
    """ Typed version of the return of open() in text mode. """
    def __enter__(self): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    buffer = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    encoding = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    errors = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    line_buffering = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    newlines = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default


    _abc_cache = None # (!) real value is '<_weakrefset.WeakSet object at 0x7f2600726f60>'
    _abc_negative_cache = None # (!) real value is '<_weakrefset.WeakSet object at 0x7f2600726fd0>'
    _abc_negative_cache_version = 46
    _abc_registry = None # (!) real value is '<_weakrefset.WeakSet object at 0x7f2600726ef0>'
    __abstractmethods__ = frozenset({'line_buffering', 'close', 'encoding', 'closed', 'readable', 'name', 'isatty', 'read', '__enter__', 'readlines', '__exit__', 'readline', 'errors', 'writable', 'seek', 'truncate', 'seekable', 'write', 'mode', 'buffer', 'tell', 'writelines', 'flush', 'newlines', 'fileno'})
    __args__ = None
    __extra__ = None
    __next_in_mro__ = object
    __origin__ = None
    __parameters__ = ()
    __slots__ = ()


# variables with complex values

__all__ = [
    'IO',
    'TextIO',
    'BinaryIO',
]

__weakref__ = None # (!) real value is "<attribute '__weakref__' of 'typing.io' objects>"

