# encoding: utf-8
# module numpy.random._common
# from /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/numpy/random/_common.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import sys as sys # <module 'sys' (built-in)>
import numpy as np # /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/numpy/__init__.py
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def namedtuple(typename, field_names, verbose=False, rename=False): # reliably restored by inspect
    """
    Returns a new subclass of tuple with named fields.
    
        >>> Point = namedtuple('Point', ['x', 'y'])
        >>> Point.__doc__                   # docstring for the new class
        'Point(x, y)'
        >>> p = Point(11, y=22)             # instantiate with positional args or keywords
        >>> p[0] + p[1]                     # indexable like a plain tuple
        33
        >>> x, y = p                        # unpack like a regular tuple
        >>> x, y
        (11, 22)
        >>> p.x + p.y                       # fields also accessible by name
        33
        >>> d = p._asdict()                 # convert to a dictionary
        >>> d['x']
        11
        >>> Point(**d)                      # convert from a dictionary
        Point(x=11, y=22)
        >>> p._replace(x=100)               # _replace() is like str.replace() but targets named fields
        Point(x=100, y=22)
    """
    pass

# classes

class interface(tuple):
    """ interface(state_address, state, next_uint64, next_uint32, next_double, bit_generator) """
    def _asdict(self): # reliably restored by inspect
        """ Return a new OrderedDict which maps field names to their values. """
        pass

    @classmethod
    def _make(cls, *args, **kwargs): # real signature unknown
        """ Make a new interface object from a sequence or iterable """
        pass

    def _replace(_self, **kwds): # reliably restored by inspect
        """ Return a new interface object replacing specified fields with new values """
        pass

    def __getnewargs__(self): # reliably restored by inspect
        """ Return self as a plain tuple.  Used by copy and pickle. """
        pass

    def __init__(self, state_address, state, next_uint64, next_uint32, next_double, bit_generator): # real signature unknown; restored from __doc__
        pass

    @staticmethod # known case of __new__
    def __new__(_cls, state_address, state, next_uint64, next_uint32, next_double, bit_generator): # reliably restored by inspect
        """ Create new instance of interface(state_address, state, next_uint64, next_uint32, next_double, bit_generator) """
        pass

    def __repr__(self): # reliably restored by inspect
        """ Return a nicely formatted representation string """
        pass

    bit_generator = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 5"""

    next_double = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 4"""

    next_uint32 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 3"""

    next_uint64 = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 2"""

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 1"""

    state_address = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Alias for field number 0"""


    _fields = (
        'state_address',
        'state',
        'next_uint64',
        'next_uint32',
        'next_double',
        'bit_generator',
    )
    _source = "from builtins import property as _property, tuple as _tuple\nfrom operator import itemgetter as _itemgetter\nfrom collections import OrderedDict\n\nclass interface(tuple):\n    'interface(state_address, state, next_uint64, next_uint32, next_double, bit_generator)'\n\n    __slots__ = ()\n\n    _fields = ('state_address', 'state', 'next_uint64', 'next_uint32', 'next_double', 'bit_generator')\n\n    def __new__(_cls, state_address, state, next_uint64, next_uint32, next_double, bit_generator):\n        'Create new instance of interface(state_address, state, next_uint64, next_uint32, next_double, bit_generator)'\n        return _tuple.__new__(_cls, (state_address, state, next_uint64, next_uint32, next_double, bit_generator))\n\n    @classmethod\n    def _make(cls, iterable, new=tuple.__new__, len=len):\n        'Make a new interface object from a sequence or iterable'\n        result = new(cls, iterable)\n        if len(result) != 6:\n            raise TypeError('Expected 6 arguments, got %d' % len(result))\n        return result\n\n    def _replace(_self, **kwds):\n        'Return a new interface object replacing specified fields with new values'\n        result = _self._make(map(kwds.pop, ('state_address', 'state', 'next_uint64', 'next_uint32', 'next_double', 'bit_generator'), _self))\n        if kwds:\n            raise ValueError('Got unexpected field names: %r' % list(kwds))\n        return result\n\n    def __repr__(self):\n        'Return a nicely formatted representation string'\n        return self.__class__.__name__ + '(state_address=%r, state=%r, next_uint64=%r, next_uint32=%r, next_double=%r, bit_generator=%r)' % self\n\n    def _asdict(self):\n        'Return a new OrderedDict which maps field names to their values.'\n        return OrderedDict(zip(self._fields, self))\n\n    def __getnewargs__(self):\n        'Return self as a plain tuple.  Used by copy and pickle.'\n        return tuple(self)\n\n    state_address = _property(_itemgetter(0), doc='Alias for field number 0')\n\n    state = _property(_itemgetter(1), doc='Alias for field number 1')\n\n    next_uint64 = _property(_itemgetter(2), doc='Alias for field number 2')\n\n    next_uint32 = _property(_itemgetter(3), doc='Alias for field number 3')\n\n    next_double = _property(_itemgetter(4), doc='Alias for field number 4')\n\n    bit_generator = _property(_itemgetter(5), doc='Alias for field number 5')\n\n"
    __slots__ = ()


