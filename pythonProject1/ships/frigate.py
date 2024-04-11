from .ship import Ship


class Frigate(Ship):
    def __init__(self, name, length, width, number_of_sails):
        super().__init__(name, length, width)
        self.number_of_sails = f"Tato loď má {number_of_sails} plachet."

