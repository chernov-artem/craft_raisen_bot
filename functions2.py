import mouse
import time

import images
from move_functions import move_and_clic
class Item():
    ""
    def __init__(self, src):
        self.src = src

    def clic(self, xd = 0, yd = 0):
        xy_tmp = images.find_coordinates(str('images/' + self.src))
        if xy_tmp != None:
            x, y = xy_tmp[0], xy_tmp[1]
            print(x, y)
            move_and_clic(x + 24 + xd, y + 8 + yd)
        else:
            move_and_clic(1200, 500)
        time.sleep(1.5)




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

time.sleep(2)
# learned.clic(130, 100)
aion_icon.clic()
mouse.move(-77, -77, False)
