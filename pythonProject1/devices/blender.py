from .device import Device
class Blender(Device):
    def __init__(self, name, price, volume):
        super().__init__(name, price)
        self.volume = volume

    def __str__(self):
        return f"""informace o stroji:
Jméno: {self.name}
Cena: {self.price} Kč
Maximální objem mixéru: {self.volume}ml"""

    def blend(self, object):
        print(f"Mixér {self.name} úspěšně rozmixoval položku {object}")

