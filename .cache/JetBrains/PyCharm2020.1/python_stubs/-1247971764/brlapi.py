# encoding: utf-8
# module brlapi
# from /usr/lib/python3/dist-packages/brlapi.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
"""
This module implements a set of bindings for BrlAPI, a braille bridge for applications.

The reference C API documentation is available online http://brltty.com/doc/BrlAPIref-HTML, as well as in manual pages.

This documentation is only a python helper, you should also read C manual pages.

Example : 
import brlapi
import errno
import Xlib.keysymdef.miscellany
try:
  b = brlapi.Connection()
  b.enterTtyMode()
  b.ignoreKeys(brlapi.rangeType_all,[0])

  # Accept the home, window up and window down braille commands
  b.acceptKeys(brlapi.rangeType_command,[brlapi.KEY_TYPE_CMD|brlapi.KEY_CMD_HOME, brlapi.KEY_TYPE_CMD|brlapi.KEY_CMD_WINUP, brlapi.KEY_TYPE_CMD|brlapi.KEY_CMD_WINDN])

  # Accept the tab key
  b.acceptKeys(brlapi.rangeType_key,[brlapi.KEY_TYPE_SYM|Xlib.keysymdef.miscellany.XK_Tab])

  b.writeText("Press home, winup/dn or tab to continue ... ¤")
  key = b.readKey()

  k = b.expandKeyCode(key)
  b.writeText("Key %ld (%x %x %x %x) !" % (key, k["type"], k["command"], k["argument"], k["flags"]))
  b.writeText(None,1)
  b.readKey()

  underline = chr(brlapi.DOT7 + brlapi.DOT8)
  # Note: center() can take two arguments only starting from python 2.4
  b.write(
      regionBegin = 1,
      regionSize = 40,
      text = "Press any key to exit ¤                 ",
      orMask = "".center(21,underline) + "".center(19,chr(0)))

  b.acceptKeys(brlapi.rangeType_all,[0])
  b.readKey()

  b.leaveTtyMode()

except brlapi.ConnectionError as e:
  if e.brlerrno == brlapi.ERROR_CONNREFUSED:
    print "Connection to %s refused. BRLTTY is too busy..." % e.host
  elif e.brlerrno == brlapi.ERROR_AUTHENTICATION:
    print "Authentication with %s failed. Please check the permissions of %s" % (e.host,e.auth)
  elif e.brlerrno == brlapi.ERROR_LIBCERR and (e.libcerrno == errno.ECONNREFUSED or e.libcerrno == errno.ENOENT):
    print "Connection to %s failed. Is BRLTTY really running?" % (e.host)
  else:
    print "Connection to BRLTTY at %s failed: " % (e.host)
  print(e)
  print(e.brlerrno)
  print(e.libcerrno)
"""

# imports
import builtins as __builtins__ # <module 'builtins' (built-in)>
import errno as errno # <module 'errno' (built-in)>

# Variables with simple values

CURSOR_LEAVE = -1
CURSOR_OFF = 0

DISPLAY_DEFAULT = -1

DOT1 = 1
DOT2 = 2
DOT3 = 4
DOT4 = 8
DOT5 = 16
DOT6 = 32
DOT7 = 64
DOT8 = 128
DOTC = 256

ERROR_AUTHENTICATION = 17
ERROR_CONNREFUSED = 8
ERROR_DEVICEBUSY = 3
ERROR_DRIVERERROR = 16
ERROR_EMPTYKEY = 15
ERROR_EOF = 14
ERROR_GAIERR = 10

ERROR_ILLEGAL_INSTRUCTION = 5

ERROR_INVALID_PACKET = 7
ERROR_INVALID_PARAMETER = 6

ERROR_LIBCERR = 11
ERROR_NOMEM = 1
ERROR_OPNOTSUPP = 9

ERROR_PROTOCOL_VERSION = 13

ERROR_SUCCESS = 0
ERROR_TTYBUSY = 2
ERROR_UNKNOWNTTY = 12

