from devices import *

c1 = CoffeeMaker("Nescafé", 2000, 8)
c2 = CoffeeMaker("Tassimo", 5000, 7)
c3 = CoffeeMaker("Nespresso", 4800, 6)

b1 = Blender("Blender1", 1520, 220)
b2 = Blender("Blender2", 1990, 250)

mg1 = MeatGrinder("MeatGrinder1 ", 2050, "Šnek")
mg2 = MeatGrinder("MeatGrinder2", 3500, "nože")



print(c3)
print()

print(b2)
b2.blend("cibule")
print()

print(mg1)
mg2.grind("telecí maso")

print(c1.availability())
print(mg2.availability())
print(b2.availability())

