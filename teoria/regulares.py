#EXPRESIONES REGULARES#
import re

# patron=['term1','term2']
# patron= 'term1'
# texto = "Esto es un texto en el que aparece term1"

# print(re.search(patron,texto))

# enc = re.search(patron,texto)
# enc = re.split(patron,texto)
# print enc
#print(enc.start()) # INDICE DE POSICION DONDE SE ENCUENTRA EL PATRON

# for p in patron:
#     print("Estoy buscando el patron: {}".format(p))
#     if( re.search(p,texto) ):
#         print("ENCONTRADO")
#     else:
#         print("NO ENCONTRADO")

def multi_re_find(patrones, texto):
    for pat in patrones:
        print ("Estoy buscando el patron: {}".format(pat))
        print( re.findall(pat,texto) )
        print("\n")
# frase = 'sdsd...... dssdsdsddd.....sss...........dsdsssss......dsdsdsds...sddsd'
#test_pat = ['sd*'] # S seguida de 0 o mas D
#test_pat = ['sd+'] # S seguida de 1 o mas D
# test_pat = ['sd?'] # S y 1 D o S y 0D
# test_pat = ['sd{3}'] # S seguida de 3 D
# test_pat = ['sd{2:3}'] # S seguida de 2 o 3 D
# test_pat = ['s[sd]+'] # S seguida de una D o mas / una S o mas

frase = "Esto es un string! Pero contiene signos de puntuacion. Y un #hashtag"
# test_pat = ['[^!?.,#]+'] # Busca todos los elementos !?.,#
# test_pat = ['[a-z]+']
# test_pat = [r'\S+'] # Busca los espacios
# test_pat = [r'\W+'] # Busca los signos de puntuacion
test_pat = [r'\D+'] # Busca los numeros


multi_re_find(test_pat,frase)