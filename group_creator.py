import random

person = [
    "David", "Sergio", "Jorge", "Santiago", "Héctor", "Diego", "Marco",
    "Ginebra", "Izaro", "Nerea", "Andrea", "Rojo", "Román", "Adrián"
    ]

# --- Hacemos una copia de la lista original ---
# Esto es importante para no "gastar" la lista original.
# La lista 'remaining_people' se irá achicando.
remaining_people = list(person)

try:
    x = int(input("Please insert the number of integrants of the group: "))

    if x <= 0:
        print("Error: The group size must be a positive number.")
    elif x > len(person):
        print(f"Error: Cannot pick a group of {x} from only {len(person)} people.")
    else:
        print("--- Generating groups... ---")
        group_number = 1
        
        # --- El bucle WHILE ---
        # "Mientras la cantidad de gente que queda sea mayor o igual 
        # al tamaño de grupo que queremos..."
        while len(remaining_people) >= x:
            
            # 1. Escoge un grupo de la gente que QUEDA
            group = random.sample(remaining_people, x)
            
            print(f"Group {group_number}: {group}")
            
            # 2. Actualiza la lista de gente que queda
            # Esto crea una nueva lista solo con las personas
            # que NO estaban en el 'group' que acabamos de crear.
            remaining_people = [p for p in remaining_people if p not in group]
            
            # 3. Incrementa el contador del grupo
            group_number += 1

        # --- Fin del bucle ---
        # Cuando el bucle termina, imprimimos los que sobraron.
        print("--- Process finished ---")
        if remaining_people:
            print(f"\nYet to be assigned: {remaining_people}")
        else:
            print("\nEveryone was assigned to a group!")

except ValueError:
    print("Error: Please enter a valid number.")