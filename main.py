import win32gui
import numpy as np
from PIL import ImageGrab, Image, ImageDraw, ImageChops
import time
import inventory
import threading

window_location = []
window_size = []


class Fisher:
    def __init__(self):
        self.inventory = inventory.Inventory()
        self.can_put = False

    def drop_fish(self):
        while True:
            if self.can_put:
                self.inventory.put_in_car()
                time.sleep(0.2)

    def main_stripe(self):
        win32gui.EnumWindows(callback, None)
        fish_bbox = get_fish_strip_bbox(window_size, window_location)
        green = np.array([60, 150, 60])
        while True:
            self.can_put = False
            printscreen_pil_stripe = ImageGrab.grab(bbox=fish_bbox)
            image_stripe = np.array(printscreen_pil_stripe)
            color_stripe = image_stripe[5, 17]
            if np.array_equal(color_stripe, green):
                inventory.pressEnter()
                time.sleep(1)
                inventory.pressComma()
                self.can_put = True
                time.sleep(0.2)

    def main(self):
        # self.drop_fish()
        threading.Thread(target=self.drop_fish).start()
        threading.Thread(target=self.main_stripe).start()



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





if __name__ == '__main__':
    fish = Fisher()
    fish.main()