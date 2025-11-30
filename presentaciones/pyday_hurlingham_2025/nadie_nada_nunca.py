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
        self._autor = autor

    @property
    def autor(self):
        return self._autor

    def __repr__(self):
        return f"{super().__repr__()} id:{self.id}"

class LibroDesconocido:

    @property
    def autor(self):
        return "Libro desconocido"

class BibliotecaSegura:

    @staticmethod
    def buscar(id):
        return Biblioteca.buscar(id) or LibroDesconocido()

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


    libros = [Biblioteca.buscar(id) or LibroDesconocido() for id in ids]
    for libro in libros:
        print(libro.autor)

    libros = [BibliotecaSegura.buscar(id) for id in ids]