# encoding: utf-8
# module sklearn.utils._weight_vector
# from /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/utils/_weight_vector.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/numpy/__init__.py

# functions

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class WeightVector(object):
    """
    Dense vector represented by a scalar and a numpy array.
    
        The class provides methods to ``add`` a sparse vector
        and scale the vector.
        Representing a vector explicitly as a scalar times a
        vector allows for efficient scaling operations.
    
        Attributes
        ----------
        w : ndarray, dtype=double, order='C'
            The numpy array which backs the weight vector.
        aw : ndarray, dtype=double, order='C'
            The numpy array which backs the average_weight vector.
        wscale : double
            The scale of the vector.
        n_features : int
            The number of features (= dimensionality of ``w``).
        sq_norm : double
            The squared norm of ``w``.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __reduce__(self, *args, **kwargs): # real signature unknown
        pass

    def __setstate__(self, *args, **kwargs): # real signature unknown
        pass

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f260e159f00>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f260d1e4e10>'

__spec__ = None # (!) real value is "ModuleSpec(name='sklearn.utils._weight_vector', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f260d1e4e10>, origin='/home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/utils/_weight_vector.cpython-35m-x86_64-linux-gnu.so')"

__test__ = {}

