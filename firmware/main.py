from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.modules.oneshot import OneShot

oneshot = OneShot()
# optional: set a custom tap timeout in ms (default: 1000ms)
# oneshot.tap_time = 1500

# fmt: off
# ↓ EDIT CONFIG HERE ↓
klor_variant = "saegewerk"  # Options: "polydactyl", "konrad", "yubitsume", "saegewerk"
klor_rgb = "none"           # Options: "basic_rgb", "peg_rgb", "none"
klor_oled = False           # Options: True, False
klor_speaker = False        # Options: True, False
# ↑ EDIT CONFIG HERE ↑
# fmt: on

keyboard = KMKKeyboard(klor_variant, klor_rgb, klor_oled, klor_speaker)

keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(oneshot)

combo_layers = {
    (3, 4): 5,
}
keyboard.modules.append(Layers(combo_layers))

# Enable debugging: http://kmkfw.io/docs/debugging/
# keyboard.debug_enabled = True


# Key aliases
xxxxxxx = KC.NO
_______ = KC.TRNS
RAISE = KC.MO(1)
LOWER = KC.MO(2)
NAV = KC.MO(3)
SYM = KC.MO(4)
NUM = KC.MO(5)

# More aliases
HK = KC.LSFT(KC.NUHS)  # HochKomma

SWPWN = KC.LALT(KC.TAB)  # Swap Window
TBL = KC.LSFT(KC.LCTL(KC.TAB))  # Tab Left
TBR = KC.LCTL(KC.TAB)  # Tab Left

OSG = KC.OS(KC.LGUI)  # Sticky Gui
OSA = KC.OS(KC.LALT)  # Sticky Alt
OSS = KC.OS(KC.LSFT)  # Sticky Shift
OSC = KC.OS(KC.LCTL)  # Sticky Control
OSGR = KC.OS(KC.LGUI)  # Sticky Gui (Right)
OSAR = KC.OS(KC.LALT)  # Sticky Alt (Right)
OSSR = KC.OS(KC.LSFT)  # Sticky Shift (Right)
OSCR = KC.OS(KC.LCTL)  # Sticky Control (Right)

DL = KC.OS(KC.LCTL(KC.LGUI(KC.LEFT)))  # Desktop Left
DR = KC.OS(KC.LCTL(KC.LGUI(KC.RIGHT)))  # Desktop Right
MEH = lambda x: KC.LCTL(KC.LSFT(KC.ALT(x)))  # noqa: E731
SRCH = KC.LCTL(KC.F)  # Search

# Symbol Layer
LPA = KC.LSFT(KC.N8)  # (
RPA = KC.LSFT(KC.N9)  # )
LBR = KC.RALT(KC.N8)  # [
RBR = KC.RALT(KC.N9)  # ]
LCB = KC.RALT(KC.N7)  # {
RCB = KC.RALT(KC.N0)  # }
TLD = KC.RALT(KC.RBRACKET)  # ~
CIRC = KC.GRAVE  # ^ (dead)
GRV = KC.LSFT(KC.EQUAL)  # ` (dead)

MIN = KC.SLASH  # -
AST = KC.LSFT(KC.RBRACKET)  # *
EQL = KC.LSFT(KC.N0)  # =
UND = KC.LSFT(KC.SLASH)  # _
DOL = KC.LSFT(KC.N4)  # $

HAS = KC.NUHS  # #

PLS = KC.RBRACKET  # +
PIP = KC.RALT(KC.NONUS_BSLASH)  # |
ATT = KC.RALT(KC.Q)  # @
SLSH = KC.LSFT(KC.N7)  # /
PERC = KC.LSFT(KC.N5)  # %
DQT = KC.LSFT(KC.N2)  # "
BSLS = KC.RALT(KC.MINUS)  # \
AMPR = KC.LSFT(KC.N6)  # &
QUES = KC.LSFT(KC.MINUS)  # ?
EXLM = KC.EXCLAIM  # !

