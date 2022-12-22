import pyautogui
from time import sleep
import pygetwindow
import utils
import functions


window_rect = functions.get_window_rect()


def create_lobby():
    #functions.focus_window()
    sleep(1)
    functions.click_element_region("./img/gui/play_button.png", window_rect)
    sleep(1)
    functions.click_element_region("./img/gui/soloduo_ranked.png", window_rect)
    sleep(1)
    functions.click_element_region("./img/gui/confirm_lobby_button.png", window_rect)


def define_role():
    functions.click_element_region("./img/gui/pointer_role.png", window_rect)
    sleep(2)
    functions.click_element_region("./img/gui/roles/jungle_role.png", window_rect)
    sleep(2)
    functions.click_element_region("./img/gui/pointer_role.png", window_rect)
    sleep(2)
    functions.click_element_region("./img/gui/roles/top_role.png", window_rect)


def start_queue():
    functions.click_element_region("./img/gui/search_queue.png", window_rect)
    sleep(3)

sleep(5)
create_lobby()
sleep(5)
define_role()
sleep(5)
start_queue()
