class Libro():
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
    def __str__(self):
        return "titulo: {}, autor: {}, n.paginas: {}".format(self.titulo,self.autor,self.paginas)
    def __len__(self):
        return self.paginas

l=Libro("Python","Jorge",200)
print(l)
print(len(l))
listas = [1,2,3]
print(listas)