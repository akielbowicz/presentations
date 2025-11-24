class Biblioteca:

    _libros = dict()

    @staticmethod
    def buscar(id):
        return Biblioteca._libros.get(id, None)
    
    @staticmethod
    def agregar(libro):
        if Biblioteca.buscar(libro) is None:
            Biblioteca._libros[libro.id] = libro

class Libro:

    def __init__(self, id, autor):
        self.id = id
        self.autor = autor

    def __repr__(self):
        return f"{super().__repr__()} id:{self.id}"

if __name__ == "__main__":
    ls = [Libro("Los Sorias", "Alberto Laiseca"),
          Libro("Ocio", "Fabián Casas"),]

    for libro in ls:
        Biblioteca.agregar(libro)

    ids = ["Los Sorias", "", "Ocio"]
    libros = [Biblioteca.buscar(id) for id in ids]

    
    # for libro in libros:
    #     print(libro.autor)

    for libro in libros:
        print(libro and libro.autor)