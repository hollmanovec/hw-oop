

class Money:
    def __init__(self, name, integer_name, decimal_name, integer=0, decimal=0 ):
        self.name = name
        self.integer = integer
        self.integer_name = integer_name
        self.decimal = decimal
        self.decimal_name = decimal_name

    def __str__(self):
        return f"""Name of the currency: {self.name}
Amount of money: {self.integer}.{self.decimal}"""

    def get_integer(self):
        return f"{self.integer} {self.integer_name}"

    def set_integer(self, n):
        self.integer = n
        print("Operation successful!")
        print()

    def get_decimal(self):
        return f"{self.decimal} {self.decimal_name}"


    def set_decimal(self, n):
        self.decimal = n
        print("Operation successful!")
        print()
