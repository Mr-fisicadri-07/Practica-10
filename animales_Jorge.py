class Animal:
    """Clase base que almacena el nombre y el sonido."""
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido

# (Nota: La convención sugiere 'AnimalesGranja' como nombre)
class animales_granja(Animal):
    """Clase intermedia para animales de granja."""
    def __init__(self, nombre, sonido):
        super().__init__(nombre, sonido)

class Vaca(animales_granja):
    def __init__(self, nombre, caracteristica="dar leche", ubicacion="granja"):
        # 1. Pasa nombre y sonido al padre
        super().__init__(nombre, "Muu")
        # 2. Almacena los atributos específicos de esta clase
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion

class Cerdo(animales_granja):
    def __init__(self, nombre, caracteristica="revolcarse en el lodo", ubicacion="granja"):
        super().__init__(nombre, "Oink")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion

class Oveja(animales_granja):
    def __init__(self, nombre, caracteristica="se esquila", ubicacion="granja"):
        super().__init__(nombre, "Bee")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion

class Gallo(animales_granja):
    def __init__(self, nombre, caracteristica="cantar al amanecer", ubicacion="granja"):
        super().__init__(nombre, "kikiriki")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion

class Cabra(animales_granja): # (Corregido de 'cabra' a 'Cabra')
    def __init__(self, nombre, caracteristica="trepar", ubicacion="granja"):
        super().__init__(nombre, "Baaaaaaa")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion