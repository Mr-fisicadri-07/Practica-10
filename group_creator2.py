import random

person = [
    "David", "Sergio", "Jorge", "Santiago", "Héctor", "Diego", "Marco",
    "Ginebra", "Izaro", "Nerea", "Andrea", "Rojo", "Román", "Adrián"
]

# Validación de entrada para evitar errores si el usuario pone 0 o letras
try:
    x = int(input("Please insert the number of integrants of the group: "))
    if x <= 0:
        print("The group size must be greater than 0.")
        exit()
except ValueError:
    print("Please enter a valid number.")
    exit()

# Lógica principal
random.shuffle(person)
grupos_random = []

# Crear los grupos base
for i in range(0, len(person), x):
    grupos_random.append(person[i:i + x])

# Lógica para manejar grupos "huerfanos" (de 1 sola persona)
# Si el último grupo tiene 1 persona y hay más de un grupo, movemos esa persona al penúltimo grupo.
if len(grupos_random) > 1 and len(grupos_random[-1]) == 1:
    ultimo_miembro = grupos_random.pop()  # Sacamos el último grupo (la lista completa)
    grupos_random[-1].extend(ultimo_miembro) # Añadimos el miembro al grupo anterior

# Imprimir resultados
print(f"\n--- Grupos generados (Total personas: {len(person)}) ---")
for i, grupo in enumerate(grupos_random):
    print(f"Grupo {i + 1}: {grupo} ({len(grupo)} personas)")