# --- 4. CREAR LA "POBLACIÓN" DE ANIMALES ---
# Creamos instancias de cada animal para que el juego pueda elegirlas.
# Usamos el tipo de animal como su nombre para que el juego funcione.

poblacion_total = [
    # Domésticos
    Perro("Perro"), Gato("Gato"), Hamster("Hamster"), Periquito("Periquito"), PezDomestico("Pez Doméstico"),
    # Granja
    Vaca("Vaca"), Cerdo("Cerdo"), Oveja("Oveja"), Gallo("Gallo"), Cabra("Cabra"),
    # Marinos
    Delfin("Delfín"), Tiburon("Tiburón"), Pulpo("Pulpo"), PezPayaso("Pez Payaso"),
    # Salvajes
    Leon("León"), Mono("Mono"), Lobo("Lobo"), Elefante("Elefante"), Hiena("Hiena")
]


# --- 5. LÓGICA DEL JUEGO DE OPCIONES MÚLTIPLES ---

print("============================================")
print("  JUEGO: ¿QUÉ ANIMAL HACE ESTE SONIDO?  ")
print("============================================")

# 1. Elegir 3 animales únicos al azar de la población
#    random.sample() es perfecto para esto, ¡no coge repetidos!
opciones = random.sample(poblacion_total, 3)

# 2. De esos 3, elegimos 1 para que sea la respuesta correcta
animal_correcto = random.choice(opciones)

# 3. Guardamos el nombre y el sonido correctos
nombre_correcto = animal_correcto.nombre
sonido_pregunta = animal_correcto.sonido

# 4. Presentamos la pregunta
print(f"Un animal dice: ¡{sonido_pregunta}!")
print("\n¿Cuál de estos animales crees que es?\n")

# 5. Barajamos las opciones para que no salgan siempre en el mismo orden
random.shuffle(opciones)

# 6. Mostramos las opciones (A, B, C) y guardamos cuál es cuál
#    Usamos un diccionario para rastrear la respuesta
mapa_de_opciones = {}
letras = ['A', 'B', 'C']

for i in range(3):
    letra = letras[i]
    nombre_animal_opcion = opciones[i].nombre
    
    print(f"   {letra}) {nombre_animal_opcion}")
    mapa_de_opciones[letra] = nombre_animal_opcion # Ej: {'A': 'Perro'}

# 7. Pedimos la respuesta al usuario
print("--------------------------------------------")
respuesta_usuario = input("Elige A, B, o C: ").upper() # .upper() para A, B, C

# 8. Comprobamos la respuesta
if respuesta_usuario in mapa_de_opciones:
    # Vemos qué nombre de animal eligió el usuario
    nombre_elegido = mapa_de_opciones[respuesta_usuario]
    
    # Comparamos si ese nombre es el correcto
    if nombre_elegido == nombre_correcto:
        print(f"\n¡CORRECTO! 🥳  Era un {nombre_correcto}.")
    else:
        print(f"\nINCORRECTO. 😕 El animal que eligió ({nombre_elegido}) no era.")
        print(f"La respuesta correcta era {nombre_correcto}.")
else:
    print("\n¡Opción no válida! Debes elegir A, B o C.")