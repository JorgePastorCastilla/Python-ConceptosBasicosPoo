# HERENCIA#
class Animal():
    def __init__(self):
        print("Animal creado")

    def quiensoy(self):
        print("SOY UN ANIMAL")

    def comer(self):
        print("COMIENDO")

class Perro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print ("Perro creado")
    def ladrar(self):
        print("guau guau")
    def quiensoy(self):
        print("SOY UN PERRO")

p = Perro()
p.quiensoy()
p.comer()
p.ladrar()