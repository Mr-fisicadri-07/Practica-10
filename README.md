# 🦁 Adivina el Animal: Juego de Colección en Python

¡Bienvenido a **Adivina el Animal**\! Este es un juego interactivo de consola basado en Python que utiliza **Programación Orientada a Objetos (POO)**. El objetivo es adivinar qué animal emite un sonido específico o tiene cierta característica, ponerle un nombre personalizado y completar tu "Libro de Animales".

## 📋 Descripción

El programa simula un ecosistema con diferentes tipos de animales (Domésticos, Salvajes, Marinos y de Granja). El "Chatbot" selecciona aleatoriamente un animal y reta al usuario a identificarlo basándose en su sonido y una pista sobre su comportamiento.

Si el usuario acierta:

1.  Gana el derecho a ponerle un **nombre propio** al animal.
2.  El animal se añade a su **colección personal (Libro)**.
3.  El animal deja de aparecer en las preguntas futuras (se ha "capturado").

## 🚀 Características

  * **Diversidad de Clases:** Implementación de herencia múltiple categorizada por hábitats.
  * **Sistema de Pistas:** Utiliza atributos únicos (`caracteristica`) para ayudar al usuario.
  * **Mecánica de Colección:** Los animales acertados se guardan en una lista dinámica con nombres personalizados.
  * **Aleatoriedad:** Las preguntas y el orden de las respuestas varían en cada turno.

## 📂 Estructura del Proyecto

El proyecto está modularizado en varios archivos para organizar las clases según los autores y tipos de animales:

| Archivo | Descripción | Responsable/Tipo |
| :--- | :--- | :--- |
| `Chatbot.py` | **Script Principal**. Contiene la lógica del juego, el bucle `while` y la interacción con el usuario. | Main |
| `animales.py` | Contiene la clase padre base `Animal`. | Base |
| `animales_adrian.py` | Subclases de `AnimalesDomesticos` (Perro, Gato, Hamster, etc.). | Adrián |
| `animales_marco.py` | Subclases de `AnimalSalvaje` (León, Mono, Lobo, etc.). | Marco |
| `animales_andrea.py` | Subclases de `AnimalesMarinos` (Delfín, Tiburón, Pulpo, etc.). | Andrea |
| `animales_jorge.py` | Subclases de `AnimalesGranja` (Vaca, Cerdo, Oveja, etc.). | Jorge |

## 🛠️ Conceptos Técnicos Aplicados

Este proyecto es un excelente ejemplo práctico de los pilares de la POO en Python:

  * **Herencia:** Todas las clases heredan de `Animal` o de clases intermedias (ej. `AnimalesMarinos`).
  * **Polimorfismo:** Diferentes objetos responden a los mismos métodos o atributos (como `.sonido` o `.caracteristica`) de manera única.
  * **Super():** Uso de `super().__init__` para gestionar la inicialización de atributos entre clases padres e hijas.
  * **Modularidad:** Importación de clases desde diferentes scripts.

## 💻 Instalación y Ejecución

No se requieren librerías externas (solo utiliza la librería estándar `random`).

1.  **Clona el repositorio** (o descarga los archivos en una misma carpeta):

    ```bash
    git clone <tu-repositorio-url>
    ```

2.  **Ejecuta el juego**:
    Asegúrate de estar en la carpeta del proyecto y corre el siguiente comando en tu terminal:

    ```bash
    python Chatbot.py
    ```

## 🎮 Cómo Jugar

1.  El juego te mostrará un **sonido** (ej. "¡Muu\!") y una **pista** (ej. "Es conocido por dar leche").
2.  Se te presentarán 3 opciones (A, B, C).
3.  Escribe la letra de tu respuesta.
4.  Si aciertas, escribe un nombre divertido para tu nuevo animal.
5.  ¡Intenta coleccionar todos los animales antes de que se acaben\!

-----

*Proyecto desarrollado como práctica de Python y Programación Orientada a Objetos.*