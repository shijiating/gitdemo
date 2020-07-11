# encoding: utf-8
# module hpmudext
# from /usr/lib/python3/dist-packages/hpmudext.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
""" Python extension for HP multi-point transport driver """
# no imports

# Variables with simple values

HPMUD_BUFFER_SIZE = 16384

HPMUD_BUS_ALL = 3
HPMUD_BUS_NA = 0
HPMUD_BUS_PARALLEL = 2
HPMUD_BUS_USB = 1

HPMUD_DOT4_BRIDGE_MODE = 5

HPMUD_DOT4_MODE = 3

HPMUD_DOT4_PHOENIX_MODE = 4

HPMUD_MLC_GUSHER_MODE = 6

HPMUD_MLC_MISER_MODE = 7

HPMUD_RAW_MODE = 1

HPMUD_R_DATFILE_ERROR = 48

HPMUD_R_DEVICE_BUSY = 21

HPMUD_R_INVALID_CHANNEL_ID = 30

HPMUD_R_INVALID_DESCRIPTOR = 3
HPMUD_R_INVALID_DEVICE = 2

HPMUD_R_INVALID_DEVICE_NODE = 38
HPMUD_R_INVALID_DEVICE_OPEN = 37

HPMUD_R_INVALID_IP = 45

HPMUD_R_INVALID_IP_PORT = 46

HPMUD_R_INVALID_LENGTH = 8
HPMUD_R_INVALID_SN = 28
HPMUD_R_INVALID_STATE = 31
HPMUD_R_INVALID_TIMEOUT = 47
HPMUD_R_INVALID_URI = 4

HPMUD_R_IO_ERROR = 12
HPMUD_R_IO_TIMEOUT = 49

HPMUD_R_OK = 0

HPMUD_S_CONFIG_DOWNLOAD_CHANNEL = 'HP-CONFIGURATION-DOWNLOAD'

HPMUD_S_CONFIG_UPLOAD_CHANNEL = 'HP-CONFIGURATION-UPLOAD'

HPMUD_S_DEVMGMT_CHANNEL = 'HP-DEVMGMT'

HPMUD_S_EWS_CHANNEL = 'HP-EWS'

HPMUD_S_EWS_LEDM_CHANNEL = 'HP-EWS-LEDM'

HPMUD_S_FAX_SEND_CHANNEL = 'HP-FAX-SEND'

HPMUD_S_LEDM_SCAN = 'HP-LEDM-SCAN'

HPMUD_S_MARVELL_EWS_CHANNEL = 'HP-MARVELL-EWS'

HPMUD_S_MARVELL_FAX_CHANNEL = 'HP-MARVELL-FAX'

HPMUD_S_MEMORY_CARD_CHANNEL = 'HP-CARD-ACCESS'

HPMUD_S_PML_CHANNEL = 'HP-MESSAGE'

HPMUD_S_PRINT_CHANNEL = 'PRINT'

HPMUD_S_SCAN_CHANNEL = 'HP-SCAN'

HPMUD_S_SOAP_FAX = 'HP-SOAP-FAX'
HPMUD_S_SOAP_SCAN = 'HP-SOAP-SCAN'

HPMUD_S_WIFI_CHANNEL = 'HP-WIFICONFIG'

HPMUD_UNI_MODE = 0

# functions

def close_channel(*args, **kwargs): # real signature unknown
    pass

def close_device(*args, **kwargs): # real signature unknown
    pass

def get_device_id(*args, **kwargs): # real signature unknown
    pass

def get_pml(*args, **kwargs): # real signature unknown
    pass

def get_zc_ip_address(*args, **kwargs): # real signature unknown
    pass

def make_net_uri(*args, **kwargs): # real signature unknown
    pass

def make_par_uri(*args, **kwargs): # real signature unknown
    pass

def make_usb_uri(*args, **kwargs): # real signature unknown
    pass

def make_zc_uri(*args, **kwargs): # real signature unknown
    pass

def open_channel(*args, **kwargs): # real signature unknown
    pass

def open_device(*args, **kwargs): # real signature unknown
    pass

def probe_devices(*args, **kwargs): # real signature unknown
    pass

def read_channel(*args, **kwargs): # real signature unknown
    pass

def set_pml(*args, **kwargs): # real signature unknown
    pass

def write_channel(*args, **kwargs): # real signature unknown
    pass

# no classes
# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fb820afa0b8>'

__spec__ = None # (!) real value is "ModuleSpec(name='hpmudext', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fb820afa0b8>, origin='/usr/lib/python3/dist-packages/hpmudext.cpython-35m-x86_64-linux-gnu.so')"

