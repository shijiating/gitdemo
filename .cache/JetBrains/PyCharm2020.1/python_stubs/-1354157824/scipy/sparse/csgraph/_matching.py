# encoding: utf-8
# module scipy.sparse.csgraph._matching
# from /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/scipy/sparse/csgraph/_matching.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import numpy as np # /home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/numpy/__init__.py
import numpy as __numpy
import scipy.sparse.compressed as __scipy_sparse_compressed


# functions

def isspmatrix_coo(x): # reliably restored by inspect
    """
    Is x of coo_matrix type?
    
        Parameters
        ----------
        x
            object to check for being a coo matrix
    
        Returns
        -------
        bool
            True if x is a coo matrix, False otherwise
    
        Examples
        --------
        >>> from scipy.sparse import coo_matrix, isspmatrix_coo
        >>> isspmatrix_coo(coo_matrix([[5]]))
        True
    
        >>> from scipy.sparse import coo_matrix, csr_matrix, isspmatrix_coo
        >>> isspmatrix_coo(csr_matrix([[5]]))
        False
    """
    pass

def isspmatrix_csc(x): # reliably restored by inspect
    """
    Is x of csc_matrix type?
    
        Parameters
        ----------
        x
            object to check for being a csc matrix
    
        Returns
        -------
        bool
            True if x is a csc matrix, False otherwise
    
        Examples
        --------
        >>> from scipy.sparse import csc_matrix, isspmatrix_csc
        >>> isspmatrix_csc(csc_matrix([[5]]))
        True
    
        >>> from scipy.sparse import csc_matrix, csr_matrix, isspmatrix_csc
        >>> isspmatrix_csc(csr_matrix([[5]]))
        False
    """
    pass

def isspmatrix_csr(x): # reliably restored by inspect
    """
    Is x of csr_matrix type?
    
        Parameters
        ----------
        x
            object to check for being a csr matrix
    
        Returns
        -------
        bool
            True if x is a csr matrix, False otherwise
    
        Examples
        --------
        >>> from scipy.sparse import csr_matrix, isspmatrix_csr
        >>> isspmatrix_csr(csr_matrix([[5]]))
        True
    
        >>> from scipy.sparse import csc_matrix, csr_matrix, isspmatrix_csc
        >>> isspmatrix_csr(csc_matrix([[5]]))
        False
    """
    pass

