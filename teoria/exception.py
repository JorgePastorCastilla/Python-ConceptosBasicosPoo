#ERRORES Y EXCEPCIONES#
# try
# except
# finally

try:
    f = open("ejemplo.txt",'r')
    f.write("Esto es una prueba")
except IOError:
    print("Error!! no se puede abrir el fichero o escribir")
else:
    print("Todo correcto")
finally:
    print("Despues de la ejecucion, con error o sin error")
