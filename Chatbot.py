import random

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

# --- 2. INICIALIZAR EL LIBRO ---
mi_libro_de_animales = [] 
print("¡Bienvenido al juego de coleccionar animales!")

# --- 3. BUCLE PRINCIPAL DEL JUEGO ---
while True:
    
    # --- Comprobar si quedan animales suficientes para jugar ---
    if len(poblacion_total) < 3:
        print("\n¡Felicidades! Has coleccionado tantos animales que no podemos seguir jugando.")
        print("Juego terminado.")
        break 

    print("\n" + "=" * 30)
    print("   JUEGO: ADIVINA EL ANIMAL   ")
    print("=" * 30)

    # 1. Elegir 3 animales únicos
    opciones = random.sample(poblacion_total, 3)

    # 2. Elegir 1 respuesta correcta
    animal_correcto = random.choice(opciones)

    # 3. Guardamos datos
    nombre_correcto = animal_correcto.nombre
    sonido_pregunta = animal_correcto.sonido
    
    # 4. Obtenemos la característica del animal
    pista_caracteristica = animal_correcto.caracteristica 

    # 5. Presentamos la pregunta con las pistas
    print(f"Un animal hace este sonido: '¡{sonido_pregunta}!'")
    print(f"Pista extra: Es conocido por {pista_caracteristica}.")
    print("\n¿Cuál de estos animales crees que es?\n")

    # 6. Barajamos las opciones
    random.shuffle(opciones)

    # 7. Mostramos las opciones (A, B, C)
    mapa_de_opciones = {}
    letras = ['A', 'B', 'C']

    for i in range(3):
        letra = letras[i]
        nombre_animal_opcion = opciones[i].nombre
        
        print(f"   {letra}) {nombre_animal_opcion}")
        mapa_de_opciones[letra] = nombre_animal_opcion

    # 8. Pedimos la respuesta
    print("-" * 30)
    respuesta_usuario = input("Elige A, B, o C: ").upper()

    # 9. Comprobamos la respuesta
    if respuesta_usuario in mapa_de_opciones:
        nombre_elegido = mapa_de_opciones[respuesta_usuario]
        
        if nombre_elegido == nombre_correcto:
            print(f"\n¡CORRECTO! 🥳  Era un {nombre_correcto}.")
            
            # 9a. Pedimos nombre personalizado
            nuevo_nombre = input(f"¿Qué nombre quieres ponerle a tu {nombre_correcto}? ")
            
            # 9b. Añadimos atributo personalizado
            animal_correcto.nombre_personalizado = nuevo_nombre
            
            # 9c. Añadimos al libro
            mi_libro_de_animales.append(animal_correcto)
            
            # 9d. Lo quitamos de la población
            poblacion_total.remove(animal_correcto)
            
            print(f"¡{nuevo_nombre} (un/a {nombre_correcto}) se ha añadido a tu libro!")

        else:
            print(f"\nINCORRECTO. 😕 El animal que eligió ({nombre_elegido}) no era.")
            print(f"La respuesta correcta era {nombre_correcto}.")
            ### NUEVO: Explicamos por qué (mostrando la característica) ###
            print(f"Recuerda: El {nombre_correcto} es el que suele {pista_caracteristica}.")
    else:
        print("\n¡Opción no válida! Debes elegir A, B o C.")

    # --- 4. MOSTRAR EL LIBRO Y PREGUNTAR DE NUEVO ---
    
    print("\n--- 📖 Tu Libro de Animales ---")
    if not mi_libro_de_animales:
        print("(Aún está vacío)")
    else:
        # Mostramos los animales con su nuevo nombre y su característica
        for animal in mi_libro_de_animales:
            # Añadimos la característica al reporte del libro
            print(f"  - {animal.nombre_personalizado} ({animal.nombre}) -> Le gusta {animal.caracteristica}")
            
    print("-" * 30)
    print(f"({len(poblacion_total)} animales restantes por descubrir)")

    # Preguntamos si quiere jugar otra ronda
    jugar_de_nuevo = input("¿Jugar otra ronda? (s/n): ").lower()
    if jugar_de_nuevo != 's':
        print("\n¡Gracias por jugar! ¡Vuelve pronto!")
        break