def maximum_bipartite_matching(graph, perm_type='row'): # real signature unknown; restored from __doc__
    """
    maximum_bipartite_matching(graph, perm_type='row')
    
        Returns a matching of a bipartite graph whose cardinality is as least that
        of any given matching of the graph.
    
        Parameters
        ----------
        graph : sparse matrix
            Input sparse in CSR format whose rows represent one partition of the
            graph and whose columns represent the other partition. An edge between
            two vertices is indicated by the corresponding entry in the matrix
            existing in its sparse representation.
        perm_type : str, {'row', 'column'}
            Which partition to return the matching in terms of: If ``'row'``, the
            function produces an array whose length is the number of columns in the
            input, and whose :math:`j`'th element is the row matched to the
            :math:`j`'th column. Conversely, if ``perm_type`` is ``'column'``, this
            returns the columns matched to each row.
    
        Returns
        -------
        perm : ndarray
            A matching of the vertices in one of the two partitions. Unmatched
            vertices are represented by a ``-1`` in the result.
    
        Notes
        -----
        This function implements the Hopcroft--Karp algorithm [1]_. Its time
        complexity is :math:`O(\lvert E \rvert \sqrt{\lvert V \rvert})`, and its
        space complexity is linear in the number of rows. In practice, this
        asymmetry between rows and columns means that it can be more efficient to
        transpose the input if it contains more columns than rows.
    
        By Konig's theorem, the cardinality of the matching is also the number of
        vertices appearing in a minimum vertex cover of the graph.
    
        Note that if the sparse representation contains explicit zeros, these are
        still counted as edges.
    
        The implementation was changed in SciPy 1.4.0 to allow matching of general
        bipartite graphs, where previous versions would assume that a perfect
        matching existed. As such, code written against 1.4.0 will not necessarily
        work on older versions.
    
        References
        ----------
        .. [1] John E. Hopcroft and Richard M. Karp. "An n^{5 / 2} Algorithm for
               Maximum Matchings in Bipartite Graphs" In: SIAM Journal of Computing
               2.4 (1973), pp. 225--231. <https://dx.doi.org/10.1137/0202019>.
    
        Examples
        --------
        >>> from scipy.sparse import csr_matrix
        >>> from scipy.sparse.csgraph import maximum_bipartite_matching
    
        As a simple example, consider a bipartite graph in which the partitions
        contain 2 and 3 elements respectively. Suppose that one partition contains
        vertices labelled 0 and 1, and that the other partition contains vertices
        labelled A, B, and C. Suppose that there are edges connecting 0 and C,
        1 and A, and 1 and B. This graph would then be represented by the following
        sparse matrix:
    
        >>> graph = csr_matrix([[0, 0, 1], [1, 1, 0]])
    
        Here, the 1s could be anything, as long as they end up being stored as
        elements in the sparse matrix. We can now calculate maximum matchings as
        follows:
    
        >>> print(maximum_bipartite_matching(graph, perm_type='column'))
        [2 0]
        >>> print(maximum_bipartite_matching(graph, perm_type='row'))
        [ 1 -1  0]
    
        The first output tells us that 1 and 2 are matched with C and A
        respectively, and the second output tells us that A, B, and C are matched
        with 1, nothing, and 0 respectively.
    
        Note that explicit zeros are still converted to edges. This means that a
        different way to represent the above graph is by using the CSR structure
        directly as follows:
    
        >>> data = [0, 0, 0]
        >>> indices = [2, 0, 1]
        >>> indptr = [0, 1, 3]
        >>> graph = csr_matrix((data, indices, indptr))
        >>> print(maximum_bipartite_matching(graph, perm_type='column'))
        [2 0]
        >>> print(maximum_bipartite_matching(graph, perm_type='row'))
        [ 1 -1  0]
    
        When one or both of the partitions are empty, the matching is empty as
        well:
    
        >>> graph = csr_matrix((2, 0))
        >>> print(maximum_bipartite_matching(graph, perm_type='column'))
        [-1 -1]
        >>> print(maximum_bipartite_matching(graph, perm_type='row'))
        []
    
        When the input matrix is square, and the graph is known to admit a perfect
        matching, i.e. a matching with the property that every vertex in the graph
        belongs to some edge in the matching, then one can view the output as the
        permutation of rows (or columns) turning the input matrix into one with the
        property that all diagonal elements are non-empty:
    
        >>> a = [[0, 1, 2, 0], [1, 0, 0, 1], [2, 0, 0, 3], [0, 1, 3, 0]]
        >>> graph = csr_matrix(a)
        >>> perm = maximum_bipartite_matching(graph, perm_type='row')
        >>> print(graph[perm].toarray())
        [[1 0 0 1]
         [0 1 2 0]
         [0 1 3 0]
         [2 0 0 3]]
    """
    pass

def __pyx_unpickle_Enum(*args, **kwargs): # real signature unknown
    pass

# classes

