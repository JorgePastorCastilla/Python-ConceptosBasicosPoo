def func():
    print ("func() en priemero.py")
    print("TOP LEVEL primero.py")
    if(__name__== "__main__"):
        print("El fichero primero.py se esta ejecutando direcamente")
    else:
        print("el fichero primero.py se ha importado")