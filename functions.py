import pyautogui as pag
import time

import images
from move_functions import move_and_clic, move_and_right_clic


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

def orders_btn():
    "функция нажатия на кнопку 'заказы' "
    xy_tmp = images.oders_btn()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.5)

def take_order():
    "функция нажатия на пункт меню 'новый заказ' ищет самый верхний заказ и нажимает на него"
    xy_tmp = images.take_order()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.5)

def ready_order():
    "функция нажатия на пункт меню 'готовый заказ' "
    xy_tmp = images.ready_order()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 24, y + 8)
    else:
        move_and_clic(1200, 500)
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
        move_and_clic(1200, 500)
    time.sleep(0.53)

def create_all():
    "функция нажатия на кнопку изготовить всё"
    xy_tmp = images.create_all()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 44, y + 7)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.5)

def agree_btn():
    "функция нажатия на кнопку согласиться"
    xy_tmp = images.agree_btn()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 44, y + 7)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.58)
def prinat_btn():
    "функция нажатия на кнопку принять"
    xy_tmp = images.prinat_btn()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 44, y + 7)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.59)

def select_sewing():
    "функция нажатия на иконку шитья"
    xy_tmp = images.sewing_icon()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 4, y + 7)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.49)
def craft_new_order():
    "функция нажатия на заказ в меню заданий"
    xy_tmp = images.orders_craft_menu()
    if xy_tmp != None:
        x, y = xy_tmp[0], xy_tmp[1]
        print(x, y)
        move_and_clic(x + 90, y + 24)
    else:
        move_and_clic(1200, 500)
    time.sleep(0.59)

def find_fail():
    "функция поиска фейла крафта"
    if images.ready_order() == None:
        print('нет фейла')
    else:
        print("фейл!")
    xy_tmp = images.orders_craft_menu()
    # if xy_tmp != None:
    #     x, y = xy_tmp[0], xy_tmp[1]
    #     print(x, y)
    #     move_and_clic(x + 90, y + 24)
    # else:
    #     move_and_clic(1200, 500)
    # time.sleep(0.59)

def craft_period():
    cross()
    select_npc()
    orders_btn()
    ready_order()
    prinat_btn()
    time.sleep(2)
    select_npc()
    orders_btn()
    take_order()
    agree_btn()

time.sleep(2)

# craft_period()
# select_sewing()
# craft_new_order()
# create_all()

find_fail()