ERROR_UNKNOWN_INSTRUCTION = 4

KEY_CMD_ALERT = 2031616
KEY_CMD_ALTGR = 112
KEY_CMD_APNDCHARS = 1114112

KEY_CMD_ARG_MASK = 65535
KEY_CMD_ARG_SHIFT = 0

KEY_CMD_ASPK_CMP_WORDS = 88

KEY_CMD_ASPK_DEL_CHARS = 86

KEY_CMD_ASPK_INS_CHARS = 85

KEY_CMD_ASPK_REP_CHARS = 87

KEY_CMD_ASPK_SEL_CHAR = 84
KEY_CMD_ASPK_SEL_LINE = 83

KEY_CMD_ATTRBLINK = 44
KEY_CMD_ATTRDN = 8
KEY_CMD_ATTRUP = 7
KEY_CMD_ATTRVIS = 43
KEY_CMD_AUTOREPEAT = 47
KEY_CMD_AUTOSPEAK = 48
KEY_CMD_BACK = 30

KEY_CMD_BLK_MASK = 536805376
KEY_CMD_BLK_SHIFT = 16

KEY_CMD_BOT = 10

KEY_CMD_BOT_LEFT = 12

KEY_CMD_BRLKBD = 110
KEY_CMD_BRLUCDOTS = 109

KEY_CMD_BRL_START = 115
KEY_CMD_BRL_STOP = 114

KEY_CMD_CAPBLINK = 45
KEY_CMD_CHRLT = 19
KEY_CMD_CHRRT = 20

KEY_CMD_CLIP_ADD = 196608
KEY_CMD_CLIP_APPEND = 1114112
KEY_CMD_CLIP_COPY = 1048576
KEY_CMD_CLIP_NEW = 131072
KEY_CMD_CLIP_RESTORE = 108
KEY_CMD_CLIP_SAVE = 107

KEY_CMD_CONTEXT = 2490368
KEY_CMD_CONTROL = 79
KEY_CMD_COPYCHARS = 1048576

KEY_CMD_COPY_LINE = 327680
KEY_CMD_COPY_RECT = 262144

KEY_CMD_CSRBLINK = 42
KEY_CMD_CSRHIDE = 39

KEY_CMD_CSRJMP_VERT = 72

KEY_CMD_CSRSIZE = 41
KEY_CMD_CSRTRK = 40
KEY_CMD_CSRVIS = 38
KEY_CMD_CUTAPPEND = 196608
KEY_CMD_CUTBEGIN = 131072
KEY_CMD_CUTLINE = 327680
KEY_CMD_CUTRECT = 262144
KEY_CMD_DESCCHAR = 589824

KEY_CMD_DESC_CURR_CHAR = 102

KEY_CMD_DISPMD = 33
KEY_CMD_FREEZE = 32
KEY_CMD_FWINLT = 23
KEY_CMD_FWINLTSKIP = 25
KEY_CMD_FWINRT = 24
KEY_CMD_FWINRTSKIP = 26
KEY_CMD_GOTOLINE = 851968
KEY_CMD_GOTOMARK = 786432
KEY_CMD_GUI = 113
KEY_CMD_HELP = 49
KEY_CMD_HOME = 29
KEY_CMD_HWINLT = 21
KEY_CMD_HWINRT = 22
KEY_CMD_INFO = 50
KEY_CMD_LEARN = 51
KEY_CMD_LNBEG = 27
KEY_CMD_LNDN = 2
KEY_CMD_LNEND = 28
KEY_CMD_LNUP = 1

KEY_CMD_MENU_FIRST_ITEM = 55

KEY_CMD_MENU_LAST_ITEM = 56

KEY_CMD_MENU_NEXT_ITEM = 58
KEY_CMD_MENU_NEXT_SETTING = 60

KEY_CMD_MENU_PREV_ITEM = 57
KEY_CMD_MENU_PREV_LEVEL = 82
KEY_CMD_MENU_PREV_SETTING = 59

