class Animal:
    
    def __init__(self, nombre, sonido):
        self.nombre = nombre
        self.sonido = sonido

class Animales_Domesticos(Animal): # (Nota: Quité la tilde, es mejor evitar acentos en nombres de clases)
    
    def __init__(self, nombre, sonido):
        # 1. Recibe 'nombre' y 'sonido' (de Perro)
        # 2. Los pasa hacia "arriba" (a Animal)
        super().__init__(nombre, sonido)
        
        # Opcional: Aquí puedes añadir lógica solo para domésticos
        # self.es_domestico = True 

class Perro(Animales_Domesticos):
    
    def __init__(self, nombre, caracteristica="hacer pis"):
        # Pasa los valores "Perro" y "guau guau"
        # a su clase padre (Animales_Domesticos)
        super().__init__(nombre, "Quería decir, guau guau")
        self.caracteristica = caracteristica

class Gato(Animales_Domesticos):
    
    def __init__(self):
        # Pasa los valores "Perro" y "guau guau"
        # a su clase padre (Animales_Domesticos)
        super().__init__("Soy un gato", "Perdón, miau miau")


class Hamster(Animales_Domesticos):
    
    def __init__(self, nombre, caracteristica="roer"):
        # Pasa los valores "Perro" y "guau guau"
        # a su clase padre (Animales_Domesticos)
        super().__init__(nombre, "quería decir *roe algo*")
        self.caracteristica = caracteristica

class Periquito(Animales_Domesticos):
    
    def __init__(self):
        # Pasa los valores "Perro" y "guau guau"
        # a su clase padre (Animales_Domesticos)
        super().__init__("Soy un periquito", "perdón, pío pío")

class Perro(Animales_Domesticos):
    
    def __init__(self):
        # Pasa los valores "Perro" y "guau guau"
        # a su clase padre (Animales_Domesticos)
        super().__init__("Perro", "guau guau")