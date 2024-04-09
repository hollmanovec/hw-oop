class Device:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def availability(self):
        print(f"Zařízení {self.name} je na skladě")     #Tam by pak byl samozřejmě nějaký check se skladem


