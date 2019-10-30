import win32gui
import numpy as np
from PIL import ImageGrab
import cv2
import time
import keyPress


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
    keyPress.PressKey(keyPress.L_ALT)
    time.sleep(0.5)
    keyPress.PressKey(keyPress.KEY_5)
    keyPress.ReleaseKey(keyPress.L_ALT)
    keyPress.ReleaseKey(keyPress.KEY_5)

def pressUp():
    keyPress.PressKey(keyPress.UP)
    time.sleep(1)
    keyPress.ReleaseKey(keyPress.UP)

window_location = []
window_size = []


def callback(hwnd, extra):
    if 'FiveM' in win32gui.GetWindowText(hwnd):
        rect = win32gui.GetWindowRect(hwnd)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        window_location.append(x)
        window_location.append(y)
        window_size.append(w)
        window_size.append(h)


def main():
    win32gui.EnumWindows(callback, None)

    window_width = window_size[0]
    window_height = window_size[1]
    window_x = window_location[0]
    window_y = window_location[1]
    window_w_per = window_width / 100
    window_h_per = window_height / 100
    bbox_x1 = window_x + window_w_per * 44
    bbox_y1 = window_y + window_h_per * 13.6
    bbox_x2 = window_x + window_w_per * 55
    bbox_y2 = window_y + window_h_per * 15
    bbox = (bbox_x1, bbox_y1, bbox_x2, bbox_y2)
    green = np.array([60, 150, 60])
    while True:
        printscreen_pil = ImageGrab.grab(bbox=bbox)
        image = np.array(printscreen_pil)
        cv2.imshow("test", image)
        color = image[5,17]
        if np.array_equal(color, green):
            pressEnter()
            time.sleep(2)
            pressComma()
        if cv2.waitKey(25) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break


if __name__ == '__main__':
    try:
        main()
    except Exception:
        input()