KEY_CMD_META = 80
KEY_CMD_MUTE = 61
KEY_CMD_NOOP = 0
KEY_CMD_NXDIFCHAR = 983040
KEY_CMD_NXDIFLN = 6
KEY_CMD_NXINDENT = 524288
KEY_CMD_NXNBWIN = 123
KEY_CMD_NXPGRPH = 14
KEY_CMD_NXPROMPT = 16
KEY_CMD_NXSEARCH = 18
KEY_CMD_OFFLINE = 76
KEY_CMD_PASSAT = 2293760
KEY_CMD_PASSDOTS = 2228224
KEY_CMD_PASSPS2 = 2424832
KEY_CMD_PASSXT = 2359296
KEY_CMD_PASTE = 73

KEY_CMD_PASTE_HISTORY = 1179648

KEY_CMD_PRDIFCHAR = 917504
KEY_CMD_PRDIFLN = 5
KEY_CMD_PREFLOAD = 54
KEY_CMD_PREFMENU = 52
KEY_CMD_PREFSAVE = 53
KEY_CMD_PRINDENT = 458752
KEY_CMD_PRNBWIN = 122
KEY_CMD_PRPGRPH = 13
KEY_CMD_PRPROMPT = 15
KEY_CMD_PRSEARCH = 17
KEY_CMD_RESTARTBRL = 74
KEY_CMD_RESTARTSPEECH = 75
KEY_CMD_RETURN = 31
KEY_CMD_ROUTE = 65536

KEY_CMD_ROUTE_CURR_LOCN = 104

KEY_CMD_SAY_ABOVE = 64
KEY_CMD_SAY_BELOW = 65
KEY_CMD_SAY_FASTER = 67
KEY_CMD_SAY_LINE = 63
KEY_CMD_SAY_LOUDER = 69
KEY_CMD_SAY_SLOWER = 66
KEY_CMD_SAY_SOFTER = 68

KEY_CMD_SCR_START = 119
KEY_CMD_SCR_STOP = 118

KEY_CMD_SELECTVT = 1966080

KEY_CMD_SELECTVT_NEXT = 121
KEY_CMD_SELECTVT_PREV = 120

KEY_CMD_SETLEFT = 655360
KEY_CMD_SETMARK = 720896

KEY_CMD_SET_ATTRIBUTES_TABLE = 1310720

KEY_CMD_SET_CONTRACTION_TABLE = 1376256

KEY_CMD_SET_KEYBOARD_TABLE = 1441792

KEY_CMD_SET_LANGUAGE_PROFILE = 1507328

KEY_CMD_SET_TEXT_TABLE = 1245184

KEY_CMD_SHIFT = 77

KEY_CMD_SHOW_CURR_LOCN = 106

KEY_CMD_SIXDOTS = 34
KEY_CMD_SKPBLNKWINS = 37
KEY_CMD_SKPIDLNS = 36
KEY_CMD_SLIDEWIN = 35

KEY_CMD_SPEAK_CURR_CHAR = 89
KEY_CMD_SPEAK_CURR_LINE = 95
KEY_CMD_SPEAK_CURR_LOCN = 105
KEY_CMD_SPEAK_CURR_WORD = 92

KEY_CMD_SPEAK_FRST_CHAR = 98
KEY_CMD_SPEAK_FRST_LINE = 100

KEY_CMD_SPEAK_LAST_CHAR = 99
KEY_CMD_SPEAK_LAST_LINE = 101

KEY_CMD_SPEAK_NEXT_CHAR = 91
KEY_CMD_SPEAK_NEXT_LINE = 97
KEY_CMD_SPEAK_NEXT_WORD = 94

KEY_CMD_SPEAK_PREV_CHAR = 90
KEY_CMD_SPEAK_PREV_LINE = 96
KEY_CMD_SPEAK_PREV_WORD = 93

KEY_CMD_SPELL_CURR_WORD = 103

KEY_CMD_SPKHOME = 62

KEY_CMD_SPK_START = 117
KEY_CMD_SPK_STOP = 116

KEY_CMD_SWITCHVT = 393216

