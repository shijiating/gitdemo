# encoding: utf-8
# module Onboard.osk
# from /usr/lib/python3/dist-packages/Onboard/osk.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
""" osk utility module """
# no imports

# no functions
# classes

class Audio(object):
    """ Audio objects """
    def cache_sample(self, *args, **kwargs): # real signature unknown
        pass

    def cancel(self, *args, **kwargs): # real signature unknown
        pass

    def disable(self, *args, **kwargs): # real signature unknown
        pass

    def enable(self, *args, **kwargs): # real signature unknown
        pass

    def play(self, *args, **kwargs): # real signature unknown
        pass

    def set_theme(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class ClickMapper(object):
    """ ClickMapper objects """
    def convert_primary_click(self, *args, **kwargs): # real signature unknown
        pass

    def generate_button_event(self, *args, **kwargs): # real signature unknown
        pass

    def generate_motion_event(self, *args, **kwargs): # real signature unknown
        pass

    def map_pointer_button(self, *args, **kwargs): # real signature unknown
        pass

    def restore_pointer_buttons(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    button = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    click_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class DConf(object):
    """ DConf objects """
    def read_key(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class DeviceEvent(object):
    """ DeviceEvent objects """
    def get_source_device(self, *args, **kwargs): # real signature unknown
        pass

    def get_time(self, *args, **kwargs): # real signature unknown
        pass

    def set_source_device(self, *args, **kwargs): # real signature unknown
        pass

    def __copy__(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    button = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    device_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    keyval = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    sequence = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    source_id = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    state = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    time = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xid_event = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    xi_type = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    x_root = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default

    y_root = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default



class Devices(object):
    """ Devices objects """
    def attach(self, *args, **kwargs): # real signature unknown
        pass

    def detach(self, *args, **kwargs): # real signature unknown
        pass

    def get_client_pointer(self, *args, **kwargs): # real signature unknown
        pass

    def get_info(self, *args, **kwargs): # real signature unknown
        pass

    def grab_device(self, *args, **kwargs): # real signature unknown
        pass

    def list(self, *args, **kwargs): # real signature unknown
        pass

    def select_events(self, *args, **kwargs): # real signature unknown
        pass

    def ungrab_device(self, *args, **kwargs): # real signature unknown
        pass

    def unselect_events(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class error(Exception):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class Hunspell(object):
    """ Hunspell objects """
    def get_encoding(self, *args, **kwargs): # real signature unknown
        pass

    def spell(self, *args, **kwargs): # real signature unknown
        pass

    def suggest(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class Struts(object):
    """ Struts objects """
    def clear(self, *args, **kwargs): # real signature unknown
        pass

    def set(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class Util(object):
    """ Util objects """
    def connect_root_property_notify(self, *args, **kwargs): # real signature unknown
        pass

    def get_current_wm_name(self, *args, **kwargs): # real signature unknown
        pass

    def keep_windows_on_top(self, *args, **kwargs): # real signature unknown
        pass

    def remove_atom_from_property(self, *args, **kwargs): # real signature unknown
        pass

    def set_input_rect(self, *args, **kwargs): # real signature unknown
        pass

    def set_unix_signal_handler(self, *args, **kwargs): # real signature unknown
        pass

    def set_x_property(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class Virtkey(object):
    """ Virtkey objects """
    def get_current_group(self, *args, **kwargs): # real signature unknown
        pass

    def get_current_group_name(self, *args, **kwargs): # real signature unknown
        pass

    def get_layout_symbols(self, *args, **kwargs): # real signature unknown
        pass

    def get_rules_names(self, *args, **kwargs): # real signature unknown
        pass

    def keysyms_from_keycode(self, *args, **kwargs): # real signature unknown
        pass

    def labels_from_keycode(self, *args, **kwargs): # real signature unknown
        pass

    def latch_mod(self, *args, **kwargs): # real signature unknown
        pass

    def lock_mod(self, *args, **kwargs): # real signature unknown
        pass

    def press_keycode(self, *args, **kwargs): # real signature unknown
        pass

    def press_keysym(self, *args, **kwargs): # real signature unknown
        pass

    def press_unicode(self, *args, **kwargs): # real signature unknown
        pass

    def release_keycode(self, *args, **kwargs): # real signature unknown
        pass

    def release_keysym(self, *args, **kwargs): # real signature unknown
        pass

    def release_unicode(self, *args, **kwargs): # real signature unknown
        pass

    def reload(self, *args, **kwargs): # real signature unknown
        pass

    def unlatch_mod(self, *args, **kwargs): # real signature unknown
        pass

    def unlock_mod(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fb820ce3b38>'

__spec__ = None # (!) real value is "ModuleSpec(name='Onboard.osk', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fb820ce3b38>, origin='/usr/lib/python3/dist-packages/Onboard/osk.cpython-35m-x86_64-linux-gnu.so')"

