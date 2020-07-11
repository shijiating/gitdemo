# encoding: utf-8
# module scanext
# from /usr/lib/python3/dist-packages/scanext.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
""" Python extension for HP scan sane driver """
# no imports

# Variables with simple values

CAP_ADVANCED = 64
CAP_AUTOMATIC = 16
CAP_EMULATED = 8

CAP_HARD_SELECT = 2

CAP_INACTIVE = 32

CAP_SOFT_DETECT = 4
CAP_SOFT_SELECT = 1

CONSTRAINT_NONE = 0
CONSTRAINT_RANGE = 1

CONSTRAINT_STRING_LIST = 3

CONSTRAINT_WORD_LIST = 2

FRAME_BLUE = 4
FRAME_GRAY = 0
FRAME_GREEN = 3
FRAME_RED = 2
FRAME_RGB = 1

INFO_INEXACT = 1

INFO_RELOAD_OPTIONS = 2
INFO_RELOAD_PARAMS = 4

MAX_READSIZE = 65536

RELOAD_PARAMS = 4

SANE_STATUS_ACCESS_DENIED = 11

SANE_STATUS_CANCELLED = 2

SANE_STATUS_COVER_OPEN = 8

SANE_STATUS_DEVICE_BUSY = 3

SANE_STATUS_EOF = 5
SANE_STATUS_GOOD = 0
SANE_STATUS_INVAL = 4

SANE_STATUS_IO_ERROR = 9

SANE_STATUS_JAMMED = 6

SANE_STATUS_NO_DOCS = 7
SANE_STATUS_NO_MEM = 10

SANE_STATUS_UNSUPPORTED = 1

SANE_WORD_SIZE = 4

TYPE_BOOL = 0
TYPE_BUTTON = 4
TYPE_FIXED = 2
TYPE_GROUP = 5
TYPE_INT = 1
TYPE_STRING = 3

UNIT_BIT = 2
UNIT_DPI = 4
UNIT_MICROSECOND = 6
UNIT_MM = 3
UNIT_NONE = 0
UNIT_PERCENT = 5
UNIT_PIXEL = 1

# functions

def deInit(*args, **kwargs): # real signature unknown
    pass

def getDevices(*args, **kwargs): # real signature unknown
    pass

def getErrorMessage(*args, **kwargs): # real signature unknown
    pass

def init(*args, **kwargs): # real signature unknown
    pass

def isOptionActive(*args, **kwargs): # real signature unknown
    pass

def isOptionSettable(*args, **kwargs): # real signature unknown
    pass

def openDevice(*args, **kwargs): # real signature unknown
    pass

# classes

class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fb820afacf8>'

__spec__ = None # (!) real value is "ModuleSpec(name='scanext', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fb820afacf8>, origin='/usr/lib/python3/dist-packages/scanext.cpython-35m-x86_64-linux-gnu.so')"