# variables with complex values

__all__ = [
    'interface',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f11a51e0fd0>'

__pyx_capi__ = {
    'LEGACY_POISSON_LAM_MAX': None, # (!) real value is '<capsule object "double" at 0x7f11a6224840>'
    'MAXSIZE': None, # (!) real value is '<capsule object "uint64_t" at 0x7f11a6224870>'
    'POISSON_LAM_MAX': None, # (!) real value is '<capsule object "double" at 0x7f11a6224810>'
    'benchmark': None, # (!) real value is '<capsule object "PyObject *(bitgen_t *, PyObject *, Py_ssize_t, PyObject *)" at 0x7f11a62248a0>'
    'check_array_constraint': None, # (!) real value is '<capsule object "int (PyArrayObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type)" at 0x7f11a6224990>'
    'check_constraint': None, # (!) real value is '<capsule object "int (double, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type)" at 0x7f11a6224960>'
    'cont': None, # (!) real value is '<capsule object "PyObject *(void *, void *, PyObject *, PyObject *, int, PyObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyObject *)" at 0x7f11a6224ae0>'
    'cont_broadcast_3': None, # (!) real value is '<capsule object "PyObject *(void *, void *, PyObject *, PyObject *, PyArrayObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyArrayObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyArrayObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type)" at 0x7f11a6224b70>'
    'cont_f': None, # (!) real value is '<capsule object "PyObject *(void *, bitgen_t *, PyObject *, PyObject *, PyObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyObject *)" at 0x7f11a6224b40>'
    'disc': None, # (!) real value is '<capsule object "PyObject *(void *, void *, PyObject *, PyObject *, int, int, PyObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type)" at 0x7f11a6224b10>'
    'discrete_broadcast_iii': None, # (!) real value is '<capsule object "PyObject *(void *, void *, PyObject *, PyObject *, PyArrayObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyArrayObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type, PyArrayObject *, PyObject *, __pyx_t_5numpy_6random_7_common_constraint_type)" at 0x7f11a6224ba0>'
    'double_fill': None, # (!) real value is '<capsule object "PyObject *(void *, bitgen_t *, PyObject *, PyObject *, PyObject *)" at 0x7f11a62249f0>'
    'float_fill': None, # (!) real value is '<capsule object "PyObject *(void *, bitgen_t *, PyObject *, PyObject *, PyObject *)" at 0x7f11a6224a20>'
    'float_fill_from_double': None, # (!) real value is '<capsule object "PyObject *(void *, bitgen_t *, PyObject *, PyObject *, PyObject *)" at 0x7f11a6224a50>'
    'int_to_array': None, # (!) real value is '<capsule object "PyArrayObject *(PyObject *, PyObject *, PyObject *, PyObject *)" at 0x7f11a6224ab0>'
    'kahan_sum': None, # (!) real value is '<capsule object "double (double *, npy_intp)" at 0x7f11a62249c0>'
    'prepare_cffi': None, # (!) real value is '<capsule object "PyObject *(bitgen_t *)" at 0x7f11a6224900>'
    'prepare_ctypes': None, # (!) real value is '<capsule object "PyObject *(bitgen_t *)" at 0x7f11a6224930>'
    'random_raw': None, # (!) real value is '<capsule object "PyObject *(bitgen_t *, PyObject *, PyObject *, PyObject *)" at 0x7f11a62248d0>'
    'wrap_int': None, # (!) real value is '<capsule object "PyObject *(PyObject *, PyObject *)" at 0x7f11a6224a80>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='numpy.random._common', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f11a51e0fd0>, origin='/home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/numpy/random/_common.cpython-35m-x86_64-linux-gnu.so')"

__test__ = {}