class csr_matrix(__scipy_sparse_compressed._cs_matrix):
    """
    Compressed Sparse Row matrix
    
        This can be instantiated in several ways:
            csr_matrix(D)
                with a dense matrix or rank-2 ndarray D
    
            csr_matrix(S)
                with another sparse matrix S (equivalent to S.tocsr())
    
            csr_matrix((M, N), [dtype])
                to construct an empty matrix with shape (M, N)
                dtype is optional, defaulting to dtype='d'.
    
            csr_matrix((data, (row_ind, col_ind)), [shape=(M, N)])
                where ``data``, ``row_ind`` and ``col_ind`` satisfy the
                relationship ``a[row_ind[k], col_ind[k]] = data[k]``.
    
            csr_matrix((data, indices, indptr), [shape=(M, N)])
                is the standard CSR representation where the column indices for
                row i are stored in ``indices[indptr[i]:indptr[i+1]]`` and their
                corresponding values are stored in ``data[indptr[i]:indptr[i+1]]``.
                If the shape parameter is not supplied, the matrix dimensions
                are inferred from the index arrays.
    
        Attributes
        ----------
        dtype : dtype
            Data type of the matrix
        shape : 2-tuple
            Shape of the matrix
        ndim : int
            Number of dimensions (this is always 2)
        nnz
            Number of stored values, including explicit zeros
        data
            CSR format data array of the matrix
        indices
            CSR format index array of the matrix
        indptr
            CSR format index pointer array of the matrix
        has_sorted_indices
            Whether indices are sorted
    
        Notes
        -----
    
        Sparse matrices can be used in arithmetic operations: they support
        addition, subtraction, multiplication, division, and matrix power.
    
        Advantages of the CSR format
          - efficient arithmetic operations CSR + CSR, CSR * CSR, etc.
          - efficient row slicing
          - fast matrix vector products
    
        Disadvantages of the CSR format
          - slow column slicing operations (consider CSC)
          - changes to the sparsity structure are expensive (consider LIL or DOK)
    
        Examples
        --------
    
        >>> import numpy as np
        >>> from scipy.sparse import csr_matrix
        >>> csr_matrix((3, 4), dtype=np.int8).toarray()
        array([[0, 0, 0, 0],
               [0, 0, 0, 0],
               [0, 0, 0, 0]], dtype=int8)
    
        >>> row = np.array([0, 0, 1, 2, 2, 2])
        >>> col = np.array([0, 2, 2, 0, 1, 2])
        >>> data = np.array([1, 2, 3, 4, 5, 6])
        >>> csr_matrix((data, (row, col)), shape=(3, 3)).toarray()
        array([[1, 0, 2],
               [0, 0, 3],
               [4, 5, 6]])
    
        >>> indptr = np.array([0, 2, 3, 6])
        >>> indices = np.array([0, 2, 2, 0, 1, 2])
        >>> data = np.array([1, 2, 3, 4, 5, 6])
        >>> csr_matrix((data, indices, indptr), shape=(3, 3)).toarray()
        array([[1, 0, 2],
               [0, 0, 3],
               [4, 5, 6]])
    
        As an example of how to construct a CSR matrix incrementally,
        the following snippet builds a term-document matrix from texts:
    
        >>> docs = [["hello", "world", "hello"], ["goodbye", "cruel", "world"]]
        >>> indptr = [0]
        >>> indices = []
        >>> data = []
        >>> vocabulary = {}
        >>> for d in docs:
        ...     for term in d:
        ...         index = vocabulary.setdefault(term, len(vocabulary))
        ...         indices.append(index)
        ...         data.append(1)
        ...     indptr.append(len(indices))
        ...
        >>> csr_matrix((data, indices, indptr), dtype=int).toarray()
        array([[2, 1, 0, 0],
               [0, 1, 1, 1]])
    """
    def getcol(self, i): # reliably restored by inspect
        """
        Returns a copy of column i of the matrix, as a (m x 1)
                CSR matrix (column vector).
        """
        pass

    def getrow(self, i): # reliably restored by inspect
        """
        Returns a copy of row i of the matrix, as a (1 x n)
                CSR matrix (row vector).
        """
        pass

    def tobsr(self, blocksize=None, copy=True): # reliably restored by inspect
        """
        Convert this matrix to Block Sparse Row format.
        
                With copy=False, the data/indices may be shared between this matrix and
                the resultant bsr_matrix.
        
                When blocksize=(R, C) is provided, it will be used for construction of
                the bsr_matrix.
        """
        pass

    def tocsc(self, copy=False): # reliably restored by inspect
        """
        Convert this matrix to Compressed Sparse Column format.
        
                With copy=False, the data/indices may be shared between this matrix and
                the resultant csc_matrix.
        """
        pass

    def tocsr(self, copy=False): # reliably restored by inspect
        """
        Convert this matrix to Compressed Sparse Row format.
        
                With copy=False, the data/indices may be shared between this matrix and
                the resultant csr_matrix.
        """
        pass

    def tolil(self, copy=False): # reliably restored by inspect
        """
        Convert this matrix to List of Lists format.
        
                With copy=False, the data/indices may be shared between this matrix and
                the resultant lil_matrix.
        """
        pass

    def transpose(self, axes=None, copy=False): # reliably restored by inspect
        """
        Reverses the dimensions of the sparse matrix.
        
                Parameters
                ----------
                axes : None, optional
                    This argument is in the signature *solely* for NumPy
                    compatibility reasons. Do not pass in anything except
                    for the default value.
                copy : bool, optional
                    Indicates whether or not attributes of `self` should be
                    copied whenever possible. The degree to which attributes
                    are copied varies depending on the type of sparse matrix
                    being used.
        
                Returns
                -------
                p : `self` with the dimensions reversed.
        
                See Also
                --------
                numpy.matrix.transpose : NumPy's implementation of 'transpose'
                                         for matrices
        """
        pass

    def _get_arrayXint(self, row, col): # reliably restored by inspect
        # no doc
        pass

    def _get_arrayXslice(self, row, col): # reliably restored by inspect
        # no doc
        pass

    def _get_intXarray(self, row, col): # reliably restored by inspect
        # no doc
        pass

    def _get_intXslice(self, row, col): # reliably restored by inspect
        # no doc
        pass

    def _get_sliceXarray(self, row, col): # reliably restored by inspect
        # no doc
        pass

    def _get_sliceXint(self, row, col): # reliably restored by inspect
        # no doc
        pass

    def _swap(self, x): # reliably restored by inspect
        """ swap the members of x if this is a column-oriented matrix """
        pass

    def __init__(self, arg1, shape=None, dtype=None, copy=False): # reliably restored by inspect
        # no doc
        pass

    def __iter__(self): # reliably restored by inspect
        # no doc
        pass

    format = 'csr'


