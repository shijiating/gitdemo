# encoding: utf-8
# module sklearn.manifold._utils
# from /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/manifold/_utils.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/numpy/__init__.py

# functions

def _binary_search_perplexity(*args, **kwargs): # real signature unknown
    """
    Binary search for sigmas of conditional Gaussians.
    
        This approximation reduces the computational complexity from O(N^2) to
        O(uN).
    
        Parameters
        ----------
        sqdistances : array-like, shape (n_samples, n_neighbors)
            Distances between training samples and their k nearest neighbors.
            When using the exact method, this is a square (n_samples, n_samples)
            distance matrix. The TSNE default metric is "euclidean" which is
            interpreted as squared euclidean distance.
    
        desired_perplexity : float
            Desired perplexity (2^entropy) of the conditional Gaussians.
    
        verbose : int
            Verbosity level.
    
        Returns
        -------
        P : array, shape (n_samples, n_samples)
            Probabilities of conditional Gaussian distributions p_i|j.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25f29f5390>'

__spec__ = None # (!) real value is "ModuleSpec(name='sklearn.manifold._utils', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25f29f5390>, origin='/home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/manifold/_utils.cpython-35m-x86_64-linux-gnu.so')"

__test__ = {}

