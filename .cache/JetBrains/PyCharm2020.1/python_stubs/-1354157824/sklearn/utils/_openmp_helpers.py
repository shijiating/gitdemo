# encoding: utf-8
# module sklearn.utils._openmp_helpers
# from /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/utils/_openmp_helpers.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import os as os # /usr/lib/python3.5/os.py

# functions

def cpu_count(): # reliably restored by inspect
    """ Return the number of CPUs. """
    pass

def _openmp_effective_n_threads(*args, **kwargs): # real signature unknown
    """
    Determine the effective number of threads to be used for OpenMP calls
    
        - For ``n_threads = None``,
          - if the ``OMP_NUM_THREADS`` environment variable is set, return
            ``openmp.omp_get_max_threads()``
          - otherwise, return the minimum between ``openmp.omp_get_max_threads()``
            and the number of cpus, taking cgroups quotas into account. Cgroups 
            quotas can typically be set by tools such as Docker.
          The result of ``omp_get_max_threads`` can be influenced by environment
          variable ``OMP_NUM_THREADS`` or at runtime by ``omp_set_num_threads``.
    
        - For ``n_threads > 0``, return this as the maximal number of threads for
          parallel OpenMP calls.
    
        - For ``n_threads < 0``, return the maximal number of threads minus
          ``|n_threads + 1|``. In particular ``n_threads = -1`` will use as many
          threads as there are available cores on the machine.
    
        - Raise a ValueError for ``n_threads = 0``.
    
        If scikit-learn is built without OpenMP support, always return 1.
    """
    pass

def _openmp_parallelism_enabled(*args, **kwargs): # real signature unknown
    """
    Determines whether scikit-learn has been built with OpenMP
        
        It allows to retrieve at runtime the information gathered at compile time.
    """
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25f5b43f98>'

__spec__ = None # (!) real value is "ModuleSpec(name='sklearn.utils._openmp_helpers', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f25f5b43f98>, origin='/home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/sklearn/utils/_openmp_helpers.cpython-35m-x86_64-linux-gnu.so')"

__test__ = {}

