# encoding: utf-8
# module sklearn.svm._libsvm_sparse
# from /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/svm/_libsvm_sparse.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # /usr/lib/python3.5/warnings.py
import numpy as np # /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/numpy/__init__.py
import scipy.sparse as sparse # /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/scipy/sparse/__init__.py

# functions

def libsvm_sparse_decision_function(*args, **kwargs): # real signature unknown
    """
    Predict margin (libsvm name for this is predict_values)
    
        We have to reconstruct model and parameters to make sure we stay
        in sync with the python object.
    """
    pass

def libsvm_sparse_predict(*args, **kwargs): # real signature unknown
    """
    Predict values T given a model.
    
        For speed, all real work is done at the C level in function
        copy_predict (libsvm_helper.c).
    
        We have to reconstruct model and parameters to make sure we stay
        in sync with the python object.
    
        See sklearn.svm.predict for a complete list of parameters.
    
        Parameters
        ----------
        X : array-like, dtype=float
        Y : array
            target vector
    
        Returns
        -------
        dec_values : array
            predicted values.
    """
    pass

def libsvm_sparse_predict_proba(*args, **kwargs): # real signature unknown
    """ Predict values T given a model. """
    pass

def libsvm_sparse_train(*args, **kwargs): # real signature unknown
    """
    Wrap svm_train from libsvm using a scipy.sparse.csr matrix
    
        Work in progress.
    
        Parameters
        ----------
        n_features : number of features.
            XXX: can we retrieve this from any other parameter ?
    
        X : array-like, dtype=float, size=[N, D]
    
        Y : array, dtype=float, size=[N]
            target vector
    
        ...
    
        Notes
        -------------------
        See sklearn.svm.predict for a complete list of parameters.
    """
    pass

def set_verbosity_wrap(*args, **kwargs): # real signature unknown
    """ Control verbosity of libsvm library """
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

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25f5b62358>'

__spec__ = None # (!) real value is "ModuleSpec(name='sklearn.svm._libsvm_sparse', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25f5b62358>, origin='/home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/svm/_libsvm_sparse.cpython-35m-x86_64-linux-gnu.so')"

__test__ = {}

