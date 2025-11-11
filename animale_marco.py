class Animal:
    """Clase base que almacena el nombre y el sonido."""
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido

class Animales_Domesticos(Animal): # (Nota: Quité la tilde, es mejor evitar acentos en nombres de clases)
    """
    Clase intermedia. DEBE aceptar los argumentos de sus hijos
    y pasarlos a su padre (Animal).
    """
    def __init__(self, nombre, sonido):
        # 1. Recibe 'nombre' y 'sonido' (de Perro)
        # 2. Los pasa hacia "arriba" (a Animal)
        super().__init__(nombre, sonido)
        
        # Opcional: Aquí puedes añadir lógica solo para domésticos
        # self.es_domestico = True 

class Perro(Animales_Domesticos):
    
    def __init__(self):
        # Pasa los valores "Perro" y "guau guau"
        # a su clase padre (Animales_Domesticos)
        super().__init__("Soy un perro", "Quería decir, guau guau")

class Gato(Animales_Domesticos):
    
    def __init__(self):
        # Pasa los valores "Perro" y "guau guau"
        # a su clase padre (Animales_Domesticos)
        super().__init__("Soy un gato", "Perdón, miau miau")


class Hamster(Animales_Domesticos):
    
    def __init__(self):
        # Pasa los valores "Perro" y "guau guau"
        # a su clase padre (Animales_Domesticos)
        super().__init__("Soy un hamster", "quería decir *roe algo*")

class Periquito(Animales_Domesticos):
    
    def __init__(self):
        # Pasa los valores "Perro" y "guau guau"
        # a su clase padre (Animales_Domesticos)
        super().__init__("Soy un periquito", "perdón, pío pío")

class Perro(Animales_Domesticos):
    
    def __init__(self):
        # Pasa los valores "Perro" y "guau guau"
        # a su clase padre (Animales_Domesticos)
        super().__init__("Perro"    , "guau guau")
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
        super().__init__(nombre, "Mee")

class AnimalSalvaje(Animal):
    def __init__(self, nombre, sonido):
        super().__init__(nombre, sonido)
        self.nombre = nombre
        self.sonido = sonido    

class Leon (AnimalSalvaje):
    def __init__(self, nombre, sonido, caracteristica="Rey de la selva"):
        super().__init__(nombre, sonido)
        self.caracteristica = caracteristica
        sonido = "r"

class mono (AnimalSalvaje):
    def __init__(self, nombre, sonido , caracteristica="Muy jugueton"):
        super().__init__(nombre, sonido)
    

class lobo (AnimalSalvaje):
    def __init__(self, nombre, sonido , caracteristica="Cazador en manada"):
        super().__init__(nombre, sonido)    

class elefante (AnimalSalvaje):
    def __init__(self, nombre, sonido , caracteristica="El animal terrestre mas grande"):
        super().__init__(nombre, sonido)

class hiena (AnimalSalvaje):
    def __init__(self, nombre, sonido , caracteristica="Risa siniestra"):
        super().__init__(nombre, sonido)
        super().__init__(nombre, "Baaaaaaa")