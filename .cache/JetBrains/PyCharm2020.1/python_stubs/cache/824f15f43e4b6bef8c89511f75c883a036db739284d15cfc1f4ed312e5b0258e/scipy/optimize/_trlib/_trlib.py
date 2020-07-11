# encoding: utf-8
# module scipy.optimize._trlib._trlib
# from /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/scipy/optimize/_trlib/_trlib.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/numpy/__init__.py
import scipy.optimize._trustregion as __scipy_optimize__trustregion


# functions

def _minimize_trust_region(fun, x0, args='()', jac=None, hess=None, hessp=None, subproblem=None, initial_trust_radius=1.0, max_trust_radius=1000.0, eta=0.15, gtol=0.0001, maxiter=None, disp=False, return_all=False, callback=None, inexact=True, **unknown_options): # reliably restored by inspect
    """
    Minimization of scalar function of one or more variables using a
        trust-region algorithm.
    
        Options for the trust-region algorithm are:
            initial_trust_radius : float
                Initial trust radius.
            max_trust_radius : float
                Never propose steps that are longer than this value.
            eta : float
                Trust region related acceptance stringency for proposed steps.
            gtol : float
                Gradient norm must be less than `gtol`
                before successful termination.
            maxiter : int
                Maximum number of iterations to perform.
            disp : bool
                If True, print convergence message.
            inexact : bool
                Accuracy to solve subproblems. If True requires less nonlinear
                iterations, but more vector products. Only effective for method
                trust-krylov.
    
        This function is called by the `minimize` function.
        It is not supposed to be called directly.
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class BaseQuadraticSubproblem(object):
    """
    Base/abstract class defining the quadratic model for trust-region
        minimization. Child classes must implement the ``solve`` method.
    
        Values of the objective function, jacobian and hessian (if provided) at
        the current iterate ``x`` are evaluated on demand and then stored as
        attributes ``fun``, ``jac``, ``hess``.
    """
    def get_boundaries_intersections(self, z, d, trust_radius): # reliably restored by inspect
        """
        Solve the scalar quadratic equation ||z + t d|| == trust_radius.
                This is like a line-sphere intersection.
                Return the two values of t, sorted from low to high.
        """
        pass

    def hessp(self, p): # reliably restored by inspect
        # no doc
        pass

    def solve(self, trust_radius): # reliably restored by inspect
        # no doc
        pass

    def __call__(self, p): # reliably restored by inspect
        # no doc
        pass

    def __init__(self, x, fun, jac, hess=None, hessp=None): # reliably restored by inspect
        # no doc
        pass

    fun = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Value of objective function at current iteration."""

    hess = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Value of hessian of objective function at current iteration."""

    jac = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Value of jacobian of objective function at current iteration."""

    jac_mag = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Magniture of jacobian of objective function at current iteration."""

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    __dict__ = None # (!) real value is "mappingproxy({'__dict__': <attribute '__dict__' of 'BaseQuadraticSubproblem' objects>, '__init__': <function BaseQuadraticSubproblem.__init__ at 0x7f2600632a60>, '__weakref__': <attribute '__weakref__' of 'BaseQuadraticSubproblem' objects>, 'hessp': <function BaseQuadraticSubproblem.hessp at 0x7f2600632d08>, '__module__': 'scipy.optimize._trustregion', 'jac': <property object at 0x7f260064f728>, '__doc__': '\\n    Base/abstract class defining the quadratic model for trust-region\\n    minimization. Child classes must implement the ``solve`` method.\\n\\n    Values of the objective function, jacobian and hessian (if provided) at\\n    the current iterate ``x`` are evaluated on demand and then stored as\\n    attributes ``fun``, ``jac``, ``hess``.\\n    ', '__call__': <function BaseQuadraticSubproblem.__call__ at 0x7f2600632ae8>, 'get_boundaries_intersections': <function BaseQuadraticSubproblem.get_boundaries_intersections at 0x7f2600632e18>, 'solve': <function BaseQuadraticSubproblem.solve at 0x7f2600632ea0>, 'fun': <property object at 0x7f260064f6d8>, 'jac_mag': <property object at 0x7f260064f7c8>, 'hess': <property object at 0x7f260064f778>})"


class TRLIBQuadraticSubproblem(__scipy_optimize__trustregion.BaseQuadraticSubproblem):
    # no doc
    def solve(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f260064df60>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.optimize._trlib._trlib', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f260064df60>, origin='/home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/scipy/optimize/_trlib/_trlib.cpython-35m-x86_64-linux-gnu.so')"

__test__ = {}

