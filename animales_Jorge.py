class Animal:
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido
class animales_granja(Animal):
    def __init__(self, nombre, sonido):
        super().__init__(nombre, sonido)
class Vaca(animales_granja):
    def __init__(self, nombre):
        super().__init__(nombre, "Muu")
class Cerdo(animales_granja):
    def __init__(self, nombre):
        super().__init__(nombre, "Oink")
class Oveja(animales_granja):
    def __init__(self, nombre):
        super().__init__(nombre, "Bee")
class Gallo(animales_granja):
    def __init__(self, nombre):
        super().__init__(nombre, "kikiriki")
class  cabra(animales_granja):
    def __init__(self, nombre):
        super().__init__(nombre, "Baaaaaaa")
