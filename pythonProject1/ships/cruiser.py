from .ship import Ship


class Cruiser(Ship):
    def __init__(self, name, length, width, type):
        super().__init__(name, length, width)
        self.type = f"Typ tohoto křižníku je: {type}."      #pomocné, lehké, pancéřové, bitevní