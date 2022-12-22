import pyautogui
import pygetwindow
from time import sleep
from win32gui import FindWindow, GetWindowRect


def click_element_region(img_dir: str, region: tuple):
    element = pyautogui.locateCenterOnScreen(f"{img_dir}", grayscale=False, confidence=.98, region=region)
    if element:
        pyautogui.click(element)
    else:
        print("Element not found.\n")
        return None


def locate_element_region(img_dir: str, region: tuple):
    element = pyautogui.locateCenterOnScreen(f"`{img_dir}", grayscale=False, confidence=.98, region=region)
    if element:
        return element
    else:
        print("Element not found.\n")
        return None


def click_element(img_dir: str):
    element = pyautogui.locateCenterOnScreen(f"{img_dir}", grayscale=False, confidence=.98)
    if element:
        pyautogui.click(element)
    else:
        print("Element not found.\n")
        return None


def locate_element(img_dir: str):
    element = pyautogui.locateCenterOnScreen(f"`{img_dir}", grayscale=False, confidence=.98)
    if element:
        return element
    else:
        print("Element not found.\n")
        return None


def get_window_rect():
    window_handle = FindWindow(None, "League of Legends")
    window_rect = GetWindowRect(window_handle)
    return window_rect


def focus_window():
    window = pyautogui.getWindowsWithTitle("League of Legends")[0]
    if window:
        window.minimize()
        sleep(1)
        window.maximize()
        sleep(1)
        window.activate()
