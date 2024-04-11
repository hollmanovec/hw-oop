from .device import Device


class MeatGrinder(Device):
    def __init__(self, name, price, interior):
        super().__init__(name, price)
        self.interior = interior            #šnek nebo nože

    def __str__(self):
        return f"""informace o stroji:
Jméno: {self.name}
Cena: {self.price} Kč
Vnitřní mechanismus mletí: {self.interior}"""


    def grind(self, object):
        print(f"Vrrrrr, položka {object} byla úspěšně rozemleta")

