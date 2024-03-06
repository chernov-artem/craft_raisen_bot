"рассчет ресурсов для крафта"

class Res():
    "класс ресурсов"

    def __init__(self, name: str, cost: int):
        self.name = name
        self.cost = cost

class Blacksmith(Res):
    'класс кузн дела'
    pass

class Arms(Res):
    'класс оружейки'
    pass

class Cooking(Res):
    'класс кулинарки'
    pass

class Alhem(Res):
    'класс алхимии'
    pass

class Sew(Res):
    'класс портняжки'
    pass

class Jew(Res):
    'класс ювелирки'
    pass

