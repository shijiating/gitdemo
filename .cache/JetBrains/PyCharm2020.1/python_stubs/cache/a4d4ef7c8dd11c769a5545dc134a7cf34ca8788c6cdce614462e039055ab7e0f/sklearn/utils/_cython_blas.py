# encoding: utf-8
# module sklearn.utils._cython_blas
# from /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/utils/_cython_blas.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import enum as __enum


# Variables with simple values

ColMajor = 1

NoTrans = 110

RowMajor = 0

Trans = 116

# functions

def _asum_memview(*args, **kwargs): # real signature unknown
    pass

def _axpy_memview(*args, **kwargs): # real signature unknown
    pass

def _copy_memview(*args, **kwargs): # real signature unknown
    pass

def _dot_memview(*args, **kwargs): # real signature unknown
    pass

def _gemm_memview(*args, **kwargs): # real signature unknown
    pass

def _gemv_memview(*args, **kwargs): # real signature unknown
    pass

def _ger_memview(*args, **kwargs): # real signature unknown
    pass

def _nrm2_memview(*args, **kwargs): # real signature unknown
    pass

def _rotg_memview(*args, **kwargs): # real signature unknown
    pass

def _rot_memview(*args, **kwargs): # real signature unknown
    pass

def _scal_memview(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

def __pyx_unpickle___Pyx_EnumMeta(*args, **kwargs): # real signature unknown
    pass

# classes

class BLAS_Order(__enum.IntEnum):
    """ An enumeration. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    ColMajor = 1
    RowMajor = 0
    _member_map_ = {
        'ColMajor': 1,
        'RowMajor': 0,
    }
    _member_names_ = [
        'RowMajor',
        'ColMajor',
    ]
    _member_type_ = int
    _value2member_map_ = {
        0: 0,
        1: 1,
    }


class BLAS_Trans(__enum.IntEnum):
    """ An enumeration. """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(cls, value): # reliably restored by inspect
        # no doc
        pass

    NoTrans = 110
    Trans = 116
    _member_map_ = {
        'NoTrans': 110,
        'Trans': 116,
    }
    _member_names_ = [
        'NoTrans',
        'Trans',
    ]
    _member_type_ = int
    _value2member_map_ = {
        110: 110,
        116: 116,
    }


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f260d1e4e10>'

__pyx_capi__ = {
    '__pyx_fuse_0_asum': None, # (!) real value is '<capsule object "float (int, float *, int)" at 0x7f260d1e0300>'
    '__pyx_fuse_0_axpy': None, # (!) real value is '<capsule object "void (int, float, float *, int, float *, int)" at 0x7f25f5b314b0>'
    '__pyx_fuse_0_copy': None, # (!) real value is '<capsule object "void (int, float *, int, float *, int)" at 0x7f25f5b31570>'
    '__pyx_fuse_0_dot': None, # (!) real value is '<capsule object "float (int, float *, int, float *, int)" at 0x7f260e159f00>'
    '__pyx_fuse_0_gemm': None, # (!) real value is '<capsule object "void (enum __pyx_t_7sklearn_5utils_12_cython_blas_BLAS_Order, enum __pyx_t_7sklearn_5utils_12_cython_blas_BLAS_Trans, enum __pyx_t_7sklearn_5utils_12_cython_blas_BLAS_Trans, int, int, int, float, float *, int, float *, int, float, float *, int)" at 0x7f25f5b317b0>'
    '__pyx_fuse_0_gemv': None, # (!) real value is '<capsule object "void (enum __pyx_t_7sklearn_5utils_12_cython_blas_BLAS_Order, enum __pyx_t_7sklearn_5utils_12_cython_blas_BLAS_Trans, int, int, float, float *, int, float *, int, float, float *, int)" at 0x7f25f5b316f0>'
    '__pyx_fuse_0_ger': None, # (!) real value is '<capsule object "void (enum __pyx_t_7sklearn_5utils_12_cython_blas_BLAS_Order, int, int, float, float *, int, float *, int, float *, int)" at 0x7f25f5b31750>'
    '__pyx_fuse_0_nrm2': None, # (!) real value is '<capsule object "float (int, float *, int)" at 0x7f25f5b31510>'
    '__pyx_fuse_0_rot': None, # (!) real value is '<capsule object "void (int, float *, int, float *, int, float, float)" at 0x7f25f5b31690>'
    '__pyx_fuse_0_rotg': None, # (!) real value is '<capsule object "void (float *, float *, float *, float *)" at 0x7f25f5b31630>'
    '__pyx_fuse_0_scal': None, # (!) real value is '<capsule object "void (int, float, float *, int)" at 0x7f25f5b315d0>'
    '__pyx_fuse_1_asum': None, # (!) real value is '<capsule object "double (int, double *, int)" at 0x7f25f5b31480>'
    '__pyx_fuse_1_axpy': None, # (!) real value is '<capsule object "void (int, double, double *, int, double *, int)" at 0x7f25f5b314e0>'
    '__pyx_fuse_1_copy': None, # (!) real value is '<capsule object "void (int, double *, int, double *, int)" at 0x7f25f5b315a0>'
    '__pyx_fuse_1_dot': None, # (!) real value is '<capsule object "double (int, double *, int, double *, int)" at 0x7f260e159870>'
    '__pyx_fuse_1_gemm': None, # (!) real value is '<capsule object "void (enum __pyx_t_7sklearn_5utils_12_cython_blas_BLAS_Order, enum __pyx_t_7sklearn_5utils_12_cython_blas_BLAS_Trans, enum __pyx_t_7sklearn_5utils_12_cython_blas_BLAS_Trans, int, int, int, double, double *, int, double *, int, double, double *, int)" at 0x7f25f5b317e0>'
    '__pyx_fuse_1_gemv': None, # (!) real value is '<capsule object "void (enum __pyx_t_7sklearn_5utils_12_cython_blas_BLAS_Order, enum __pyx_t_7sklearn_5utils_12_cython_blas_BLAS_Trans, int, int, double, double *, int, double *, int, double, double *, int)" at 0x7f25f5b31720>'
    '__pyx_fuse_1_ger': None, # (!) real value is '<capsule object "void (enum __pyx_t_7sklearn_5utils_12_cython_blas_BLAS_Order, int, int, double, double *, int, double *, int, double *, int)" at 0x7f25f5b31780>'
    '__pyx_fuse_1_nrm2': None, # (!) real value is '<capsule object "double (int, double *, int)" at 0x7f25f5b31540>'
    '__pyx_fuse_1_rot': None, # (!) real value is '<capsule object "void (int, double *, int, double *, int, double, double)" at 0x7f25f5b316c0>'
    '__pyx_fuse_1_rotg': None, # (!) real value is '<capsule object "void (double *, double *, double *, double *)" at 0x7f25f5b31660>'
    '__pyx_fuse_1_scal': None, # (!) real value is '<capsule object "void (int, double, double *, int)" at 0x7f25f5b31600>'
}

__spec__ = None # (!) real value is "ModuleSpec(name='sklearn.utils._cython_blas', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f260d1e4e10>, origin='/home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/utils/_cython_blas.cpython-35m-x86_64-linux-gnu.so')"

__test__ = {}

