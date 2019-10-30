import keyPress
import keyboard
import time

hotkb_pro_up = "alt+6"
hotkp_pro_down = "alt+5"


def pressEnter():
    keyPress.PressKey(keyPress.RETURN)
    time.sleep(0.2)
    keyPress.ReleaseKey(keyPress.RETURN)


def pressComma():
    keyPress.PressKey(keyPress.COMMA)
    time.sleep(0.2)
    keyPress.ReleaseKey(keyPress.COMMA)


def pressGrave():
    keyPress.PressKey(keyPress.GRAVE)
    time.sleep(0.2)
    keyPress.ReleaseKey(keyPress.GRAVE)

def pressDown():
    keyboard.press_and_release(hotkp_pro_down)

def pressUp():
    keyboard.press_and_release(hotkb_pro_up)


class Menu:

    def __init__(self, menu_items_count):
        self.menu_items_count = menu_items_count


