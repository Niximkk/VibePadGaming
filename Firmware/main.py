import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC

from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys
from kmk.handlers.sequences import send_string, simple_key_sequence

from kmk.extensions.rgb import RGB
from kmk.extensions.rgb import AnimationModes

import time

keyboard = KMKKeyboard()

layers = Layers()
keyboard.modules.append(layers)

keyboard.extensions.append(MediaKeys())

PINS = (board.D3, board.D4, board.D2, board.D1)

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)

# Layers
BASE = 0
DISCORD = 1
GAME = 2
MEDIA = 3
LED = 4

rgb = RGB(
    pixel_pin=board.D10,
    num_pixels=2,
    val_default=40,
    val_limit=100,
)
keyboard.extensions.append(rgb)

rgb_mode = 0  # 0 = layer, 1 = fade, 2 = off

layer_colors = {
    BASE: (0, 255, 0),
    DISCORD: (114, 137, 218),
    GAME: (255, 0, 0),
    MEDIA: (255, 200, 0),
    LED: (0, 255, 255),
}

def update_leds():
    global rgb_mode

    if rgb_mode == 0:  # Layer mode
        rgb.animation_mode = AnimationModes.STATIC
        cur = keyboard.active_layers[0]
        r, g, b = layer_colors.get(cur, (0, 0, 0))
        rgb.set_all(r, g, b)

    elif rgb_mode == 1:  # Fade
        rgb.animation_mode = AnimationModes.BREATHING_RAINBOW

    elif rgb_mode == 2:  # OFF
        rgb.animation_mode = AnimationModes.STATIC
        rgb.set_all(0, 0, 0)

DISCORD_MUTE = simple_key_sequence((KC.LCTL(KC.LSFT(KC.M)),))
DISCORD_DEAFEN = simple_key_sequence((KC.LCTL(KC.LSFT(KC.D)),))
DISCORD_STREAM = simple_key_sequence((KC.LCTL(KC.LSFT(KC.S)),))

shift_held = False
ctrl_held = False
mouse_down = False
previous_layer = BASE

def reset_game_modifiers():
    global shift_held, ctrl_held, mouse_down
    
    if shift_held:
        keyboard.send_key(KC.LSFT, pressed=False)
        shift_held = False
    if ctrl_held:
        keyboard.send_key(KC.LCTL, pressed=False)
        ctrl_held = False
    mouse_down = False

def game_layer_handler(keyboard, key, pressed, *args):
    global shift_held, ctrl_held, mouse_down

    if keyboard.active_layers[0] != GAME:
        return True

    if key == 0 and pressed:
        if not shift_held:
            keyboard.send_key(KC.LSFT, pressed=True)
            shift_held = True
        else:
            keyboard.send_key(KC.LSFT, pressed=False)
            shift_held = False
        return False

    if key == 1 and pressed:
        if not ctrl_held:
            keyboard.send_key(KC.LCTL, pressed=True)
            ctrl_held = True
        else:
            keyboard.send_key(KC.LCTL, pressed=False)
            ctrl_held = False
        return False

    if key == 2:
        mouse_down = pressed
        return False

    return True

keyboard.before_matrix_scan.append(game_layer_handler)

def autoclick_loop(keyboard):
    global mouse_down

    if mouse_down and keyboard.active_layers[0] == GAME:
        keyboard.send_key(KC.MB_LMB, pressed=True)
        time.sleep(0.015)
        keyboard.send_key(KC.MB_LMB, pressed=False)

keyboard.before_matrix_scan.append(autoclick_loop)

def led_layer_handler(keyboard, key, pressed, *args):
    global rgb_mode

    if pressed and keyboard.active_layers[0] == LED:

        if key == 0:  # Layer mode
            rgb_mode = 0
            update_leds()
            return False

        elif key == 1:  # Fade
            rgb_mode = 1
            update_leds()
            return False

        elif key == 2:  # Off
            rgb_mode = 2
            update_leds()
            return False

    return True

keyboard.before_matrix_scan.append(led_layer_handler)

def layer_change_handler(keyboard):
    global previous_layer
    
    current_layer = keyboard.active_layers[0]
    
    if previous_layer == GAME and current_layer != GAME:
        reset_game_modifiers()
    
    if rgb_mode == 0:
        update_leds()
    
    previous_layer = current_layer

keyboard.after_hid_send.append(layer_change_handler)

keyboard.keymap = [
    [
        KC.TO(DISCORD),   # Discord Layer
        KC.TO(GAME),      # Game Layer
        KC.TO(MEDIA),     # Media Layer
        KC.TO(LED),       # LED Layer
    ],

    [
        DISCORD_MUTE,     # Mute
        DISCORD_DEAFEN,   # Deafen
        DISCORD_STREAM,   # Start/Stop Stream
        KC.TO(BASE),
    ],

    [
        KC.NO,            # Toggle SHIFT
        KC.NO,            # Toggle CTRL
        KC.NO,            # AutoClick
        KC.TO(BASE),
    ],

    [
        KC.MPLY,          # Play/Pause
        KC.MNXT,          # Next Track
        KC.MPRV,          # Previous Track
        KC.TO(BASE),
    ],

    # LED
    [
        KC.NO,            # Layer Mode
        KC.NO,            # Fade Mode
        KC.NO,            # Off
        KC.TO(BASE),
    ],
]

if __name__ == "__main__":
    update_leds()
    keyboard.go()