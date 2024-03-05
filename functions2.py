import mouse
import time

import images
from move_functions import move_and_clic
class Item():
    "класс для взаимодействия с разными изображениями"
    def __init__(self, src):
        self.src = src

    def clic(self, xd = 0, yd = 0, delay = 0):
        xy_tmp = images.find_coordinates(str('images/' + self.src))
        if xy_tmp != None:
            x, y = xy_tmp[0], xy_tmp[1]
            print(x, y)
            move_and_clic(x + 24 + xd, y + 8 + yd)
        else:
            move_and_clic(1200, 500)
        time.sleep(1.5 + delay)

    def full_clic(self):
        def tmp():
            self.clic(-20, -4)
            if images.find_coordinates(str('images/' + self.src)) != None:
                return tmp()

        tmp()
        cross2.clic(-20, -4)


class Instructions():
    "класс инструкций"

    @classmethod
    def switch_window(cls, window = 1):
        aion_icon.clic()
        time.sleep(2)
        if window == 1:
            mouse.move(-77, -77, False)
            time.sleep(1)
            mouse.click('left')
        else:
            mouse.move(77, -77, False)
            time.sleep(1)
            mouse.click('left')

    @classmethod
    def find_fail(cls) -> bool:
        "функция поиска фейла крафта"
        if images.find_coordinates('images/ready_order.png') == None:
            # print('нет фейла')
            return True
        else:
            # print("фейл!")
            return False

    @classmethod
    def cancel_order(cls):
        "метод отмены заказа"
        cross.clic(-20, -4)
        menu_btn.clic()
        missions.clic()
        orders_on_missions_menu.clic()
        orders_on_missions_menu.clic(25, 80)
        orders_on_missions_menu.clic(13, 486)
        contune.clic()
        cross.full_clic()

    @classmethod
    def craft_risen(cls):
        "основной метод для прокачки крафта"
        npc.clic(0, 0, 3)
        orders_btn.clic()
        ready_order.clic()
        contune.clic()
        npc.clic()
        orders_btn.clic()
        if Instructions.find_fail():
            pass
        else:
            Instructions.cancel_order()
            npc.clic()
            orders_btn.clic()
        take_order.clic()
        agree_btn.clic()
        table.clic(0, 0, 4)
        learned.clic(120, 155)
        learned.clic(130, 100)
        create_all_btn.clic()

    @classmethod
    def two_window_craft(cls, delay = 0):
        'метод прокачки крафта в 2 окна'
        Instructions.switch_window()
        Instructions.craft_risen()
        time.sleep(2)
        Instructions.switch_window(2)
        Instructions.craft_risen()
        time.sleep(35 + delay)








aion_icon = Item('aion_icon.png')
npc = Item('makros_icon3.png')
table = Item('makros_icon4.png')
vendor = Item('makros_icon5.png')
orders_btn = Item('orders.png')
ready_order = Item('ready_order.png')
contune = Item('contune.png')
take_order = Item('take_order.png')
agree_btn = Item('agree_btn.png')
learned = Item('learned.png')
create_all_btn = Item('create_all.png')
cross = Item('cross.png')
cross2= Item('cross2.png')
menu_btn = Item('menu_btn.png')
missions = Item('missions.png')
orders_on_missions_menu = Item('orders_on_missions_menu.png')


time.sleep(2)
# learned.clic(130, 100)

# for i in range(35):
#     Instructions.two_window_craft(145)

for i in range(15):
    Instructions.craft_risen()
    time.sleep(145)

