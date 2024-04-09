from coffe_maker import Coffee_Maker
from blender import Blender
from meat_grinder import Meat_Grinder
from cruiser import Cruiser as Cruiser
from frigate import Frigate as Frigate
from destroyer import Destroyer as Destroyer

#Task1

coffee1 = Coffee_Maker("Nescafé", 2000, 8)
coffee2 = Coffee_Maker("Tassimo", 5000, 7)
coffee3 = Coffee_Maker("Nespresso", 4800, 6)

print(coffee3)
print()

b1 = Blender("Blender1", 1520, 220)
b2 = Blender("Blender2", 1990, 250)

print(b2)
b2.blend("cibule")
print()

mg1 = Meat_Grinder("Meat Grinder1 ", 2050, "Šnek")
mg2 = Meat_Grinder("Meat Grinder 2", 3500, "nože")

print(mg1)
mg2.grind("telecí maso")
print()


#Task 2

f1 = Frigate("Frigata 1", 60, 10, 5)
f2 = Frigate("Frigata 2", 40, 9, 3)
print(f1.number_of_sails)
print(f2)
print()

c1 = Cruiser("Křižník 1", 80, 20, "obranný")
c2 = Cruiser("Křižník 2", 75, 15, "pancéřovaný")

print(c2.type)
print()

d1 = Destroyer("Torpédoborec 1", 90, 10, "rakety")
d2 = Destroyer("Torpédoborec 2", 80, 12, "torpéda")

print(d1.weapons)
d2.destroy(f1)