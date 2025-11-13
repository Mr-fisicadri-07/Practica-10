import random
# Asumo que estos imports funcionan y los archivos existen
from animales_jorge import Vaca, Cerdo, Oveja, Gallo, Cabra
from animales_andrea import Delfin, Tiburon, Pulpo, Medusa, PezGlobo, CaballitoDeMar, EstrellaDeMar
from animales_adrian import Perro, Gato, Hamster, Periquito, Nemo
from animales_marco import Leon, Mono, Lobo, Elefante, Hiena

# --- 1. POBLACIÓN DE ANIMALES ---
poblacion_total = [
    # Domésticos
    Perro("Perro"), Gato("Gato"), Hamster("Hamster"), Periquito("Periquito"), Nemo("Nemo"),
    # Granja
    Vaca("Vaca"), Cerdo("Cerdo"), Oveja("Oveja"), Gallo("Gallo"), Cabra("Cabra"),
    # Marinos
    Delfin("Delfín"), Tiburon("Tiburón"), Pulpo("Pulpo"), PezGlobo("Pez Globo"),Medusa("Medusa"), CaballitoDeMar("Caballito de Mar"), EstrellaDeMar("Estrella de Mar"),
    # Salvajes
    Leon("León"), Mono("Mono"), Lobo("Lobo"), Elefante("Elefante"), Hiena("Hiena")
]

# --- 2. INICIALIZAR EL LIBRO (FUERA DEL BUCLE) ---
mi_libro_de_animales = [] 
print("¡Bienvenido al juego de coleccionar animales!")

# --- 3. BUCLE PRINCIPAL DEL JUEGO ---
while True:
    
    # --- Comprobar si quedan animales suficientes para jugar ---
    if len(poblacion_total) < 3:
        print("\n¡Felicidades! Has coleccionado tantos animales que no podemos seguir jugando.")
        print("Juego terminado.")
        break # Sale del bucle 'while'

    print("\n" + "=" * 30)
    print("  JUEGO: ¿QUÉ ANIMAL HACE ESTE SONIDO?  ")
    print("=" * 30)

    # 1. Elegir 3 animales únicos de los que quedan
    opciones = random.sample(poblacion_total, 3)

    # 2. De esos 3, elegimos 1 para que sea la respuesta correcta
    animal_correcto = random.choice(opciones)

    # 3. Guardamos el nombre (especie) y el sonido
    nombre_correcto = animal_correcto.nombre
    sonido_pregunta = animal_correcto.sonido

    # 4. Presentamos la pregunta
    print(f"Un animal dice: ¡{sonido_pregunta}!")
    print("\n¿Cuál de estos animales crees que es?\n")

    # 5. Barajamos las opciones
    random.shuffle(opciones)

    # 6. Mostramos las opciones (A, B, C)
    mapa_de_opciones = {}
    letras = ['A', 'B', 'C']

    for i in range(3):
        letra = letras[i]
        nombre_animal_opcion = opciones[i].nombre
        
        print(f"   {letra}) {nombre_animal_opcion}")
        mapa_de_opciones[letra] = nombre_animal_opcion

    # 7. Pedimos la respuesta al usuario
    print("-" * 30)
    respuesta_usuario = input("Elige A, B, o C: ").upper()

    # 8. Comprobamos la respuesta
    if respuesta_usuario in mapa_de_opciones:
        nombre_elegido = mapa_de_opciones[respuesta_usuario]
        
        if nombre_elegido == nombre_correcto:
            print(f"\n¡CORRECTO! 🥳  Era un {nombre_correcto}.")
            
            # --- ¡AQUÍ ESTÁ LA NUEVA LÓGICA! ---
            
            # 8a. Pedimos un nombre personalizado
            nuevo_nombre = input(f"¿Qué nombre quieres ponerle a tu {nombre_correcto}? ")
            
            # 8b. Añadimos ese nombre como un nuevo atributo al objeto
            animal_correcto.nombre_personalizado = nuevo_nombre
            
            # 8c. Añadimos el animal a nuestro libro
            mi_libro_de_animales.append(animal_correcto)
            
            # 8d. Lo quitamos de la población para no volver a encontrarlo
            poblacion_total.remove(animal_correcto)
            
            print(f"¡{nuevo_nombre} (un/a {nombre_correcto}) se ha añadido a tu libro!")
            # --- FIN DE LA NUEVA LÓGICA ---

        else:
            print(f"\nINCORRECTO. 😕 El animal que eligió ({nombre_elegido}) no era.")
            print(f"La respuesta correcta era {nombre_correcto}.")
    else:
        print("\n¡Opción no válida! Debes elegir A, B o C.")

    # --- 4. MOSTRAR EL LIBRO Y PREGUNTAR DE NUEVO ---
    
    print("\n--- 📖 Tu Libro de Animales ---")
    if not mi_libro_de_animales:
        print("(Aún está vacío)")
    else:
        # Mostramos los animales con su nuevo nombre
        for animal in mi_libro_de_animales:
            print(f"  - {animal.nombre_personalizado} (Especie: {animal.nombre})")
    print("-" * 30)
    print(f"({len(poblacion_total)} animales restantes por descubrir)")

    # Preguntamos si quiere jugar otra ronda
    jugar_de_nuevo = input("¿Jugar otra ronda? (s/n): ").lower()
    if jugar_de_nuevo != 's':
        print("\n¡Gracias por jugar! ¡Vuelve pronto!")
        break # Sale del bucle 'while'