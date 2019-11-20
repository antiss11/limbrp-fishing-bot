import keyPress
import keyboard
import time

hotkb_pro_up = "alt+6"
hotkb_pro_down = "alt+5"


class Inventory:

    def put_in_car(self):
        pressGrave()
        time.sleep(0.3)
        pressUp()
        time.sleep(0.3)
        pressEnter()
        time.sleep(0.3)
        pressEnter()
        time.sleep(0.3)
        pressDown()
        time.sleep(0.3)
        pressEnter()
        time.sleep(0.3)
        pressUp()
        time.sleep(0.3)
        pressEnter()
        time.sleep(0.3)
        pressFive()
        time.sleep(0.3)
        pressTab()
        time.sleep(0.3)
        pressGrave()
        time.sleep(0.3)
        pressBackspace()

    def take_from_car(self):
        pressGrave()
        time.sleep(0.3)
        pressUp()
        time.sleep(0.3)
        pressEnter()
        time.sleep(0.3)
        pressEnter()
        time.sleep(0.3)
        pressEnter()
        time.sleep(0.3)
        pressDown()
        time.sleep(0.3)
        pressEnter()
        time.sleep(0.3)
        pressEight()
        time.sleep(0.3)
        pressTab()
        time.sleep(0.3)
        pressBackspace()
        time.sleep(0.3)
        pressBackspace()
        time.sleep(0.3)
        pressBackspace()


def pressEnter():
    keyPress.PressKey(keyPress.RETURN)
    time.sleep(0.05)
    keyPress.ReleaseKey(keyPress.RETURN)

def pressBackspace():
    time.sleep(0.2)
    keyPress.PressKey(keyPress.BACKSPACE)
    time.sleep(0.05)
    keyPress.ReleaseKey(keyPress.BACKSPACE)


def pressOne():
    keyPress.PressKey(keyPress.ONE)
    time.sleep(0.05)
    keyPress.ReleaseKey(keyPress.ONE)

def pressZero():
    keyPress.PressKey(keyPress.ZERO)
    time.sleep(0.05)
    keyPress.ReleaseKey(keyPress.ZERO)

def pressTwo():
    keyPress.PressKey(keyPress.TWO)
    time.sleep(0.05)
    keyPress.ReleaseKey(keyPress.TWO)

def pressFive():
    keyPress.PressKey(keyPress.FIVE)
    time.sleep(0.05)
    keyPress.ReleaseKey(keyPress.FIVE)

def pressTab():
    keyPress.PressKey(keyPress.TAB)
    time.sleep(0.05)
    keyPress.ReleaseKey(keyPress.TAB)

def pressComma():
    keyPress.PressKey(keyPress.COMMA)
    time.sleep(0.05)
    keyPress.ReleaseKey(keyPress.COMMA)

def pressFour():
    keyPress.PressKey(keyPress.FOUR)
    time.sleep(0.05)
    keyPress.ReleaseKey(keyPress.FOUR)

def pressEight():
    keyPress.PressKey(keyPress.EIGHT)
    time.sleep(0.05)
    keyPress.ReleaseKey(keyPress.EIGHT)

def pressGrave():
    keyPress.PressKey(keyPress.GRAVE)
    time.sleep(0.05)
    keyPress.ReleaseKey(keyPress.GRAVE)

def pressDown():
    keyboard.press_and_release(hotkb_pro_down)
    time.sleep(0.05)

def pressUp():
    keyboard.press_and_release(hotkb_pro_up)
    time.sleep(0.05)
