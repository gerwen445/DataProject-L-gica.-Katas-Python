# PROYECTO LÓGICA: Katas de Python

## Descripción del proyecto

Este proyecto consiste en la resolución de 41 katas de Python. El objetivo es practicar y afianzar los conocimientos básicos del lenguaje, incluyendo tipos de datos, estructuras de datos, condicionales, bucles, funciones, clases y módulos.

---

## Estructura del repositorio

```
📁 proyecto-katas-python/
├── katas_python.py   # Archivo principal con todos los ejercicios resueltos
└── README.md         # Este archivo
```

---

## Pasos seguidos durante el proyecto

### 1. Lectura del enunciado
Lo primero fue leer bien todos los ejercicios para entender qué pedía cada uno. Hay muchos ejercicios que usan `map()`, `filter()` y `reduce()`, así que tuve que repasar cómo funcionan estas funciones antes de empezar.

### 2. Organización
Decidí poner todos los ejercicios en un único archivo `.py`, cada uno encabezado con un comentario con el enunciado, tal como pedía el enunciado del proyecto.

### 3. Resolución de los ejercicios

Fui resolviendo los ejercicios en orden. Estos son los bloques principales que trabajé:

**Ejercicios 1-7 → Funciones básicas y map()**
Los primeros ejercicios me ayudaron a coger soltura con las funciones y con `map()`. El ejercicio 1 (frecuencia de letras) lo resolví con un diccionario y un bucle `for`, que es lo que más controlaba al principio.

**Ejercicios 8, 10, 11, 31 → Manejo de excepciones**
Estos ejercicios me costaron un poco más porque tuve que aprender a crear excepciones personalizadas (ejercicio 10 con `class ListaVaciaError(Exception)`). El uso de `try/except` lo entendí bien con la práctica.

**Ejercicios 9, 14, 16, 18, 19, 20 → filter()**
Con `filter()` la lógica es parecida a `map()` pero en vez de transformar, se filtran elementos. Lo combiné con lambdas para hacerlo más compacto.

**Ejercicios 17, 22, 23, 24 → reduce()**
`reduce()` fue lo que más me costó al principio porque no lo había visto antes. Tuve que importarlo desde `functools`. Una vez entendí que acumula un resultado aplicando una función, los ejercicios fueron más fáciles.

**Ejercicios 15, 19, 21, 26, 33 → Funciones lambda**
Las lambdas son funciones anónimas de una línea. Las usé sobre todo en combinación con `map()` y `filter()`.

**Ejercicio 6 → Recursividad**
El factorial recursivo lo entendí bien con el caso base (`n == 0` o `n == 1`) y la llamada a sí misma.

**Ejercicios 34 y 36 → Clases y POO**
La parte de clases fue la que más tiempo me llevó. Para la clase `Arbol` tuve que pensar bien cómo gestionar la lista de ramas con índices. Para `UsuarioBanco` lo más importante fue controlar los errores al retirar o transferir dinero. Al ejecutar el caso de uso del ejercicio 36 me sale un error porque Bob no tiene saldo suficiente para transferir 80€ (solo tiene 70€ tras agregarle 20), pero la clase en sí funciona correctamente y lanza la excepción como se pide.

**Ejercicio 37 → Funciones de orden superior**
Este ejercicio me gustó porque combinaba varias funciones dentro de una función principal (`procesar_texto`). Usé `*args` para pasar un número variable de argumentos según la opción elegida.

**Ejercicios 38, 39, 40, 41 → Condicionales**
Los últimos ejercicios fueron los más directos. El ejercicio 40 de calcular áreas lo resolví con `if/elif` y usando el módulo `math` para el número π.

### 4. Pruebas
Fui probando cada función a medida que la escribía. Para los ejercicios que pedían `input()` del usuario (8, 11, 31, 41), los dejé definidos pero sin ejecutar, ya que en el archivo `.py` no tienen sentido sin interacción del usuario.

---

## Conceptos demostrados

| Concepto | Ejercicios |
|---|---|
| Tipos de datos básicos y funciones incorporadas | 1, 25, 29, 30 |
| Estructuras de datos (listas, diccionarios, tuplas) | 1, 3, 7, 13, 18, 28, 32 |
| Condicionales | 38, 39, 40, 41 |
| Estructuras de iteración | 1, 3, 28, 34 |
| Funciones (map, filter, reduce, lambda) | 2, 4, 7, 9, 12, 14, 15, 16, 17, 19, 20, 21, 22, 23, 24, 26, 33 |
| Recursividad | 6 |
| Manejo de excepciones | 8, 10, 11, 31, 36 |
| Clases y POO | 34, 36 |
| Módulos (functools, math) | 17, 22, 23, 24, 40 |
| Buenas prácticas (comentarios, nombres descriptivos) | Todos |

---

## Requisitos

- Python 3.x
- No se necesitan librerías externas (solo `functools` y `math`, que vienen con Python)

## Cómo ejecutar

```bash
python katas_python.py
```
