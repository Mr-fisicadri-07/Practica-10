class Animal:
    
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido

class Animales_Domesticos(Animal): 
    
    def __init__(self, nombre, sonido):
    
        super().__init__(nombre, sonido)
        

class Perro(Animales_Domesticos):
    
    def __init__(self, nombre, caracteristica="hacer pis", ubicacion="casa"):
    
        super().__init__(nombre, "Quería decir, guau guau")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion

class Gato(Animales_Domesticos):
    
    def __init__(self, nombre, caracteristica="arañar", ubicacion="casa"):
        # Pasa los valores "Perro" y "guau guau"
        # a su clase padre (Animales_Domesticos)
        super().__init__(nombre, "Perdón, miau miau")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion


class Hamster(Animales_Domesticos):
    
    def __init__(self, nombre, caracteristica="roer", ubicacion="casa"):
        # Pasa los valores "Perro" y "guau guau"
        # a su clase padre (Animales_Domesticos)
        super().__init__(nombre, "quería decir *roe algo*")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion

class Periquito(Animales_Domesticos):
    
    def __init__(self, nombre, caracteristica="dar picotazos", ubicacion="casa"):
        # Pasa los valores "Perro" y "guau guau"
        # a su clase padre (Animales_Domesticos)
        super().__init__(nombre, "perdón, pío pío")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion

class Nemo(Animales_Domesticos):
    
    def __init__(self, nombre, caracteristica="ser un payaso", ubicacion="casa"):
        # Pasa los valores "Perro" y "guau guau"
        # a su clase padre (Animales_Domesticos)
        super().__init__(nombre, "quería decir, glugluglu")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion


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

class Cabra(animales_granja):
    def __init__(self, nombre):
        super().__init__(nombre, "Baaaaaaa")

class Animales_Marinos(Animal): 
    """
    Clase intermedia. DEBE aceptar los argumentos de sus hijos
    y pasarlos a su padre (Animal).
    """
    def __init__(self, nombre, sonido):
        super().__init__(nombre, sonido)
