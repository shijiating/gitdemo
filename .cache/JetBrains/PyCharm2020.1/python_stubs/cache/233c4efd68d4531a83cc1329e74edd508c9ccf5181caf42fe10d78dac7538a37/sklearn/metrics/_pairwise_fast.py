# encoding: utf-8
# module sklearn.metrics._pairwise_fast
# from /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/metrics/_pairwise_fast.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/numpy/__init__.py
from sklearn.utils._openmp_helpers import _openmp_effective_n_threads


# functions

def _chi2_kernel_fast(*args, **kwargs): # real signature unknown
    pass

def _sparse_manhattan(X_data, X_indices, X_indptr, *more, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Pairwise L1 distances for CSR matrices.
    
        Usage:
        >>> D = np.zeros(X.shape[0], Y.shape[0])
        >>> _sparse_manhattan(X.data, X.indices, X.indptr,
        ...                   Y.data, Y.indices, Y.indptr,
        ...                   D)
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25f51b0588>'

__spec__ = None # (!) real value is "ModuleSpec(name='sklearn.metrics._pairwise_fast', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25f51b0588>, origin='/home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/metrics/_pairwise_fast.cpython-35m-x86_64-linux-gnu.so')"

__test__ = {
    '_sparse_manhattan (line 43)': 'Pairwise L1 distances for CSR matrices.\n\n    Usage:\n    >>> D = np.zeros(X.shape[0], Y.shape[0])\n    >>> _sparse_manhattan(X.data, X.indices, X.indptr,\n    ...                   Y.data, Y.indices, Y.indptr,\n    ...                   D)\n    ',
}

