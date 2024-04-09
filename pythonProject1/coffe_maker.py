from device import Device


class Coffee_Maker(Device):
    def __init__(self, name, price, amount_of_coffee):
        super().__init__(name, price)
        self.amount_of_coffee = amount_of_coffee

    def __str__(self):
        return f"""informace o stroji:
Jméno: {self.name}
Cena: {self.price} Kč
Průměrné množství kávy na šálek: {self.amount_of_coffee}g"""