class DTYPE(__numpy.floating, float):
    """
    Double-precision floating-point number type, compatible with Python `float`
        and C ``double``.
        Character code: ``'d'``.
        Canonical name: ``np.double``.
        Alias: ``np.float_``.
        Alias *on this platform*: ``np.float64``: 64-bit precision floating-point number type: sign bit, 11 bits exponent, 52 bits mantissa.
    """
    def as_integer_ratio(self): # real signature unknown; restored from __doc__
        """
        double.as_integer_ratio() -> (int, int)
        
                Return a pair of integers, whose ratio is exactly equal to the original
                floating point number, and with a positive denominator.
                Raise OverflowError on infinities and a ValueError on NaNs.
        
                >>> np.double(10.0).as_integer_ratio()
                (10, 1)
                >>> np.double(0.0).as_integer_ratio()
                (0, 1)
                >>> np.double(-.25).as_integer_ratio()
                (-1, 4)
        """
        pass

    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass


class ITYPE(__numpy.signedinteger):
    """
    Signed integer type, compatible with C ``int``.
        Character code: ``'i'``.
        Canonical name: ``np.intc``.
        Alias *on this platform*: ``np.int32``: 32-bit signed integer (-2147483648 to 2147483647).
    """
    def __abs__(self, *args, **kwargs): # real signature unknown
        """ abs(self) """
        pass

    def __add__(self, *args, **kwargs): # real signature unknown
        """ Return self+value. """
        pass

    def __and__(self, *args, **kwargs): # real signature unknown
        """ Return self&value. """
        pass

    def __bool__(self, *args, **kwargs): # real signature unknown
        """ self != 0 """
        pass

    def __divmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(self, value). """
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __float__(self, *args, **kwargs): # real signature unknown
        """ float(self) """
        pass

    def __floordiv__(self, *args, **kwargs): # real signature unknown
        """ Return self//value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __hash__(self, *args, **kwargs): # real signature unknown
        """ Return hash(self). """
        pass

    def __index__(self, *args, **kwargs): # real signature unknown
        """ Return self converted to an integer, if self is suitable for use as an index into a list. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __int__(self, *args, **kwargs): # real signature unknown
        """ int(self) """
        pass

    def __invert__(self, *args, **kwargs): # real signature unknown
        """ ~self """
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lshift__(self, *args, **kwargs): # real signature unknown
        """ Return self<<value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mod__(self, *args, **kwargs): # real signature unknown
        """ Return self%value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    def __neg__(self, *args, **kwargs): # real signature unknown
        """ -self """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __or__(self, *args, **kwargs): # real signature unknown
        """ Return self|value. """
        pass

    def __pos__(self, *args, **kwargs): # real signature unknown
        """ +self """
        pass

    def __pow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(self, value, mod). """
        pass

    def __radd__(self, *args, **kwargs): # real signature unknown
        """ Return value+self. """
        pass

    def __rand__(self, *args, **kwargs): # real signature unknown
        """ Return value&self. """
        pass

    def __rdivmod__(self, *args, **kwargs): # real signature unknown
        """ Return divmod(value, self). """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rfloordiv__(self, *args, **kwargs): # real signature unknown
        """ Return value//self. """
        pass

    def __rlshift__(self, *args, **kwargs): # real signature unknown
        """ Return value<<self. """
        pass

    def __rmod__(self, *args, **kwargs): # real signature unknown
        """ Return value%self. """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    def __ror__(self, *args, **kwargs): # real signature unknown
        """ Return value|self. """
        pass

    def __rpow__(self, *args, **kwargs): # real signature unknown
        """ Return pow(value, self, mod). """
        pass

    def __rrshift__(self, *args, **kwargs): # real signature unknown
        """ Return value>>self. """
        pass

    def __rshift__(self, *args, **kwargs): # real signature unknown
        """ Return self>>value. """
        pass

    def __rsub__(self, *args, **kwargs): # real signature unknown
        """ Return value-self. """
        pass

    def __rtruediv__(self, *args, **kwargs): # real signature unknown
        """ Return value/self. """
        pass

    def __rxor__(self, *args, **kwargs): # real signature unknown
        """ Return value^self. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    def __sub__(self, *args, **kwargs): # real signature unknown
        """ Return self-value. """
        pass

    def __truediv__(self, *args, **kwargs): # real signature unknown
        """ Return self/value. """
        pass

    def __xor__(self, *args, **kwargs): # real signature unknown
        """ Return self^value. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f2600691f28>'

