import pyautogui as pag
import time
import cv2
import numpy as np

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
    return find_coordinates('images/makros_btn.png')


