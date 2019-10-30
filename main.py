import win32gui
import numpy as np
from PIL import ImageGrab, Image, ImageDraw, ImageChops
import cv2
import time
import keyPress
import inventory
import pyautogui



window_location = []
window_size = []


# fish1.show()


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


def get_fish_val_bbox(window_size, window_location):
    window_width = window_size[0]
    window_height = window_size[1]
    window_x = window_location[0]
    window_y = window_location[1]
    window_w_per = window_width / 100
    window_h_per = window_height / 100
    bbox_x1 = window_x + window_w_per * 16.5
    bbox_y1 = window_y + window_h_per * 94.6
    bbox_x2 = window_x + window_w_per * 18.8
    bbox_y2 = window_y + window_h_per * 97
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


def main():
    win32gui.EnumWindows(callback, None)
    fish_bbox = get_fish_strip_bbox(window_size, window_location)
    fish_val_bbox = get_fish_val_bbox(window_size, window_location)
    green = np.array([60, 150, 60])
    while True:
        # printscreen_pil_1 = ImageGrab.grab(bbox=fish_bbox)
        # printscreen_pil_2 = ImageGrab.grab(bbox=fish_val_bbox)
        # image1 = np.array(printscreen_pil_1)
        # image2 = np.array(printscreen_pil_2)
        # cv2.imshow("test1", image2)
        # cv2.imshow("test", image1)
        # color = image1[5, 17]
        im = Image.open("images/3.png").crop(fish_val_bbox)
        fish1 = Image.open(r"images/3.png").crop(fish_val_bbox)
        # fish1.show()
        # im.show()
        diff = ImageChops.difference(fish1, im)
        t_data = [1 for x in diff.getdata() if sum(x)]
        print(sum(t_data))
        break
    #
    #     if np.array_equal(color, green):
    #         inventory.pressEnter()
    #         time.sleep(1)
    #         screenshot = pyautogui.screenshot()
    #         screenshot.save(r'temp.png')
    #         im = Image.open("temp.png").crop(fish_val_bbox)
    #         im.show()
            # time.sleep(2)
            # inventory.pressComma()
        # if cv2.waitKey(25) & 0xFF == ord('q'):
        #     cv2.destroyAllWindows()
        #     break
    pass

if __name__ == '__main__':
    try:
        main()
    except Exception:
        input()