# Keymap
# fmt: off
keyboard.keymap = [
    [
       #BASE
       #     |        |        |        |        |        |        | |        |        |        |        |        |        |        |
                  KC.W,    KC.F,    KC.M,    KC.P,    KC.V,                        HK,    KC.DOT, xxxxxxx,    KC.Y, xxxxxxx,         \
        KC.N1,    KC.R,    KC.S,    KC.N,    KC.T,    KC.B,                        KC.COMM, KC.A,    KC.E,    KC.I, KC.H, KC.N1,  \
        KC.N2,    KC.X,    KC.C,    KC.L,    KC.D,    KC.G, KC.MUTE,   KC.MPLY,    xxxxxxx, KC.U,    KC.O,    KC.Z, KC.K, KC.N2,  \
                        NAV,   KC.LSFT,  xxxxxxx,   KC.N4,                       KC.N4, xxxxxxx, KC.SPC,    SYM,

        # Encoders
        KC.AUDIO_VOL_UP,      #Left side clockwise
        KC.AUDIO_VOL_DOWN,    #Left side counterclockwise
        KC.MEDIA_NEXT_TRACK,  #Right side clockwise
        KC.MEDIA_PREV_TRACK,  #Right side counterclockwise
    ],
    [
       #RAISE
       #     |        |        |        |        |        |        | |        |        |        |        |        |        |        |
                 KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                       KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,           \
      _______,  KC.TAB, KC.LEFT, KC.DOWN,   KC.UP, KC.RGHT,                     xxxxxxx, KC.MINS,  KC.EQL, KC.LBRC, KC.RBRC, _______,  \
      _______, KC.LCTL,  KC.GRV, KC.LGUI, KC.LALT, xxxxxxx, KC.MUTE,   KC.MPLY, xxxxxxx, xxxxxxx, xxxxxxx, KC.BSLS, KC.QUOT, _______,  \
                        xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx,                     xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx,

        # Encoders
        KC.PGUP,  #Left side clockwise
        KC.PGDN,  #Left side counterclockwise
        KC.RIGHT, #Right side clockwise
        KC.LEFT,  #Right side counterclockwise
    ],
    [
       #LOWER
       #     |        |        |        |        |        |        | |        |        |        |        |        |        |        |
               KC.EXLM,   KC.AT, KC.HASH,  KC.DLR, KC.PERC,                     KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN,           \
      _______,  KC.ESC, xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx,                     xxxxxxx, KC.UNDS, KC.PLUS, KC.LBRC, KC.RBRC, _______,  \
      _______, KC.CAPS, KC.TILD, xxxxxxx, xxxxxxx, xxxxxxx, KC.MUTE,   KC.MPLY, xxxxxxx, xxxxxxx, xxxxxxx, KC.PIPE,  KC.DQT, _______,  \
                        xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx,                     xxxxxxx,  KC.ENT, xxxxxxx,  KC.DEL,

        # Encoders
        KC.AUDIO_VOL_UP,      #Left side clockwise
        KC.AUDIO_VOL_DOWN,    #Left side counterclockwise
        KC.MEDIA_NEXT_TRACK,  #Right side clockwise
        KC.MEDIA_PREV_TRACK,  #Right side counterclockwise
    ],
    [
       #NAV
       #     |        |        |        |        |        |        | |        |        |        |        |        |        |        |
                KC.TAB,   SWPWN,       TBL,     TBR, _______,                     _______, KC.HOME,   KC.UP,  KC.END,  KC.DEL,           \
      _______,     OSG,     OSA,       OSS,     OSC, _______,                     KC.LCAP, KC.LEFT, KC.DOWN, KC.RGHT, KC.BSPC, _______,  \
      _______,      DL,      DR, MEH(KC.N),    SRCH, _______, KC.MUTE,   KC.MPLY, _______, KC.PGDN, KC.PGUP, _______,  KC.ENT, _______,  \
                        _______, _______, _______, _______,                     _______,  _______, _______,  _______,

        # Encoders
        KC.AUDIO_VOL_UP,      #Left side clockwise
        KC.AUDIO_VOL_DOWN,    #Left side counterclockwise
        KC.MEDIA_NEXT_TRACK,  #Right side clockwise
        KC.MEDIA_PREV_TRACK,  #Right side counterclockwise
    ],
    [
       #SYM
       #     |        |        |        |        |        |        | |        |        |        |        |        |        |        |
                KC.ESC,     LCB,     LBR,     LPA,     TLD,                        CIRC,     RPA,     RBR,     RCB,     GRV,           \
      _______,     MIN,     AST,     EQL,     UND,     DOL,                         HAS,     OSC,     OSS,     OSA,     OSG, _______,  \
      _______,     PLS,     PIP,     ATT,    SLSH,    PERC, KC.MUTE,   KC.MPLY,     DQT,    BSLS,    AMPR,    QUES,    EXLM, _______,  \
                        xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx,                     xxxxxxx,  KC.ENT, xxxxxxx,  KC.DEL,

        # Encoders
        KC.AUDIO_VOL_UP,      #Left side clockwise
        KC.AUDIO_VOL_DOWN,    #Left side counterclockwise
        KC.MEDIA_NEXT_TRACK,  #Right side clockwise
        KC.MEDIA_PREV_TRACK,  #Right side counterclockwise
    ],
    [
       #NUM
       #     |        |        |        |        |        |        | |        |        |        |        |        |        |        |
                 KC.N7,   KC.N5,   KC.N3,   KC.N1,   KC.N9,                       KC.N8,   KC.N0,   KC.N2,   KC.N4,   KC.N6,           \
      _______,     OSG,     OSA,     OSS,     OSC,  KC.F11,                      KC.F10,    OSCR,    OSSR,    OSAR,    OSGR, _______,  \
      _______,   KC.F7,   KC.F5,   KC.F3,   KC.F1,   KC.F9,                       KC.F8,  KC.F12,   KC.F2,   KC.F4,   KC.F6,           \
                        xxxxxxx, xxxxxxx, xxxxxxx, xxxxxxx,                     xxxxxxx,  KC.ENT, xxxxxxx,  KC.DEL,

        # Encoders
        KC.AUDIO_VOL_UP,      #Left side clockwise
        KC.AUDIO_VOL_DOWN,    #Left side counterclockwise
        KC.MEDIA_NEXT_TRACK,  #Right side clockwise
        KC.MEDIA_PREV_TRACK,  #Right side counterclockwise
    ],
]
# fmt: on

if __name__ == "__main__":
    keyboard.go()
