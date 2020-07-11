# encoding: utf-8
# module scipy.linalg.cython_blas
# from /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/scipy/linalg/cython_blas.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
"""
BLAS Functions for Cython
=========================

Usable from Cython via::

    cimport scipy.linalg.cython_blas

These wrappers do not check for alignment of arrays.
Alignment should be checked before these wrappers are used.

Raw function pointers (Fortran-style pointer arguments):

- caxpy
- ccopy
- cdotc
- cdotu
- cgbmv
- cgemm
- cgemv
- cgerc
- cgeru
- chbmv
- chemm
- chemv
- cher
- cher2
- cher2k
- cherk
- chpmv
- chpr
- chpr2
- crotg
- cscal
- csrot
- csscal
- cswap
- csymm
- csyr2k
- csyrk
- ctbmv
- ctbsv
- ctpmv
- ctpsv
- ctrmm
- ctrmv
- ctrsm
- ctrsv
- dasum
- daxpy
- dcabs1
- dcopy
- ddot
- dgbmv
- dgemm
- dgemv
- dger
- dnrm2
- drot
- drotg
- drotm
- drotmg
- dsbmv
- dscal
- dsdot
- dspmv
- dspr
- dspr2
- dswap
- dsymm
- dsymv
- dsyr
- dsyr2
- dsyr2k
- dsyrk
- dtbmv
- dtbsv
- dtpmv
- dtpsv
- dtrmm
- dtrmv
- dtrsm
- dtrsv
- dzasum
- dznrm2
- icamax
- idamax
- isamax
- izamax
- lsame
- sasum
- saxpy
- scasum
- scnrm2
- scopy
- sdot
- sdsdot
- sgbmv
- sgemm
- sgemv
- sger
- snrm2
- srot
- srotg
- srotm
- srotmg
- ssbmv
- sscal
- sspmv
- sspr
- sspr2
- sswap
- ssymm
- ssymv
- ssyr
- ssyr2
- ssyr2k
- ssyrk
- stbmv
- stbsv
- stpmv
- stpsv
- strmm
- strmv
- strsm
- strsv
- zaxpy
- zcopy
- zdotc
- zdotu
- zdrot
- zdscal
- zgbmv
- zgemm
- zgemv
- zgerc
- zgeru
- zhbmv
- zhemm
- zhemv
- zher
- zher2
- zher2k
- zherk
- zhpmv
- zhpr
- zhpr2
- zrotg
- zscal
- zswap
- zsymm
- zsyr2k
- zsyrk
- ztbmv
- ztbsv
- ztpmv
- ztpsv
- ztrmm
- ztrmv
- ztrsm
- ztrsv
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>

# functions

def _test_cdotc(*args, **kwargs): # real signature unknown
    pass

def _test_cdotu(*args, **kwargs): # real signature unknown
    pass

def _test_dasum(*args, **kwargs): # real signature unknown
    pass

def _test_ddot(*args, **kwargs): # real signature unknown
    pass

def _test_dgemm(*args, **kwargs): # real signature unknown
    pass

def _test_dnrm2(*args, **kwargs): # real signature unknown
    pass

def _test_dzasum(*args, **kwargs): # real signature unknown
    pass

def _test_dznrm2(*args, **kwargs): # real signature unknown
    pass

def _test_icamax(*args, **kwargs): # real signature unknown
    pass

def _test_idamax(*args, **kwargs): # real signature unknown
    pass

def _test_isamax(*args, **kwargs): # real signature unknown
    pass

def _test_izamax(*args, **kwargs): # real signature unknown
    pass

def _test_sasum(*args, **kwargs): # real signature unknown
    pass

def _test_scasum(*args, **kwargs): # real signature unknown
    pass

def _test_scnrm2(*args, **kwargs): # real signature unknown
    pass

def _test_sdot(*args, **kwargs): # real signature unknown
    pass

def _test_snrm2(*args, **kwargs): # real signature unknown
    pass

def _test_zdotc(*args, **kwargs): # real signature unknown
    pass

def _test_zdotu(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f2600296438>'

__pyx_capi__ = {
    'caxpy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f260074fd20>'
    'ccopy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f260074fd50>'
    'cdotc': None, # (!) real value is '<capsule object "__pyx_t_float_complex (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f260074fd80>'
    'cdotu': None, # (!) real value is '<capsule object "__pyx_t_float_complex (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f260074fdb0>'
    'cgbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f260074fde0>'
    'cgemm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f260074fe10>'
    'cgemv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f260074fe40>'
    'cgerc': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f260074fe70>'
    'cgeru': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f260074fea0>'
    'chbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f260074fed0>'
    'chemm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f260074ff00>'
    'chemv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f260074ff30>'
    'cher': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f260074ff60>'
    'cher2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f260074ff90>'
    'cher2k': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_float_complex *, int *)" at 0x7f260074ffc0>'
    'cherk': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_float_complex *, int *)" at 0x7f260029a030>'
    'chpmv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f260029a060>'
    'chpr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0x7f260029a090>'
    'chpr2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *)" at 0x7f260029a0c0>'
    'crotg': None, # (!) real value is '<capsule object "void (__pyx_t_float_complex *, __pyx_t_float_complex *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_float_complex *)" at 0x7f260029a0f0>'
    'cscal': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f260029a120>'
    'csrot': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *)" at 0x7f260029a150>'
    'csscal': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_float_complex *, int *)" at 0x7f260029a180>'
    'cswap': None, # (!) real value is '<capsule object "void (int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f260029a1b0>'
    'csymm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f260029a1e0>'
    'csyr2k': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f260029a210>'
    'csyrk': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f260029a240>'
    'ctbmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f260029a270>'
    'ctbsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f260029a2a0>'
    'ctpmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f260029a2d0>'
    'ctpsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *)" at 0x7f260029a300>'
    'ctrmm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f260029a330>'
    'ctrmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f260029a360>'
    'ctrsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_float_complex *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f260029a390>'
    'ctrsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_float_complex *, int *, __pyx_t_float_complex *, int *)" at 0x7f260029a3c0>'
    'dasum': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_d (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a3f0>'
    'daxpy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a420>'
    'dcabs1': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_d (__pyx_t_double_complex *)" at 0x7f260029a450>'
    'dcopy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a480>'
    'ddot': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_d (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a4b0>'
    'dgbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a4e0>'
    'dgemm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a510>'
    'dgemv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a540>'
    'dger': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a570>'
    'dnrm2': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_d (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a5a0>'
    'drot': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *)" at 0x7f260029a5d0>'
    'drotg': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *)" at 0x7f260029a600>'
    'drotm': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *)" at 0x7f260029a630>'
    'drotmg': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *)" at 0x7f260029a660>'
    'dsbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a690>'
    'dscal': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a6c0>'
    'dsdot': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_d (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029a6f0>'
    'dspmv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a720>'
    'dspr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *)" at 0x7f260029a750>'
    'dspr2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *)" at 0x7f260029a780>'
    'dswap': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a7b0>'
    'dsymm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a7e0>'
    'dsymv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a810>'
    'dsyr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a840>'
    'dsyr2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a870>'
    'dsyr2k': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a8a0>'
    'dsyrk': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a8d0>'
    'dtbmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a900>'
    'dtbsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a930>'
    'dtpmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a960>'
    'dtpsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a990>'
    'dtrmm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a9c0>'
    'dtrmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029a9f0>'
    'dtrsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029aa20>'
    'dtrsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029aa50>'
    'dzasum': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_d (int *, __pyx_t_double_complex *, int *)" at 0x7f260029aa80>'
    'dznrm2': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_d (int *, __pyx_t_double_complex *, int *)" at 0x7f260029aab0>'
    'icamax': None, # (!) real value is '<capsule object "int (int *, __pyx_t_float_complex *, int *)" at 0x7f260029aae0>'
    'idamax': None, # (!) real value is '<capsule object "int (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, int *)" at 0x7f260029ab10>'
    'isamax': None, # (!) real value is '<capsule object "int (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029ab40>'
    'izamax': None, # (!) real value is '<capsule object "int (int *, __pyx_t_double_complex *, int *)" at 0x7f260029ab70>'
    'lsame': None, # (!) real value is '<capsule object "int (char *, char *)" at 0x7f260029aba0>'
    'sasum': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_s (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029abd0>'
    'saxpy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029ac00>'
    'scasum': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_s (int *, __pyx_t_float_complex *, int *)" at 0x7f260029ac30>'
    'scnrm2': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_s (int *, __pyx_t_float_complex *, int *)" at 0x7f260029ac60>'
    'scopy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029ac90>'
    'sdot': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_s (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029acc0>'
    'sdsdot': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_s (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029acf0>'
    'sgbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029ad20>'
    'sgemm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029ad50>'
    'sgemv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029ad80>'
    'sger': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029adb0>'
    'snrm2': None, # (!) real value is '<capsule object "__pyx_t_5scipy_6linalg_11cython_blas_s (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029ade0>'
    'srot': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *)" at 0x7f260029ae10>'
    'srotg': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *)" at 0x7f260029ae40>'
    'srotm': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *)" at 0x7f260029ae70>'
    'srotmg': None, # (!) real value is '<capsule object "void (__pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *)" at 0x7f260029aea0>'
    'ssbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029aed0>'
    'sscal': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029af00>'
    'sspmv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029af30>'
    'sspr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *)" at 0x7f260029af60>'
    'sspr2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *)" at 0x7f260029af90>'
    'sswap': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029afc0>'
    'ssymm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029b030>'
    'ssymv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029b060>'
    'ssyr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029b090>'
    'ssyr2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029b0c0>'
    'ssyr2k': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029b0f0>'
    'ssyrk': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029b120>'
    'stbmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029b150>'
    'stbsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029b180>'
    'stpmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029b1b0>'
    'stpsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029b1e0>'
    'strmm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029b210>'
    'strmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029b240>'
    'strsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029b270>'
    'strsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *, __pyx_t_5scipy_6linalg_11cython_blas_s *, int *)" at 0x7f260029b2a0>'
    'zaxpy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f260029b2d0>'
    'zcopy': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f260029b300>'
    'zdotc': None, # (!) real value is '<capsule object "__pyx_t_double_complex (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f260029b330>'
    'zdotu': None, # (!) real value is '<capsule object "__pyx_t_double_complex (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f260029b360>'
    'zdrot': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_5scipy_6linalg_11cython_blas_d *)" at 0x7f260029b390>'
    'zdscal': None, # (!) real value is '<capsule object "void (int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_double_complex *, int *)" at 0x7f260029b3c0>'
    'zgbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f260029b3f0>'
    'zgemm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f260029b420>'
    'zgemv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f260029b450>'
    'zgerc': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f260029b480>'
    'zgeru': None, # (!) real value is '<capsule object "void (int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f260029b4b0>'
    'zhbmv': None, # (!) real value is '<capsule object "void (char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f260029b4e0>'
    'zhemm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f260029b510>'
    'zhemv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f260029b540>'
    'zher': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f260029b570>'
    'zher2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f260029b5a0>'
    'zher2k': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_double_complex *, int *)" at 0x7f260029b5d0>'
    'zherk': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_double_complex *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_double_complex *, int *)" at 0x7f260029b600>'
    'zhpmv': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f260029b630>'
    'zhpr': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0x7f260029b660>'
    'zhpr2': None, # (!) real value is '<capsule object "void (char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *)" at 0x7f260029b690>'
    'zrotg': None, # (!) real value is '<capsule object "void (__pyx_t_double_complex *, __pyx_t_double_complex *, __pyx_t_5scipy_6linalg_11cython_blas_d *, __pyx_t_double_complex *)" at 0x7f260029b6c0>'
    'zscal': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f260029b6f0>'
    'zswap': None, # (!) real value is '<capsule object "void (int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f260029b720>'
    'zsymm': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f260029b750>'
    'zsyr2k': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f260029b780>'
    'zsyrk': None, # (!) real value is '<capsule object "void (char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f260029b7b0>'
    'ztbmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f260029b7e0>'
    'ztbsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f260029b810>'
    'ztpmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f260029b840>'
    'ztpsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *)" at 0x7f260029b870>'
    'ztrmm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f260029b8a0>'
    'ztrmv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f260029b8d0>'
    'ztrsm': None, # (!) real value is '<capsule object "void (char *, char *, char *, char *, int *, int *, __pyx_t_double_complex *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f260029b900>'
    'ztrsv': None, # (!) real value is '<capsule object "void (char *, char *, char *, int *, __pyx_t_double_complex *, int *, __pyx_t_double_complex *, int *)" at 0x7f260029b930>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.linalg.cython_blas', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f2600296438>, origin='/home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/scipy/linalg/cython_blas.cpython-35m-x86_64-linux-gnu.so')"

__test__ = {}

