import win32gui
import numpy as np
from PIL import ImageGrab, Image, ImageDraw, ImageChops
import time
import inventory
import threading

window_location = []
window_size = []

INVENTORY_ACTION = False


def get_fish_strip_bbox(window_size, window_location):
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
    return bbox


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


def drop_fish():
    time.sleep(2)
    while True:
        print(1)
        global INVENTORY_ACTION
        INVENTORY_ACTION = True
        inventory.put_in_car()
        INVENTORY_ACTION = False
        time.sleep(4)


def main_stripe():
    win32gui.EnumWindows(callback, None)
    fish_bbox = get_fish_strip_bbox(window_size, window_location)
    green = np.array([60, 150, 60])

    while True:
        if not INVENTORY_ACTION:
            printscreen_pil_stripe = ImageGrab.grab(bbox=fish_bbox)
            image_stripe = np.array(printscreen_pil_stripe)
            color_stripe = image_stripe[5, 17]
            if np.array_equal(color_stripe, green):

                inventory.pressEnter()
                time.sleep(1)
                inventory.pressComma()



def main():
    threading.Thread(target=main_stripe).start()
    threading.Thread(target=drop_fish).start()


if __name__ == '__main__':
    main()
    # time.sleep(2)
    # inventory.put_in_car()
