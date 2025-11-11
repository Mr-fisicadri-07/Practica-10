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
        super().__init__(nombre, "Baaaaaaa")

class Animales_Marinos(Animal): 
    """
    Clase intermedia. DEBE aceptar los argumentos de sus hijos
    y pasarlos a su padre (Animal).
    """
    def __init__(self, nombre, sonido):
        super().__init__(nombre, sonido)


class Delfin(Animales_Marinos):
    def __init__(self):
        super().__init__(
            "Soy un delfín influencer",
            "Perdón, quise decir: iiiiiii (sígueme en Insta)"
        )


class Tiburon(Animales_Marinos):
    def __init__(self):
        super().__init__(
            "Soy un tiburón mal entendido",
            "Quería decir: ñam ñam... digo, 'solo soy incomprendido'"
        )


class Pulpo(Animales_Marinos):
    def __init__(self):
        super().__init__(
            "Soy un pulpo multitarea",
            "Perdón, estoy respondiendo 8 whatsapps a la vez"
        )


class Medusa(Animales_Marinos):
    def __init__(self):
        super().__init__(
            "Soy una medusa brillante",
            "Ups, no hablo, solo doy toques eléctricos"
        )


class PezPayaso(Animales_Marinos):
    def __init__(self):
        super().__init__(
            "Soy un pez payaso",
            "Quería decir: 'ríete por compromiso, por favor'"
        )

