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
    """
    Clase específica. Solo necesita definir sus propios valores
    y pasarlos hacia "arriba" (a Animales_Domesticos).
    """
    def __init__(self):
        # Pasa los valores "Perro" y "guau guau"
        # a su clase padre (Animales_Domesticos)
        super().__init__("Perro", "guau guau")

# --- Cómo usarlo ---

# 1. Creamos la instancia
mi_perro = Perro()

# 2. Imprimimos sus atributos (que se guardaron en la clase Animal)
print(f"Soy un {mi_perro.nombre} y mi sonido es '{mi_perro.sonido}'")

# Si imprimes el objeto solo, no verás los atributos:
# print(mi_perro)  # Esto solo mostrará algo como <__main__.Perro object at ...>