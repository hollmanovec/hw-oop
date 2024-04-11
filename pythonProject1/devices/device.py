class Device:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"""Informace o stroji:
Jméno: {self.name}
Cena: {self.price} Kč"""

    def availability(self):
        if self.name in stock:
            return f"Zařízení {self.name} je na skladě."

        else:
            return f"Zařízení {self.name} není na skladě."

stock = ["Nescafé", "Nespresso", "Blender1", "MeatGrinder2"]