import pyautogui as pag
import time
import cv2
import numpy as np

"""Модуль с функциями машинного зрения """

def find_coordinates(tmp: str) -> tuple:
    'функция поиска шаблона на изображении. Возвращает координаты'
    # Преобразование изображения в оттенки серого
    time.sleep(0.3)
    pag.screenshot('screenshot.png')
    time.sleep(0.3)
    template = cv2.imread(tmp, cv2.IMREAD_GRAYSCALE)
    image = cv2.imread('screenshot.png')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Поиск совпадения
    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(result >= threshold)

    for pt in zip(*loc[::-1]):
        return pt

def oders_btn():
    return find_coordinates('images/orders.png')

def ready_order():
    return find_coordinates('images/ready_order.png')

def take_order():
    return find_coordinates('images/take_order.png')

def cross():
    return find_coordinates('images/cross.png')

def create_all():
    return find_coordinates('images/create_all.png')

def makros_icon():
    return find_coordinates('images/makros_icon.png')
def makros_icon2():
    return find_coordinates('images/makros_icon2.png')

def sewing_icon():
    return find_coordinates('images/sewing_icon.png')

def craft_icon():
    return find_coordinates('images/craft_icon.png')

def agree_btn():
    return find_coordinates('images/agree_btn.png')

def prinat_btn():
    return find_coordinates('images/prinat.png')

def orders_craft_menu():
    return find_coordinates('images/orders_craft_menu.png')

def menu_btn():
    return find_coordinates('images/menu_btn.png')
def missions():
    return find_coordinates('images/missions.png')

def orders_on_missions_menu():
    return find_coordinates('images/orders_on_missions_menu.png')

def craft_done():
    return find_coordinates('images/craft_done.png')