__spec__ = None # (!) real value is "ModuleSpec(name='scipy.sparse.csgraph._matching', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f2600691f28>, origin='/home/sjt/chinafyl-adminycj-master/venv/ycj35/lib/python3.5/site-packages/scipy/sparse/csgraph/_matching.cpython-35m-x86_64-linux-gnu.so')"

__test__ = {
    'maximum_bipartite_matching (line 12)': '\n    maximum_bipartite_matching(graph, perm_type=\'row\')\n\n    Returns a matching of a bipartite graph whose cardinality is as least that\n    of any given matching of the graph.\n\n    Parameters\n    ----------\n    graph : sparse matrix\n        Input sparse in CSR format whose rows represent one partition of the\n        graph and whose columns represent the other partition. An edge between\n        two vertices is indicated by the corresponding entry in the matrix\n        existing in its sparse representation.\n    perm_type : str, {\'row\', \'column\'}\n        Which partition to return the matching in terms of: If ``\'row\'``, the\n        function produces an array whose length is the number of columns in the\n        input, and whose :math:`j`\'th element is the row matched to the\n        :math:`j`\'th column. Conversely, if ``perm_type`` is ``\'column\'``, this\n        returns the columns matched to each row.\n\n    Returns\n    -------\n    perm : ndarray\n        A matching of the vertices in one of the two partitions. Unmatched\n        vertices are represented by a ``-1`` in the result.\n\n    Notes\n    -----\n    This function implements the Hopcroft--Karp algorithm [1]_. Its time\n    complexity is :math:`O(\\lvert E \\rvert \\sqrt{\\lvert V \\rvert})`, and its\n    space complexity is linear in the number of rows. In practice, this\n    asymmetry between rows and columns means that it can be more efficient to\n    transpose the input if it contains more columns than rows.\n\n    By Konig\'s theorem, the cardinality of the matching is also the number of\n    vertices appearing in a minimum vertex cover of the graph.\n\n    Note that if the sparse representation contains explicit zeros, these are\n    still counted as edges.\n\n    The implementation was changed in SciPy 1.4.0 to allow matching of general\n    bipartite graphs, where previous versions would assume that a perfect\n    matching existed. As such, code written against 1.4.0 will not necessarily\n    work on older versions.\n\n    References\n    ----------\n    .. [1] John E. Hopcroft and Richard M. Karp. "An n^{5 / 2} Algorithm for\n           Maximum Matchings in Bipartite Graphs" In: SIAM Journal of Computing\n           2.4 (1973), pp. 225--231. <https://dx.doi.org/10.1137/0202019>.\n\n    Examples\n    --------\n    >>> from scipy.sparse import csr_matrix\n    >>> from scipy.sparse.csgraph import maximum_bipartite_matching\n\n    As a simple example, consider a bipartite graph in which the partitions\n    contain 2 and 3 elements respectively. Suppose that one partition contains\n    vertices labelled 0 and 1, and that the other partition contains vertices\n    labelled A, B, and C. Suppose that there are edges connecting 0 and C,\n    1 and A, and 1 and B. This graph would then be represented by the following\n    sparse matrix:\n\n    >>> graph = csr_matrix([[0, 0, 1], [1, 1, 0]])\n\n    Here, the 1s could be anything, as long as they end up being stored as\n    elements in the sparse matrix. We can now calculate maximum matchings as\n    follows:\n\n    >>> print(maximum_bipartite_matching(graph, perm_type=\'column\'))\n    [2 0]\n    >>> print(maximum_bipartite_matching(graph, perm_type=\'row\'))\n    [ 1 -1  0]\n\n    The first output tells us that 1 and 2 are matched with C and A\n    respectively, and the second output tells us that A, B, and C are matched\n    with 1, nothing, and 0 respectively.\n\n    Note that explicit zeros are still converted to edges. This means that a\n    different way to represent the above graph is by using the CSR structure\n    directly as follows:\n\n    >>> data = [0, 0, 0]\n    >>> indices = [2, 0, 1]\n    >>> indptr = [0, 1, 3]\n    >>> graph = csr_matrix((data, indices, indptr))\n    >>> print(maximum_bipartite_matching(graph, perm_type=\'column\'))\n    [2 0]\n    >>> print(maximum_bipartite_matching(graph, perm_type=\'row\'))\n    [ 1 -1  0]\n\n    When one or both of the partitions are empty, the matching is empty as\n    well:\n\n    >>> graph = csr_matrix((2, 0))\n    >>> print(maximum_bipartite_matching(graph, perm_type=\'column\'))\n    [-1 -1]\n    >>> print(maximum_bipartite_matching(graph, perm_type=\'row\'))\n    []\n\n    When the input matrix is square, and the graph is known to admit a perfect\n    matching, i.e. a matching with the property that every vertex in the graph\n    belongs to some edge in the matching, then one can view the output as the\n    permutation of rows (or columns) turning the input matrix into one with the\n    property that all diagonal elements are non-empty:\n\n    >>> a = [[0, 1, 2, 0], [1, 0, 0, 1], [2, 0, 0, 3], [0, 1, 3, 0]]\n    >>> graph = csr_matrix(a)\n    >>> perm = maximum_bipartite_matching(graph, perm_type=\'row\')\n    >>> print(graph[perm].toarray())\n    [[1 0 0 1]\n     [0 1 2 0]\n     [0 1 3 0]\n     [2 0 0 3]]\n\n    ',
}

