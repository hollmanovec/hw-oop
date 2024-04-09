from ship import Ship

class Destroyer(Ship):
    def __init__(self, name, length, width, weapons):
        super().__init__(name, length, width)
        self.weapons = f"Tento torpédoborec je vybaven zbraněmi typu {weapons}"