KEY_CMD_SWITCHVT_NEXT = 71
KEY_CMD_SWITCHVT_PREV = 70

KEY_CMD_TIME = 81
KEY_CMD_TOP = 9

KEY_CMD_TOP_LEFT = 11

KEY_CMD_TOUCH_AT = 2555904
KEY_CMD_TOUCH_NAV = 124

KEY_CMD_TUNES = 46
KEY_CMD_UNSTICK = 111
KEY_CMD_UPPER = 78
KEY_CMD_WINDN = 4
KEY_CMD_WINUP = 3

KEY_CODE_MASK = 536870911
KEY_CODE_SHIFT = 0

KEY_FLAGS_MASK = 18446744069414584320
KEY_FLAGS_SHIFT = 32

KEY_FLG_INPUT_ALTGR = 4096
KEY_FLG_INPUT_CONTROL = 1024
KEY_FLG_INPUT_GUI = 8192
KEY_FLG_INPUT_META = 2048
KEY_FLG_INPUT_SHIFT = 256
KEY_FLG_INPUT_UPPER = 512

KEY_FLG_KBD_EMUL0 = 512
KEY_FLG_KBD_EMUL1 = 1024
KEY_FLG_KBD_RELEASE = 256

KEY_FLG_MOTION_ROUTE = 1024
KEY_FLG_MOTION_SCALED = 2048
KEY_FLG_MOTION_TOLEFT = 4096

KEY_FLG_TOGGLE_MASK = 768
KEY_FLG_TOGGLE_OFF = 512
KEY_FLG_TOGGLE_ON = 256

KEY_MAX = 18446744073709551615

KEY_SYM_BACKSPACE = 65288
KEY_SYM_DELETE = 65535
KEY_SYM_DOWN = 65364
KEY_SYM_END = 65367
KEY_SYM_ESCAPE = 65307
KEY_SYM_F1 = 65470
KEY_SYM_F10 = 65479
KEY_SYM_F11 = 65480
KEY_SYM_F12 = 65481
KEY_SYM_F13 = 65482
KEY_SYM_F14 = 65483
KEY_SYM_F15 = 65484
KEY_SYM_F16 = 65485
KEY_SYM_F17 = 65486
KEY_SYM_F18 = 65487
KEY_SYM_F19 = 65488
KEY_SYM_F2 = 65471
KEY_SYM_F20 = 65489
KEY_SYM_F21 = 65490
KEY_SYM_F22 = 65491
KEY_SYM_F23 = 65492
KEY_SYM_F24 = 65493
KEY_SYM_F25 = 65494
KEY_SYM_F26 = 65495
KEY_SYM_F27 = 65496
KEY_SYM_F28 = 65497
KEY_SYM_F29 = 65498
KEY_SYM_F3 = 65472
KEY_SYM_F30 = 65499
KEY_SYM_F31 = 65500
KEY_SYM_F32 = 65501
KEY_SYM_F33 = 65502
KEY_SYM_F34 = 65503
KEY_SYM_F35 = 65504
KEY_SYM_F4 = 65473
KEY_SYM_F5 = 65474
KEY_SYM_F6 = 65475
KEY_SYM_F7 = 65476
KEY_SYM_F8 = 65477
KEY_SYM_F9 = 65478
KEY_SYM_HOME = 65360
KEY_SYM_INSERT = 65379
KEY_SYM_LEFT = 65361
KEY_SYM_LINEFEED = 65293

KEY_SYM_PAGE_DOWN = 65366
KEY_SYM_PAGE_UP = 65365

KEY_SYM_RIGHT = 65363
KEY_SYM_TAB = 65289
KEY_SYM_UNICODE = 16777216
KEY_SYM_UP = 65362

KEY_TYPE_CMD = 536870912
KEY_TYPE_MASK = 3758096384
KEY_TYPE_SHIFT = 29
KEY_TYPE_SYM = 0

rangeType_all = 0
rangeType_code = 4
rangeType_command = 2
rangeType_key = 3
rangeType_type = 1

