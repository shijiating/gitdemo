# encoding: utf-8
# module sklearn.decomposition._online_lda_fast
# from /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/decomposition/_online_lda_fast.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/numpy/__init__.py

# functions

def mean_change(*args, **kwargs): # real signature unknown
    """
    Calculate the mean difference between two arrays.
    
        Equivalent to np.abs(arr_1 - arr2).mean().
    """
    pass

def _dirichlet_expectation_1d(*args, **kwargs): # real signature unknown
    """
    Dirichlet expectation for a single sample:
            exp(E[log(theta)]) for theta ~ Dir(doc_topic)
        after adding doc_topic_prior to doc_topic, in-place.
    
        Equivalent to
            doc_topic += doc_topic_prior
            out[:] = np.exp(psi(doc_topic) - psi(np.sum(doc_topic)))
    """
    pass

def _dirichlet_expectation_2d(*args, **kwargs): # real signature unknown
    """
    Dirichlet expectation for multiple samples:
        E[log(theta)] for theta ~ Dir(arr).
    
        Equivalent to psi(arr) - psi(np.sum(arr, axis=1))[:, np.newaxis].
    
        Note that unlike _dirichlet_expectation_1d, this function doesn't compute
        the exp and doesn't add in the prior.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25f3138048>'

__spec__ = None # (!) real value is "ModuleSpec(name='sklearn.decomposition._online_lda_fast', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25f3138048>, origin='/home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/decomposition/_online_lda_fast.cpython-35m-x86_64-linux-gnu.so')"

__test__ = {}

