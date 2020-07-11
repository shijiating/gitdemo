# encoding: utf-8
# module sklearn.metrics.cluster._expected_mutual_info_fast
# from /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/metrics/cluster/_expected_mutual_info_fast.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/numpy/__init__.py

# functions

def expected_mutual_information(*args, **kwargs): # real signature unknown
    """ Calculate the expected mutual information for two labelings. """
    pass

def gammaln(x, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    gammaln(x, /, out=None, *, where=True, casting='same_kind', order='K', dtype=None, subok=True[, signature, extobj])
    
    gammaln(x, out=None)
    
    Logarithm of the absolute value of the Gamma function.
    
    Defined as
    
    .. math::
    
       \ln(\lvert\Gamma(x)\rvert)
    
    where :math:`\Gamma` is the Gamma function. For more details on
    the Gamma function, see [dlmf]_.
    
    Parameters
    ----------
    x : array_like
        Real argument
    out : ndarray, optional
        Optional output array for the function results
    
    Returns
    -------
    scalar or ndarray
        Values of the log of the absolute value of Gamma
    
    See Also
    --------
    gammasgn : sign of the gamma function
    loggamma : principal branch of the logarithm of the gamma function
    
    Notes
    -----
    It is the same function as the Python standard library function
    :func:`math.lgamma`.
    
    When used in conjunction with `gammasgn`, this function is useful
    for working in logspace on the real axis without having to deal
    with complex numbers via the relation ``exp(gammaln(x)) =
    gammasgn(x) * gamma(x)``.
    
    For complex-valued log-gamma, use `loggamma` instead of `gammaln`.
    
    References
    ----------
    .. [dlmf] NIST Digital Library of Mathematical Functions
              https://dlmf.nist.gov/5
    
    Examples
    --------
    >>> import scipy.special as sc
    
    It has two positive zeros.
    
    >>> sc.gammaln([1, 2])
    array([0., 0.])
    
    It has poles at nonpositive integers.
    
    >>> sc.gammaln([0, -1, -2, -3, -4])
    array([inf, inf, inf, inf, inf])
    
    It asymptotically approaches ``x * log(x)`` (Stirling's formula).
    
    >>> x = np.array([1e10, 1e20, 1e40, 1e80])
    >>> sc.gammaln(x)
    array([2.20258509e+11, 4.50517019e+21, 9.11034037e+41, 1.83206807e+82])
    >>> x * np.log(x)
    array([2.30258509e+11, 4.60517019e+21, 9.21034037e+41, 1.84206807e+82])
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25f51a5128>'

__spec__ = None # (!) real value is "ModuleSpec(name='sklearn.metrics.cluster._expected_mutual_info_fast', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25f51a5128>, origin='/home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/metrics/cluster/_expected_mutual_info_fast.cpython-35m-x86_64-linux-gnu.so')"

__test__ = {}

