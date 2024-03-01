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
    cv2.imshow('1', template)
    image = cv2.imread('screenshot.png')
    cv2.imshow('2', image)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Поиск совпадения
    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    threshold = 0.9
    loc = np.where(result >= threshold)
    print(loc)

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

def makros_icon3():
    return find_coordinates('images/makros_icon3.png')
def makros_icon4():
    return find_coordinates('images/makros_icon4.png')
def makros_icon5():
    return find_coordinates('images/makros_icon5.png')
def sewing_icon():
    return find_coordinates('images/sewing_icon.png')

def smithing_icon():
    return find_coordinates('images/smithing_icon.png')

def craft_icon():
    return find_coordinates('images/craft_icon.png')

def agree_btn():
    return find_coordinates('images/agree_btn.png')

def prinat_btn():
    return find_coordinates('images/contune.png')

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



