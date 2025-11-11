from animales import Animal

class AnimalSalvaje(Animal):
    def __init__(self, nombre, sonido):
        super().__init__(nombre, sonido)
        self.nombre = nombre
        self.sonido = sonido    

class Leon (AnimalSalvaje):
    def __init__(self, nombre, sonido, caracteristica="Rey de la selva", ubicacion="selva"):
        super().__init__(nombre, "roar")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion

class mono (AnimalSalvaje):
    def __init__(self, nombre, sonido , caracteristica="Muy jugueton", ubicacion="selva"):
        super().__init__(nombre, "U u a a")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion

class lobo (AnimalSalvaje):
    def __init__(self, nombre, sonido , caracteristica="Cazador en manada", ubicacion="montaña"):
        super().__init__(nombre, "Auuuuuuuuuuuuuuu")    
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion

class elefante (AnimalSalvaje):
    def __init__(self, nombre, sonido , caracteristica="El animal terrestre mas grande", ubicacion="sabana"):
        super().__init__(nombre, "Patum patum patum")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion

class hiena (AnimalSalvaje):
    def __init__(self, nombre, caracteristica="Risa siniestra", ubicacion="bosque"):
        super().__init__(nombre, "Auuuuuuuuuuuuuuuuuu")
        self.caracteristica = caracteristica
        self.ubicacion = ubicacion