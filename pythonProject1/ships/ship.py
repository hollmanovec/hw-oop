class Ship:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width

    def __str__(self):
        return f"Typ této lodi je {type(self).__name__}. Její jméno je {self.name} a její rozměry jsou {self.length}m x {self.width}m."

    def destroy(self, other):
        print(f"Loď {other.name} byla zničena lodí {self.name}")