import pyautogui as pag
import time

import images
from move_functions import move_and_clic, move_and_right_clic

"""Модуль с основными функциями"""


def select_npc():
    "функция нажатия на кнопку макроса, который выбирает нпс "
    xy_tmp = images.makros_icon()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
    else:
        move_and_clic(1200, 500)
    time.sleep(1.5)

def select_work_bench():
    """функция нажатия на кнопку макроса, который выбирает верстака. Верстак нужно пометить знаком 2
    и написать макрос для его выбора """
    xy_tmp = images.makros_icon2()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
    else:
        move_and_clic(1200, 500)
    time.sleep(1.5)

def orders_btn():
    "функция нажатия на кнопку 'заказы' "
    xy_tmp = images.oders_btn()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
    else:
        move_and_clic(350, 955)
    time.sleep(0.5)

def take_order():
    "функция нажатия на пункт меню 'новый заказ' ищет самый верхний заказ и нажимает на него"
    xy_tmp = images.take_order()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
    else:
        move_and_clic(350, 955)
    time.sleep(0.5)

def ready_order():
    "функция нажатия на пункт меню 'готовый заказ' "
    xy_tmp = images.ready_order()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
    else:
        move_and_clic(350, 955)
    time.sleep(0.5)

def cross():
    "функция нажатия на кнопку крестика, чтобы закрыть окно"
    xy_tmp = images.cross()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 2, y + 3)
        # mouse.click('left')
        # mouse.click('left')
    else:
        move_and_clic(350, 955)
    time.sleep(0.53)

def create_all():
    "функция нажатия на кнопку изготовить всё"
    xy_tmp = images.create_all()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 44, y + 7)
    else:
        move_and_clic(350, 955)
    time.sleep(0.5)

def agree_btn():
    "функция нажатия на кнопку согласиться"
    xy_tmp = images.agree_btn()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 44, y + 7)
    else:
        move_and_clic(350, 955)
    time.sleep(0.58)
def prinat_btn():
    "функция нажатия на кнопку принять"
    xy_tmp = images.prinat_btn()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 44, y + 7)
    else:
        move_and_clic(350, 955)
    time.sleep(0.59)

def select_craft():
    """функция нажатия на иконку иконку крафта. Или для каждого крафта вручную менять иконку или сделать
    универсальный макрос выбора иконки крафта
"""
    xy_tmp = images.makros_icon()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 4, y + 7)
    else:
        move_and_clic(350, 955)
    time.sleep(0.89)



def craft_new_order():
    "функция нажатия на заказ в меню заданий"
    xy_tmp = images.orders_craft_menu()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 90, y + 24)
    else:
        move_and_clic(350, 955)
    time.sleep(0.59)

def find_fail() -> bool:
    "функция поиска фейла крафта"
    if images.ready_order() == None:
        print('нет фейла')
        return True
    else:
        print("фейл!")
        return False

def craft_done():
    "функция проверки окончания крафта"
    time.sleep(1)
    if images.craft_done() != None:
        return True
    else:
        print('ещё 5 секунд')
        time.sleep(5)
        return craft_done()


def cancel_order():
    "функция отмены заказа"
    xy_tmp = images.menu_btn()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 2, y + 3)
        # mouse.click('left')
    else:
        move_and_clic(350, 955)
    time.sleep(0.5)
    xy_tmp = images.missions()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 12, y + 5)
    else:
        move_and_clic(350, 955)
    time.sleep(0.5)
    xy_tmp = images.orders_on_missions_menu()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 12, y + 5)
    else:
        move_and_clic(350, 955)
    time.sleep(0.15)
    move_and_clic(xy_tmp[0] + 27, xy_tmp[1] + 85)
    time.sleep(0.15)
    move_and_clic(xy_tmp[0] + 13, xy_tmp[1] + 488)
    prinat_btn()
    time.sleep(0.33)
    cross()



def craft_period():
    "функция крафта на 1 итерацию"
    cross()
    select_npc()
    orders_btn()
    ready_order()
    if images.prinat_btn():
        prinat_btn()
    else:
        cancel_order()
    time.sleep(2)
    select_npc()
    orders_btn()
    take_order()
    agree_btn()
    select_work_bench()
    # select_craft()
    craft_new_order()
    create_all()

def multi_craft(n: int):
    "функция полного цикла крафта. Принимает на вход количество нужных итераций крафта"
    for i in range(n):
        print('итерация ', i)
        craft_period()
        time.sleep(55)
        if craft_done():
            time.sleep(2)
            print('закончили крафт')





