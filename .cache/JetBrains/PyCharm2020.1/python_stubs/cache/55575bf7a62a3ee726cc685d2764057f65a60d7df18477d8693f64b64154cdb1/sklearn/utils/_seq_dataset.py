# encoding: utf-8
# module sklearn.utils._seq_dataset
# from /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/utils/_seq_dataset.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
"""
Dataset abstractions for sequential data access.
WARNING: Do not edit .pyx file directly, it is generated from .pyx.tp
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/numpy/__init__.py

# no functions
# classes

class SequentialDataset32(object):
    """
    Base class for datasets with sequential data access.
    
        SequentialDataset is used to iterate over the rows of a matrix X and
        corresponding target values y, i.e. to iterate over samples.
        There are two methods to get the next sample:
            - next : Iterate sequentially (optionally randomized)
            - random : Iterate randomly (with replacement)
    
        Attributes
        ----------
        index : np.ndarray
            Index array for fast shuffling.
    
        index_data_ptr : int
            Pointer to the index array.
    
        current_index : int
            Index of current sample in ``index``.
            The index of current sample in the data is given by
            index_data_ptr[current_index].
    
        n_samples : Py_ssize_t
            Number of samples in the dataset.
    
        seed : np.uint32_t
            Seed used for random sampling.
    """
    def _next_py(self, *args, **kwargs): # real signature unknown
        """ python function used for easy testing """
        pass

    def _random_py(self, *args, **kwargs): # real signature unknown
        """ python function used for easy testing """
        pass

    def _sample_py(self, *args, **kwargs): # real signature unknown
        """ python function used for easy testing """
        pass

    def _shuffle_py(self, *args, **kwargs): # real signature unknown
        """ python function used for easy testing """
        pass

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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25f5b31480>'


class ArrayDataset32(SequentialDataset32):
    """
    Dataset backed by a two-dimensional numpy array.
    
        The dtype of the numpy array is expected to be ``np.float32`` (float)
        and C-style memory layout.
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25f5b314b0>'


class SequentialDataset64(object):
    """
    Base class for datasets with sequential data access.
    
        SequentialDataset is used to iterate over the rows of a matrix X and
        corresponding target values y, i.e. to iterate over samples.
        There are two methods to get the next sample:
            - next : Iterate sequentially (optionally randomized)
            - random : Iterate randomly (with replacement)
    
        Attributes
        ----------
        index : np.ndarray
            Index array for fast shuffling.
    
        index_data_ptr : int
            Pointer to the index array.
    
        current_index : int
            Index of current sample in ``index``.
            The index of current sample in the data is given by
            index_data_ptr[current_index].
    
        n_samples : Py_ssize_t
            Number of samples in the dataset.
    
        seed : np.uint32_t
            Seed used for random sampling.
    """
    def _next_py(self, *args, **kwargs): # real signature unknown
        """ python function used for easy testing """
        pass

    def _random_py(self, *args, **kwargs): # real signature unknown
        """ python function used for easy testing """
        pass

    def _sample_py(self, *args, **kwargs): # real signature unknown
        """ python function used for easy testing """
        pass

    def _shuffle_py(self, *args, **kwargs): # real signature unknown
        """ python function used for easy testing """
        pass

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


class ArrayDataset64(SequentialDataset64):
    """
    Dataset backed by a two-dimensional numpy array.
    
        The dtype of the numpy array is expected to be ``np.float64`` (double)
        and C-style memory layout.
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f260e159870>'


class CSRDataset32(SequentialDataset32):
    """ A ``SequentialDataset`` backed by a scipy sparse CSR matrix. """
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f25f5b314e0>'


class CSRDataset64(SequentialDataset64):
    """ A ``SequentialDataset`` backed by a scipy sparse CSR matrix. """
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

    __pyx_vtable__ = None # (!) real value is '<capsule object NULL at 0x7f260d1e0300>'


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f260d1e4e10>'

__spec__ = None # (!) real value is "ModuleSpec(name='sklearn.utils._seq_dataset', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f260d1e4e10>, origin='/home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/utils/_seq_dataset.cpython-35m-x86_64-linux-gnu.so')"

__test__ = {}

