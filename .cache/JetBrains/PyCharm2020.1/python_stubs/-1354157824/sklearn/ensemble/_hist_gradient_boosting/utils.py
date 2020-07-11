# encoding: utf-8
# module sklearn.ensemble._hist_gradient_boosting.utils
# from /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/ensemble/_hist_gradient_boosting/utils.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
""" This module contains utility routines. """

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import sklearn.base as __sklearn_base


# functions

def get_equivalent_estimator(*args, **kwargs): # real signature unknown
    """
    Return an unfitted estimator from another lib with matching hyperparams.
    
        This utility function takes care of renaming the sklearn parameters into
        their LightGBM, XGBoost or CatBoost equivalent parameters.
    
        # unmapped XGB parameters:
        # - min_samples_leaf
        # - min_data_in_bin
        # - min_split_gain (there is min_split_loss though?)
    
        # unmapped Catboost parameters:
        # max_leaves
        # min_*
    """
    pass

def is_classifier(estimator): # reliably restored by inspect
    """
    Return True if the given estimator is (probably) a classifier.
    
        Parameters
        ----------
        estimator : object
            Estimator object to test.
    
        Returns
        -------
        out : bool
            True if estimator is a classifier and False otherwise.
    """
    pass

def sum_parallel(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class _BinMapper(__sklearn_base.TransformerMixin, __sklearn_base.BaseEstimator):
    """
    Transformer that maps a dataset into integer-valued bins.
    
        The bins are created in a feature-wise fashion, using quantiles so that
        each bins contains approximately the same number of samples.
    
        For large datasets, quantiles are computed on a subset of the data to
        speed-up the binning, but the quantiles should remain stable.
    
        Features with a small number of values may be binned into less than
        ``n_bins`` bins. The last bin (at index ``n_bins - 1``) is always reserved
        for missing values.
    
        Parameters
        ----------
        n_bins : int, optional (default=256)
            The maximum number of bins to use (including the bin for missing
            values). Non-missing values are binned on ``max_bins = n_bins - 1``
            bins. The last bin is always reserved for missing values. If for a
            given feature the number of unique values is less than ``max_bins``,
            then those unique values will be used to compute the bin thresholds,
            instead of the quantiles.
        subsample : int or None, optional (default=2e5)
            If ``n_samples > subsample``, then ``sub_samples`` samples will be
            randomly chosen to compute the quantiles. If ``None``, the whole data
            is used.
        random_state: int or numpy.random.RandomState or None,         optional (default=None)
            Pseudo-random number generator to control the random sub-sampling.
            See :term:`random_state`.
    
        Attributes
        ----------
        bin_thresholds_ : list of arrays
            For each feature, gives the real-valued bin threhsolds. There are
            ``max_bins - 1`` thresholds, where ``max_bins = n_bins - 1`` is the
            number of bins used for non-missing values.
        n_bins_non_missing_ : array of uint32
            For each feature, gives the number of bins actually used for
            non-missing values. For features with a lot of unique values, this is
            equal to ``n_bins - 1``.
        missing_values_bin_idx_ : uint8
            The index of the bin where missing values are mapped. This is a
            constant across all features. This corresponds to the last bin, and
            it is always equal to ``n_bins - 1``. Note that if ``n_bins_missing_``
            is less than ``n_bins - 1`` for a given feature, then there are
            empty (and unused) bins.
    """
    def fit(self, X, y=None): # reliably restored by inspect
        """
        Fit data X by computing the binning thresholds.
        
                The last bin is reserved for missing values, whether missing values
                are present in the data or not.
        
                Parameters
                ----------
                X : array-like, shape (n_samples, n_features)
                    The data to bin.
                y: None
                    Ignored.
        
                Returns
                -------
                self : object
        """
        pass

    def transform(self, X): # reliably restored by inspect
        """
        Bin data X.
        
                Missing values will be mapped to the last bin.
        
                Parameters
                ----------
                X : array-like, shape (n_samples, n_features)
                    The data to bin.
        
                Returns
                -------
                X_binned : array-like, shape (n_samples, n_features)
                    The binned data (fortran-aligned).
        """
        pass

    def __init__(self, n_bins=256, subsample=200000, random_state=None): # reliably restored by inspect
        # no doc
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25f1796b00>'

__spec__ = None # (!) real value is "ModuleSpec(name='sklearn.ensemble._hist_gradient_boosting.utils', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25f1796b00>, origin='/home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/ensemble/_hist_gradient_boosting/utils.cpython-35m-x86_64-linux-gnu.so')"

__test__ = {}

