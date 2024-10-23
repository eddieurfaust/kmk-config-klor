from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys

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
]
# fmt: on

if __name__ == "__main__":
    keyboard.go()
