# encoding: utf-8
# module Onboard.pypredict.lm
# from /usr/lib/python3/dist-packages/Onboard/pypredict/lm.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
""" Dynamically updatable n-gram language models. """

# imports
import lm as __lm


# functions

def linint(*args, **kwargs): # real signature unknown
    pass

def loglinint(*args, **kwargs): # real signature unknown
    pass

def overlay(*args, **kwargs): # real signature unknown
    pass

# classes

class LanguageModel(object):
    """ LanguageModel objects """
    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def get_probability(self, *args, **kwargs): # real signature unknown
        pass

    def load(self, *args, **kwargs): # real signature unknown
        pass

    def lookup_word(self, *args, **kwargs): # real signature unknown
        pass

    def predict(self, *args, **kwargs): # real signature unknown
        pass

    def predictp(self, *args, **kwargs): # real signature unknown
        pass

    def save(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    ACCENT_INSENSITIVE = 4
    ACCENT_INSENSITIVE_SMART = 8
    CASE_INSENSITIVE = 1
    CASE_INSENSITIVE_SMART = 2
    IGNORE_CAPITALIZED = 16
    IGNORE_NON_CAPITALIZED = 32
    INCLUDE_CONTROL_WORDS = 64
    NORMALIZE = 256
    NO_SORT = 128
    NUM_CONTROL_WORDS = 4


class DynamicModel(__lm.LanguageModel):
    """ DynamicModel objects """
    def count_ngram(self, *args, **kwargs): # real signature unknown
        pass

    def get_ngram_count(self, *args, **kwargs): # real signature unknown
        pass

    def iter_ngrams(self, *args, **kwargs): # real signature unknown
        pass

    def memory_size(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """order of the language model"""

    smoothing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ngram smoothing: 'witten-bell' (default) or 'kneser-ney'"""



class DynamicModelKN(__lm.DynamicModel):
    """ DynamicModelKN objects """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class CachedDynamicModel(__lm.DynamicModelKN):
    """ CachedDynamicModel objects """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    recency_halflife = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """halflife of exponential falloff in number of recently used words until w=0.5"""

    recency_lambdas = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """jelinec-mercer smoothing weights, one per order"""

    recency_ratio = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ratio of recency-based to count-based probabilities"""

    recency_smoothing = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """ngram recency smoothing: 'jelinec-mercer' (default) or 'witten-bell'"""



class UnigramModel(__lm.LanguageModel):
    """ UnigramModel objects """
    def count_ngram(self, *args, **kwargs): # real signature unknown
        pass

    def get_ngram_count(self, *args, **kwargs): # real signature unknown
        pass

    def iter_ngrams(self, *args, **kwargs): # real signature unknown
        pass

    def memory_size(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    order = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """order of the language model"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fb820afa048>'

__spec__ = None # (!) real value is "ModuleSpec(name='Onboard.pypredict.lm', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fb820afa048>, origin='/usr/lib/python3/dist-packages/Onboard/pypredict/lm.cpython-35m-x86_64-linux-gnu.so')"

