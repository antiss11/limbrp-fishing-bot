import keyPress
import keyboard
import time

hotkb_pro_up = "alt+6"
hotkp_pro_down = "alt+5"


def pressEnter():
    keyPress.PressKey(keyPress.RETURN)
    time.sleep(0.2)
    keyPress.ReleaseKey(keyPress.RETURN)

def pressBackspace():
    keyPress.PressKey(keyPress.BACKSPACE)
    time.sleep(0.2)
    keyPress.ReleaseKey(keyPress.BACKSPACE)

def pressOne():
    keyPress.PressKey(keyPress.ONE)
    time.sleep(0.2)
    keyPress.ReleaseKey(keyPress.ONE)

def pressZero():
    keyPress.PressKey(keyPress.ZERO)
    time.sleep(0.2)
    keyPress.ReleaseKey(keyPress.ZERO)

def pressTwo():
    keyPress.PressKey(keyPress.TWO)
    time.sleep(0.2)
    keyPress.ReleaseKey(keyPress.TWO)

def pressFive():
    keyPress.PressKey(keyPress.FIVE)
    time.sleep(0.2)
    keyPress.ReleaseKey(keyPress.FIVE)

def pressTab():
    keyPress.PressKey(keyPress.TAB)
    time.sleep(0.2)
    keyPress.ReleaseKey(keyPress.TAB)

def pressComma():
    keyPress.PressKey(keyPress.COMMA)
    time.sleep(0.2)
    keyPress.ReleaseKey(keyPress.COMMA)

def pressFour():
    keyPress.PressKey(keyPress.FOUR)
    time.sleep(0.2)
    keyPress.ReleaseKey(keyPress.FOUR)

def pressGrave():
    keyPress.PressKey(keyPress.GRAVE)
    time.sleep(0.2)
    keyPress.ReleaseKey(keyPress.GRAVE)

def pressDown():
    time.sleep(0.2)
    keyboard.press_and_release(hotkp_pro_down)
    time.sleep(0.2)
def pressUp():
    time.sleep(0.2)
    keyboard.press_and_release(hotkb_pro_up)
    time.sleep(0.2)

def put_in_car():
    pressGrave()
    time.sleep(1)
    print(2)
    pressUp()
    time.sleep(1)
    pressEnter()
    time.sleep(1)
    pressEnter()
    time.sleep(1)
    pressDown()
    time.sleep(1)
    pressEnter()
    time.sleep(1)
    pressUp()
    time.sleep(1)
    pressEnter()
    time.sleep(1)
    pressFive()
    time.sleep(1)
    pressTab()
    time.sleep(1)
    pressBackspace()


def take_from_car():
    pressGrave()
    time.sleep(5)
    pressUp()
    time.sleep(5)
    pressEnter()
    time.sleep(5)
    pressEnter()
    time.sleep(5)
    pressEnter()
    time.sleep(5)
    pressDown()
    time.sleep(5)
    pressEnter()
    time.sleep(5)
    pressFour()
    time.sleep(5)
    pressTab()
    time.sleep(0.5)
    pressBackspace()

