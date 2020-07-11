# encoding: utf-8
# module sklearn.linear_model._cd_fast
# from /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/linear_model/_cd_fast.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # /usr/lib/python3.5/warnings.py
import numpy as np # /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/numpy/__init__.py
import numpy.linalg as linalg # /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/numpy/linalg/__init__.py

# functions

def enet_coordinate_descent(*args, **kwargs): # real signature unknown
    """
    Cython version of the coordinate descent algorithm
            for Elastic-Net regression
    
            We minimize
    
            (1/2) * norm(y - X w, 2)^2 + alpha norm(w, 1) + (beta/2) norm(w, 2)^2
    """
    pass

def enet_coordinate_descent_gram(*args, **kwargs): # real signature unknown
    """
    Cython version of the coordinate descent algorithm
            for Elastic-Net regression
    
            We minimize
    
            (1/2) * w^T Q w - q^T w + alpha norm(w, 1) + (beta/2) * norm(w, 2)^2
    
            which amount to the Elastic-Net problem when:
            Q = X^T X (Gram matrix)
            q = X^T y
    """
    pass

def enet_coordinate_descent_multi_task(*args, **kwargs): # real signature unknown
    """
    Cython version of the coordinate descent algorithm
            for Elastic-Net mult-task regression
    
            We minimize
    
            (1/2) * norm(y - X w, 2)^2 + l1_reg ||w||_21 + (1/2) * l2_reg norm(w, 2)^2
    """
    pass

def sparse_enet_coordinate_descent(*args, **kwargs): # real signature unknown
    """
    Cython version of the coordinate descent algorithm for Elastic-Net
    
        We minimize:
    
            (1/2) * norm(y - X w, 2)^2 + alpha norm(w, 1) + (beta/2) * norm(w, 2)^2
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class ConvergenceWarning(UserWarning):
    """
    Custom warning to capture convergence problems
    
        Examples
        --------
    
        >>> import numpy as np
        >>> import warnings
        >>> from sklearn.cluster import KMeans
        >>> from sklearn.exceptions import ConvergenceWarning
        >>> warnings.simplefilter("always", ConvergenceWarning)
        >>> X = np.asarray([[0, 0],
        ...                 [0, 1],
        ...                 [1, 0],
        ...                 [1, 0]])  # last point is duplicated
        >>> with warnings.catch_warnings(record=True) as w:
        ...     km = KMeans(n_clusters=4).fit(X)
        ...     print(w[-1].message)
        Number of distinct clusters (3) found smaller than n_clusters (4).
        Possibly due to duplicate points in X.
    
        .. versionchanged:: 0.18
           Moved from sklearn.utils.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25f4433b70>'

__spec__ = None # (!) real value is "ModuleSpec(name='sklearn.linear_model._cd_fast', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25f4433b70>, origin='/home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/linear_model/_cd_fast.cpython-35m-x86_64-linux-gnu.so')"

__test__ = {}