TTY_DEFAULT = -1

# no functions
# classes

class Connection(object):
    """ Class which manages the bridge between your program and BrlAPI """
    def acceptAllKeys(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Accept all key presses from the braille keyboard.
        		See brlapi_acceptAllKeys(3).
        		
        		This function asks the server to give all keys to the application, and not give them to brltty.
        
        		Warning: after calling this function, make sure to call brlapi_ignoreKeys() for ignoring important keys like BRL_CMD_SWITCHVT_PREV/NEXT and such.
        """
        pass

    def acceptKeyRanges(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Accept some key presses from the braille keyboard.
        		See brlapi_acceptKeyRanges(3).
        		
        		This function asks the server to return the provided key ranges (inclusive) to the application, and not give them to brltty.
        		
        		The given codes should be raw keycodes (i.e. some driver name was given to brlapi_enterTtyMode())
        """
        pass

    def acceptKeys(self, *args, **kwargs): # real signature unknown
        """
        Accept some key presses from the braille keyboard.
        		See brlapi_ignoreKeys(3).
        		
        		This function asks the server to give the provided keys to the application, and not give them to brltty.
        
        		The given codes should be brltty commands (nul or "" was given to brlapi_enterTtyMode())
        """
        pass

    def enterRawMode(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Switch to Raw mode
        		See brlapi_enterRawMode(3).
        		
        		* driver : Specifies the name of the driver for which the raw communication will be established
        """
        pass

    def enterTtyMode(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Ask for some tty, with some key mechanism
        
        		See brlapi_enterTtyMode(3).
        
        		* tty : If tty >= 0, application takes control of the specified tty
        			If tty == TTY_DEFAULT, the library first tries to get the tty number from the WINDOWID environment variable (form xterm case), then the CONTROLVT variable, and at last reads /proc/self/stat (on linux)
        		* driver : Tells how the application wants readKey() to return key presses. None or "" means BrlTTY commands are required, whereas a driver name means that raw key codes returned by this driver are expected.
        """
        pass

    def enterTtyModeWithPath(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Ask for some tty, with some key mechanism
        
        		See brlapi_enterTtyModeWithPath(3).
        
        		* tty is an array of ttys representing the tty path to be got. Can be None.
        		* driver : has the same meaning as in enterTtyMode.
        		
        		Providing an empty array or None means to get the root.
        """
        pass

    def expandKeyCode(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Expand a keycode into its individual components.
        		See brlapi_expandKeyCode(3).
        """
        pass

    def ignoreAllKeys(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Ignore all key presses from the braille keyboard.
        		See brlapi_ignoreAllKeys(3).
        		
        		This function asks the server to give all keys to brltty, rather than returning them to the application via brlapi_readKey().
        """
        pass

    def ignoreKeyRanges(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Ignore some key presses from the braille keyboard.
        		See brlapi_ignoreKeyRanges(3).
        		
        		This function asks the server to give the provided key ranges to brltty, rather than returning them to the application via brlapi_readKey().
        		
        		The given codes should be raw keycodes (i.e. some driver name was given to brlapi_enterTtyMode())
        """
        pass

    def ignoreKeys(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Ignore some key presses from the braille keyboard.
        		See brlapi_ignoreKeys(3).
        		
        		This function asks the server to give the provided keys to brltty, rather than returning them to the application via brlapi_readKey().
        		
        		The given codes should be brltty commands (nul or "" was given to brlapi_enterTtyMode())
        """
        pass

    def leaveRawMode(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        leave Raw mode
        		See brlapi_leaveRawMode(3).
        """
        pass

    def leaveTtyMode(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Stop controlling the tty
        		See brlapi_leaveTtyMode(3).
        """
        pass

    def readKey(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Read a key from the braille keyboard.
        		See brlapi_readKey(3).
        
        		This function returns one key press's code.
        
        		If None or "" was given to enterTtyPath(), a brltty command is returned. It is hence pretty driver-independent, and should be used by default when no other option is possible.
        
        		By default, all commands but those which restart drivers and switch virtual are returned to the application and not to brltty. If the application doesn't want to see some command events, it should call either ignoreKeys() or ignoreKeyRanges().
        
        		If some driver name was given to enterTtyMode(), a raw keycode is returned, as specified by the terminal driver. It generally corresponds to the very code that the terminal tells to the driver. This should only be used by applications which are dedicated to a particular braille terminal. Hence, checking the terminal type thanks to a call to drivername before getting tty control is a pretty good idea.
        
        		By default, all the keypresses will be passed to the client, none will go through brltty, so the application will have to handle console switching itself for instance.
        """
        pass

    def setFocus(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Tell the current tty to brltty.
        		See brlapi_setFocus(3).
        		This is intended for focus tellers, such as brltty, xbrlapi, screen, ... enterTtyMode() must have been called before hand to tell where this focus applies in the tty tree.
        """
        pass

    def write(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Update a specific region of the braille display and apply and/or masks.
        		See brlapi_write(3).
        		* s : gives information necessary for the update
        """
        pass

    def writeDots(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Write the given dots array to the display.
        		See brlapi_writeDots(3).
        		* dots : points on an array of dot information, one per character. Its size must hence be the same as what displaysize provides.
        """
        pass

    def writeText(self, *args, **kwargs): # real signature unknown
        """ Write the given """
        pass

    def __del__(self, *args, **kwargs): # real signature unknown
        """ Close the BrlAPI conection """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
        """
        Connect your program to BrlTTY using settings
        
        		See brlapi_openConnection(3)
        		
        		Setting host to None defaults it to localhost, using the local installation's default TCP port, or to the content of the BRLAPI_HOST environment variable, if it exists.
        		Note: Please check that resolving this name works before complaining.
        
        		Setting auth to None defaults it to local installation setup or to the content of the BRLAPI_AUTH environment variable, if it exists.
        """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    auth = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """This tells where the BrlAPI server resides : it might be listening on another computer, on any TCP port. It should look like "foo:1", which means TCP port number BRLAPI_SOCKETPORTNUM+1 on computer called "foo"."""

    displaySize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the size of the braille display
		See brlapi_getDisplaySize(3)."""

    driverName = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Get the complete name of the driver used by BrlTTY
		See brlapi_getDriverName(3)."""

    fileDescriptor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Returns the Unix file descriptor that the connection uses"""

    host = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """To get authorized to connect, libbrlapi has to tell the BrlAPI server a secret key, for security reasons. This is the path to the file which holds it; it will hence have to be readable by the application."""



class OperationError(Exception):
    """ Error while performing some operation """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""



class ConnectionError(OperationError):
    """ Error while connecting to BrlTTY """
    def auth(self, *args, **kwargs): # real signature unknown
        """ Authentication method used """
        pass

    def host(self, *args, **kwargs): # real signature unknown
        """ Host of BRLTTY server """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        pass


class WriteStruct(object):
    """
    Structure containing arguments to be given to Connection.write()
    	See brlapi_writeArguments_t(3).
    	
    	This is DEPRECATED. Use the named parameters of write() instead.
    """
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    attrAnd = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """And attributes; applied first"""

    attrOr = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Or attributes; applied after ANDing"""

    charset = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Character set of the text"""

    cursor = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """CURSOR_LEAVE == don't touch, CURSOR_OFF == turn off, 1 = 1st char of display, ..."""

    displayNumber = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Display number DISPLAY_DEFAULT == unspecified"""

    regionBegin = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Region of display to update, 1st character of display is 1"""

    regionSize = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Number of characters held in text, attrAnd and attrOr. For multibytes text, this is the number of multibyte characters. Combining and double-width characters count for 1"""

    text = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Text to display"""



# variables with complex values

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7fb820afaa20>'

__spec__ = None # (!) real value is "ModuleSpec(name='brlapi', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7fb820afaa20>, origin='/usr/lib/python3/dist-packages/brlapi.cpython-35m-x86_64-linux-gnu.so')"

__test__ = {}

