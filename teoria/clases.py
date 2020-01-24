#CLASES#
# Por convencion las clases se nombran con la primera letra en mayuscula
# Los metodos se nombran todos en minuscula

# class Perro():
#     especie = "canis"
#     def __init__(self,raza,nombre):
#         self.raza = raza
#         self.nombre = nombre
#
# x = Perro(raza = "labrador", nombre="perrito")
# print(type(x))
# print (x.raza)
# print (x.nombre)
# print (x.especie)

class Circulo():

    pi=3.1416
    def __init__(self,radio=1):
        self.radio = radio
    def area(self):
        return (self.radio*self.radio)*Circulo.pi
    def set_radio(self,nuevo_r):
        self.radio = nuevo_r
    def cambioPi(self,pi):
        Circulo.pi = pi
c= Circulo(100)
print(c.radio)
print(c.area())
c.cambioPi(3)
print(c.area())
