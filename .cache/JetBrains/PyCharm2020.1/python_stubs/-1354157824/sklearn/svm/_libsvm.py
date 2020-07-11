# encoding: utf-8
# module sklearn.svm._libsvm
# from /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/svm/_libsvm.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
"""
Binding for libsvm_skl
----------------------

These are the bindings for libsvm_skl, which is a fork of libsvm[1]
that adds to libsvm some capabilities, like index of support vectors
and efficient representation of dense matrices.

These are low-level routines, but can be used for flexibility or
performance reasons. See sklearn.svm for a higher-level API.

Low-level memory management is done in libsvm_helper.c. If we happen
to run out of memory a MemoryError will be raised. In practice this is
not very helpful since high chances are malloc fails inside svm.cpp,
where no sort of memory checks are done.

[1] https://www.csie.ntu.edu.tw/~cjlin/libsvm/

Notes
-----
Maybe we could speed it a bit further by decorating functions with
@cython.boundscheck(False), but probably it is not worth since all
work is done in lisvm_helper.c
Also, the signature mode='c' is somewhat superficial, since we already
check that arrays are C-contiguous in svm.py

Authors
-------
2010: Fabian Pedregosa <fabian.pedregosa@inria.fr>
      Gael Varoquaux <gael.varoquaux@normalesup.org>
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import warnings as warnings # /usr/lib/python3.5/warnings.py
import numpy as np # /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/numpy/__init__.py

# functions

def cross_validation(*args, **kwargs): # real signature unknown
    """
    Binding of the cross-validation routine (low-level routine)
    
        Parameters
        ----------
    
        X : array-like, dtype=float of shape (n_samples, n_features)
    
        Y : array, dtype=float of shape (n_samples,)
            target vector
    
        n_fold : int32
            Number of folds for cross validation.
    
        svm_type : {0, 1, 2, 3, 4}, default=0
            Type of SVM: C_SVC, NuSVC, OneClassSVM, EpsilonSVR or NuSVR
            respectively.
    
        kernel : {'linear', 'rbf', 'poly', 'sigmoid', 'precomputed'}, default='rbf'
            Kernel to use in the model: linear, polynomial, RBF, sigmoid
            or precomputed.
    
        degree : int32, default=3
            Degree of the polynomial kernel (only relevant if kernel is
            set to polynomial).
    
        gamma : float64, default=0.1
            Gamma parameter in rbf, poly and sigmoid kernels. Ignored by other
            kernels.
    
        coef0 : float64, default=0.0
            Independent parameter in poly/sigmoid kernel.
    
        tol : float64, default=1e-3
            Numeric stopping criterion (WRITEME).
    
        C : float64, default=1
            C parameter in C-Support Vector Classification.
    
        nu : float64, default=0.5
            An upper bound on the fraction of training errors and a lower bound of
            the fraction of support vectors. Should be in the interval (0, 1].
    
        epsilon : double, default=0.1
            Epsilon parameter in the epsilon-insensitive loss function.
    
        class_weight : array, dtype=float64, shape (n_classes,),             default=np.empty(0)
            Set the parameter C of class i to class_weight[i]*C for
            SVC. If not given, all classes are supposed to have
            weight one.
    
        sample_weight : array, dtype=float64, shape (n_samples,),             default=np.empty(0)
            Weights assigned to each sample.
    
        shrinking : int, default=1
            Whether to use the shrinking heuristic.
    
        probability : int, default=0
            Whether to enable probability estimates.
    
        cache_size : float64, default=100
            Cache size for gram matrix columns (in megabytes).
    
        max_iter : int (-1 for no limit), default=-1
            Stop solver after this many iterations regardless of accuracy
            (XXX Currently there is no API to know whether this kicked in.)
    
        random_seed : int, default=0
            Seed for the random number generator used for probability estimates.
    
        Returns
        -------
        target : array, float
    """
    pass

def decision_function(*args, **kwargs): # real signature unknown
    """
    Predict margin (libsvm name for this is predict_values)
    
        We have to reconstruct model and parameters to make sure we stay
        in sync with the python object.
    
        Parameters
        ----------
        X : array-like, dtype=float, size=[n_samples, n_features]
    
        support : array, shape=[n_support]
            Index of support vectors in training set.
    
        SV : array, shape=[n_support, n_features]
            Support vectors.
    
        nSV : array, shape=[n_class]
            Number of support vectors in each class.
    
        sv_coef : array, shape=[n_class-1, n_support]
            Coefficients of support vectors in decision function.
    
        intercept : array, shape=[n_class*(n_class-1)/2]
            Intercept in decision function.
    
        probA, probB : array, shape=[n_class*(n_class-1)/2]
            Probability estimates.
    
        svm_type : {0, 1, 2, 3, 4}, optional
            Type of SVM: C_SVC, NuSVC, OneClassSVM, EpsilonSVR or NuSVR
            respectively. 0 by default.
    
        kernel : {'linear', 'rbf', 'poly', 'sigmoid', 'precomputed'}, optional
            Kernel to use in the model: linear, polynomial, RBF, sigmoid
            or precomputed. 'rbf' by default.
    
        degree : int32, optional
            Degree of the polynomial kernel (only relevant if kernel is
            set to polynomial), 3 by default.
    
        gamma : float64, optional
            Gamma parameter in rbf, poly and sigmoid kernels. Ignored by other
            kernels. 0.1 by default.
    
        coef0 : float64, optional
            Independent parameter in poly/sigmoid kernel. 0 by default.
    
        Returns
        -------
        dec_values : array
            Predicted values.
    """
    pass

def fit(*args, **kwargs): # real signature unknown
    """
    Train the model using libsvm (low-level method)
    
        Parameters
        ----------
        X : array-like, dtype=float64 of shape (n_samples, n_features)
    
        Y : array, dtype=float64 of shape (n_samples,)
            target vector
    
        svm_type : {0, 1, 2, 3, 4}, default=0
            Type of SVM: C_SVC, NuSVC, OneClassSVM, EpsilonSVR or NuSVR
            respectively.
    
        kernel : {'linear', 'rbf', 'poly', 'sigmoid', 'precomputed'}, default="rbf"
            Kernel to use in the model: linear, polynomial, RBF, sigmoid
            or precomputed.
    
        degree : int32, default=3
            Degree of the polynomial kernel (only relevant if kernel is
            set to polynomial).
    
        gamma : float64, default=0.1
            Gamma parameter in rbf, poly and sigmoid kernels. Ignored by other
            kernels.
    
        coef0 : float64, default=0
            Independent parameter in poly/sigmoid kernel.
    
        tol : float64, default=1e-3
            Numeric stopping criterion (WRITEME).
    
        C : float64, default=1
            C parameter in C-Support Vector Classification.
    
        nu : float64, default=0.5
            An upper bound on the fraction of training errors and a lower bound of
            the fraction of support vectors. Should be in the interval (0, 1].
    
        epsilon : double, default=0.1
            Epsilon parameter in the epsilon-insensitive loss function.
    
        class_weight : array, dtype=float64, shape (n_classes,),             default=np.empty(0)
            Set the parameter C of class i to class_weight[i]*C for
            SVC. If not given, all classes are supposed to have
            weight one.
    
        sample_weight : array, dtype=float64, shape (n_samples,),             default=np.empty(0)
            Weights assigned to each sample.
    
        shrinking : int, default=1
            Whether to use the shrinking heuristic.
    
        probability : int, default=0
            Whether to enable probability estimates.
    
        cache_size : float64, default=100
            Cache size for gram matrix columns (in megabytes).
    
        max_iter : int (-1 for no limit), default=-1
            Stop solver after this many iterations regardless of accuracy
            (XXX Currently there is no API to know whether this kicked in.)
    
        random_seed : int, default=0
            Seed for the random number generator used for probability estimates.
    
        Returns
        -------
        support : array of shape (n_support,)
            Index of support vectors.
    
        support_vectors : array of shape (n_support, n_features)
            Support vectors (equivalent to X[support]). Will return an
            empty array in the case of precomputed kernel.
    
        n_class_SV : array of shape (n_class,)
            Number of support vectors in each class.
    
        sv_coef : array of shape (n_class-1, n_support)
            Coefficients of support vectors in decision function.
    
        intercept : array of shape (n_class*(n_class-1)/2,)
            Intercept in decision function.
    
        probA, probB : array of shape (n_class*(n_class-1)/2,)
            Probability estimates, empty array for probability=False.
    """
    pass

def predict(*args, **kwargs): # real signature unknown
    """
    Predict target values of X given a model (low-level method)
    
        Parameters
        ----------
        X : array-like, dtype=float of shape (n_samples, n_features)
    
        support : array of shape (n_support,)
            Index of support vectors in training set.
    
        SV : array of shape (n_support, n_features)
            Support vectors.
    
        nSV : array of shape (n_class,)
            Number of support vectors in each class.
    
        sv_coef : array of shape (n_class-1, n_support)
            Coefficients of support vectors in decision function.
    
        intercept : array of shape (n_class*(n_class-1)/2)
            Intercept in decision function.
    
        probA, probB : array of shape (n_class*(n_class-1)/2,)
            Probability estimates.
    
        svm_type : {0, 1, 2, 3, 4}, default=0
            Type of SVM: C_SVC, NuSVC, OneClassSVM, EpsilonSVR or NuSVR
            respectively.
    
        kernel : {'linear', 'rbf', 'poly', 'sigmoid', 'precomputed'}, default="rbf"
            Kernel to use in the model: linear, polynomial, RBF, sigmoid
            or precomputed.
    
        degree : int32, default=3
            Degree of the polynomial kernel (only relevant if kernel is
            set to polynomial).
    
        gamma : float64, default=0.1
            Gamma parameter in rbf, poly and sigmoid kernels. Ignored by other
            kernels.
    
        coef0 : float64, default=0.0
            Independent parameter in poly/sigmoid kernel.
    
        Returns
        -------
        dec_values : array
            Predicted values.
    """
    pass

def predict_proba(*args, **kwargs): # real signature unknown
    """
    Predict probabilities
    
        svm_model stores all parameters needed to predict a given value.
    
        For speed, all real work is done at the C level in function
        copy_predict (libsvm_helper.c).
    
        We have to reconstruct model and parameters to make sure we stay
        in sync with the python object.
    
        See sklearn.svm.predict for a complete list of parameters.
    
        Parameters
        ----------
        X : array-like, dtype=float of shape (n_samples, n_features)
    
        support : array of shape (n_support,)
            Index of support vectors in training set.
    
        SV : array of shape (n_support, n_features)
            Support vectors.
    
        nSV : array of shape (n_class,)
            Number of support vectors in each class.
    
        sv_coef : array of shape (n_class-1, n_support)
            Coefficients of support vectors in decision function.
    
        intercept : array of shape (n_class*(n_class-1)/2,)
            Intercept in decision function.
    
        probA, probB : array of shape (n_class*(n_class-1)/2,)
            Probability estimates.
    
        svm_type : {0, 1, 2, 3, 4}, default=0
            Type of SVM: C_SVC, NuSVC, OneClassSVM, EpsilonSVR or NuSVR
            respectively.
    
        kernel : {'linear', 'rbf', 'poly', 'sigmoid', 'precomputed'}, default="rbf"
            Kernel to use in the model: linear, polynomial, RBF, sigmoid
            or precomputed.
    
        degree : int32, default=3
            Degree of the polynomial kernel (only relevant if kernel is
            set to polynomial).
    
        gamma : float64, default=0.1
            Gamma parameter in rbf, poly and sigmoid kernels. Ignored by other
            kernels.
    
        coef0 : float64, default=0.0
            Independent parameter in poly/sigmoid kernel.
    
        Returns
        -------
        dec_values : array
            Predicted values.
    """
    pass

def set_verbosity_wrap(*args, **kwargs): # real signature unknown
    """ Control verbosity of libsvm library """
    pass

# no classes
# variables with complex values

LIBSVM_KERNEL_TYPES = [
    'linear',
    'poly',
    'rbf',
    'sigmoid',
    'precomputed',
]

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25f5b5aac8>'

__spec__ = None # (!) real value is "ModuleSpec(name='sklearn.svm._libsvm', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25f5b5aac8>, origin='/home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/svm/_libsvm.cpython-35m-x86_64-linux-gnu.so')"

__test__ = {}

