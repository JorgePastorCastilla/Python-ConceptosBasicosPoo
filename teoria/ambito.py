#AMBITO#
# Python sigue la regla LEGB:
# L - LOCAL
# E - ENCLOSING FUNCTION LOCALS
# G - GLOBAL
# B - BUILT-IN

"""
x = 25
def prueba():
    x = 50
    return x

print(x)
print(prueba())
x=prueba()
print(x)
"""

# nombre = "Esto es una variable global"
#
# def saludo():
#     nombre = "Belen"
#
#     def hola():
#         print("hola " + nombre)
#
#     hola()
# saludo()
# print (nombre)

x = 25

def prueba():
    # print('x es:' + str(x))
    global x
    x = 1000
    print('la variable local x ha cambiado ' + str(x))
    return x

print(x)
print(prueba())
# x=prueba()
print(x)