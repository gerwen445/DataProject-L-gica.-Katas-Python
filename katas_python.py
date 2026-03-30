# ============================================================
# PROYECTO LÓGICA: Katas de Python
# ============================================================

# Importaciones necesarias para algunos ejercicios
from functools import reduce
import math

# ===========================================================
# Ejercicio 1: Función que recibe una cadena de texto y devuelve
# un diccionario con las frecuencias de cada letra. Los espacios
# no deben ser considerados.
# ===========================================================

def frecuencia_letras(cadena):
    # Primero paso todo a minúsculas para que no haya diferencia entre A y a
    cadena = cadena.lower()
    resultado = {}
    for letra in cadena:
        if letra != " ":  # ignoramos los espacios
            if letra in resultado:
                resultado[letra] += 1
            else:
                resultado[letra] = 1
    return resultado

# Prueba
print("--- Ejercicio 1 ---")
print(frecuencia_letras("Hola Mundo"))


# ===========================================================
# Ejercicio 2: Dada una lista de números, obtén una nueva lista
# con el doble de cada valor. Usa la función map()
# ===========================================================

def doble_lista(numeros):
    return list(map(lambda x: x * 2, numeros))

# Prueba
print("\n--- Ejercicio 2 ---")
print(doble_lista([1, 2, 3, 4, 5]))


# ===========================================================
# Ejercicio 3: Función que tome una lista de palabras y una
# palabra objetivo. Devuelve una lista con las palabras que
# contengan la palabra objetivo.
# ===========================================================

def buscar_palabras(lista_palabras, objetivo):
    resultado = []
    for palabra in lista_palabras:
        if objetivo in palabra:
            resultado.append(palabra)
    return resultado

# Prueba
print("\n--- Ejercicio 3 ---")
palabras = ["manzana", "mandarina", "naranja", "pera", "mango"]
print(buscar_palabras(palabras, "man"))


# ===========================================================
# Ejercicio 4: Función que calcule la diferencia entre los
# valores de dos listas. Usa la función map()
# ===========================================================

def diferencia_listas(lista1, lista2):
    # Uso map para restar elemento a elemento
    return list(map(lambda x, y: x - y, lista1, lista2))

# Prueba
print("\n--- Ejercicio 4 ---")
print(diferencia_listas([10, 20, 30], [1, 5, 10]))


# ===========================================================
# Ejercicio 5: Función que tome una lista de números y un valor
# opcional nota_aprobado (por defecto 5). Calcula la media y
# determina si está aprobado o suspenso. Devuelve una tupla.
# ===========================================================

def calcular_media(numeros, nota_aprobado=5):
    media = sum(numeros) / len(numeros)
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    return (media, estado)

# Prueba
print("\n--- Ejercicio 5 ---")
print(calcular_media([4, 6, 7, 8]))
print(calcular_media([2, 3, 1]))


# ===========================================================
# Ejercicio 6: Función que calcule el factorial de un número
# de manera recursiva.
# ===========================================================

def factorial(n):
    # Caso base: factorial de 0 o 1 es 1
    if n == 0 or n == 1:
        return 1
    # Llamada recursiva
    return n * factorial(n - 1)

# Prueba
print("\n--- Ejercicio 6 ---")
print(factorial(5))
print(factorial(0))


# ===========================================================
# Ejercicio 7: Función que convierta una lista de tuplas a una
# lista de strings. Usa la función map()
# ===========================================================

def tuplas_a_strings(lista_tuplas):
    # Convierto cada tupla a string con str()
    return list(map(str, lista_tuplas))

# Prueba
print("\n--- Ejercicio 7 ---")
print(tuplas_a_strings([(1, 2), (3, 4), (5, 6)]))


# ===========================================================
# Ejercicio 8: Programa que pida dos números e intente dividirlos.
# Maneja excepciones de valor no numérico y división por cero.
# ===========================================================

def division_segura():
    try:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        resultado = num1 / num2
        print(f"La división fue exitosa: {num1} / {num2} = {resultado}")
    except ValueError:
        print("Error: Debes introducir un valor numérico.")
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero.")

# No ejecutamos la función aquí porque pide input
# division_segura()
print("\n--- Ejercicio 8 ---")
print("Función division_segura() definida (requiere input del usuario)")


# ===========================================================
# Ejercicio 9: Función que tome una lista de mascotas y devuelva
# una nueva lista excluyendo las mascotas prohibidas en España.
# Usa la función filter()
# ===========================================================

def filtrar_mascotas(lista_mascotas):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    # Filtro las mascotas que NO están en la lista de prohibidas
    return list(filter(lambda mascota: mascota not in prohibidas, lista_mascotas))

# Prueba
print("\n--- Ejercicio 9 ---")
mis_mascotas = ["Perro", "Gato", "Mapache", "Tigre", "Conejo", "Oso"]
print(filtrar_mascotas(mis_mascotas))


# ===========================================================
# Ejercicio 10: Función que reciba una lista de números y
# calcule su promedio. Si la lista está vacía, lanza una
# excepción personalizada.
# ===========================================================

class ListaVaciaError(Exception):
    # Excepción personalizada para cuando la lista está vacía
    pass

def promedio_lista(numeros):
    if len(numeros) == 0:
        raise ListaVaciaError("Error: la lista está vacía, no se puede calcular el promedio.")
    return sum(numeros) / len(numeros)

# Prueba
print("\n--- Ejercicio 10 ---")
try:
    print(promedio_lista([1, 2, 3, 4]))
    print(promedio_lista([]))
except ListaVaciaError as e:
    print(e)


# ===========================================================
# Ejercicio 11: Programa que pida la edad al usuario. Maneja
# excepciones de valor no numérico y fuera de rango (0-120).
# ===========================================================

def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 120:
            raise ValueError("La edad debe estar entre 0 y 120.")
        print(f"Tu edad es: {edad}")
    except ValueError as e:
        print(f"Error: {e}")

# No ejecutamos porque pide input
print("\n--- Ejercicio 11 ---")
print("Función pedir_edad() definida (requiere input del usuario)")


# ===========================================================
# Ejercicio 12: Función que al recibir una frase devuelva una
# lista con la longitud de cada palabra. Usa la función map()
# ===========================================================

def longitud_palabras(frase):
    palabras = frase.split()
    return list(map(len, palabras))

# Prueba
print("\n--- Ejercicio 12 ---")
print(longitud_palabras("Hola me llamo Python"))


# ===========================================================
# Ejercicio 13: Función que para un conjunto de caracteres
# devuelva una lista de tuplas con cada letra en mayúsculas y
# minúsculas. Sin letras repetidas. Usa la función map()
# ===========================================================

def mayusculas_minusculas(caracteres):
    # Paso todo a minúsculas primero para detectar bien los duplicados
    # y luego elimino con set para no repetir letras
    sin_repetidos = list(set(caracteres.lower()))
    return list(map(lambda c: (c.upper(), c.lower()), sin_repetidos))

# Prueba
print("\n--- Ejercicio 13 ---")
print(mayusculas_minusculas("aAbBcC"))


# ===========================================================
# Ejercicio 14: Función que retorne las palabras de una lista
# que comiencen con una letra específica. Usa la función filter()
# ===========================================================

def palabras_con_letra(lista_palabras, letra):
    # Comparo en minúsculas para que no importa si es mayúscula o minúscula
    return list(filter(lambda p: p.lower().startswith(letra.lower()), lista_palabras))

# Prueba
print("\n--- Ejercicio 14 ---")
print(palabras_con_letra(["manzana", "pera", "melón", "uva", "melocotón"], "m"))


# ===========================================================
# Ejercicio 15: Función lambda que sume 3 a cada número
# de una lista dada.
# ===========================================================

# Creo la lambda y la aplico con map
sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))

# Prueba
print("\n--- Ejercicio 15 ---")
print(sumar_tres([1, 2, 3, 4, 5]))


# ===========================================================
# Ejercicio 16: Función que tome una cadena de texto y un número
# n y devuelva las palabras más largas que n. Usa filter()
# ===========================================================

def palabras_mas_largas(cadena, n):
    palabras = cadena.split()
    return list(filter(lambda p: len(p) > n, palabras))

# Prueba
print("\n--- Ejercicio 16 ---")
print(palabras_mas_largas("Hola me llamo Python y me gusta programar", 4))


# ===========================================================
# Ejercicio 17: Función que tome una lista de dígitos y devuelva
# el número correspondiente. Ej: [5,7,2] -> 572. Usa reduce()
# ===========================================================

def lista_a_numero(digitos):
    # La idea es ir multiplicando por 10 y sumando el siguiente dígito
    return reduce(lambda acc, x: acc * 10 + x, digitos)

# Prueba
print("\n--- Ejercicio 17 ---")
print(lista_a_numero([5, 7, 2]))
print(lista_a_numero([1, 0, 3]))


# ===========================================================
# Ejercicio 18: Programa que cree una lista de diccionarios con
# info de estudiantes y filtre los que tienen calificación >= 90.
# Usa la función filter()
# ===========================================================

estudiantes = [
    {"nombre": "Ana", "edad": 20, "calificacion": 95},
    {"nombre": "Luis", "edad": 22, "calificacion": 78},
    {"nombre": "Marta", "edad": 19, "calificacion": 88},
    {"nombre": "Carlos", "edad": 21, "calificacion": 91},
    {"nombre": "Sara", "edad": 23, "calificacion": 65},
]

estudiantes_sobresalientes = list(filter(lambda e: e["calificacion"] >= 90, estudiantes))

print("\n--- Ejercicio 18 ---")
print(estudiantes_sobresalientes)


# ===========================================================
# Ejercicio 19: Función lambda que filtre los números impares
# de una lista dada.
# ===========================================================

filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

# Prueba
print("\n--- Ejercicio 19 ---")
print(filtrar_impares([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# ===========================================================
# Ejercicio 20: Para una lista con elementos tipo integer y string
# obtén una nueva lista sólo con los valores int. Usa filter()
# ===========================================================

def solo_enteros(lista):
    # Uso isinstance para comprobar si el elemento es un entero
    return list(filter(lambda x: isinstance(x, int), lista))

# Prueba
print("\n--- Ejercicio 20 ---")
mezcla = [1, "hola", 2, "mundo", 3, 4, "python"]
print(solo_enteros(mezcla))


# ===========================================================
# Ejercicio 21: Función que calcule el cubo de un número dado
# mediante una función lambda.
# ===========================================================

cubo = lambda x: x ** 3

# Prueba
print("\n--- Ejercicio 21 ---")
print(cubo(3))
print(cubo(5))


# ===========================================================
# Ejercicio 22: Dada una lista numérica, obtén el producto total
# de los valores. Usa la función reduce()
# ===========================================================

def producto_total(numeros):
    return reduce(lambda x, y: x * y, numeros)

# Prueba
print("\n--- Ejercicio 22 ---")
print(producto_total([1, 2, 3, 4, 5]))


# ===========================================================
# Ejercicio 23: Concatena una lista de palabras. Usa reduce()
# ===========================================================

def concatenar_palabras(lista_palabras):
    return reduce(lambda a, b: a + " " + b, lista_palabras)

# Prueba
print("\n--- Ejercicio 23 ---")
print(concatenar_palabras(["Hola", "me", "llamo", "Python"]))


# ===========================================================
# Ejercicio 24: Calcula la diferencia total en los valores
# de una lista. Usa la función reduce()
# ===========================================================

def diferencia_total(numeros):
    return reduce(lambda x, y: x - y, numeros)

# Prueba
print("\n--- Ejercicio 24 ---")
print(diferencia_total([100, 10, 5, 3]))


# ===========================================================
# Ejercicio 25: Función que cuente el número de caracteres
# en una cadena de texto dada.
# ===========================================================

def contar_caracteres(cadena):
    return len(cadena)

# Prueba
print("\n--- Ejercicio 25 ---")
print(contar_caracteres("Hola, mundo!"))


# ===========================================================
# Ejercicio 26: Función lambda que calcule el resto de la
# división entre dos números dados.
# ===========================================================

resto_division = lambda a, b: a % b

# Prueba
print("\n--- Ejercicio 26 ---")
print(resto_division(10, 3))
print(resto_division(15, 4))


# ===========================================================
# Ejercicio 27: Función que calcule el promedio de una lista
# de números.
# ===========================================================

def promedio(numeros):
    if len(numeros) == 0:
        return 0
    return sum(numeros) / len(numeros)

# Prueba
print("\n--- Ejercicio 27 ---")
print(promedio([10, 20, 30, 40]))


# ===========================================================
# Ejercicio 28: Función que busque y devuelva el primer
# elemento duplicado en una lista dada.
# ===========================================================

def primer_duplicado(lista):
    vistos = []
    for elemento in lista:
        if elemento in vistos:
            return elemento  # devuelvo el primero que ya he visto antes
        vistos.append(elemento)
    return None  # si no hay duplicados devuelvo None

# Prueba
print("\n--- Ejercicio 28 ---")
print(primer_duplicado([1, 2, 3, 4, 2, 5]))
print(primer_duplicado([1, 2, 3, 4, 5]))


# ===========================================================
# Ejercicio 29: Función que convierta una variable en cadena
# de texto y enmascare todos los caracteres con '#', excepto
# los últimos cuatro.
# ===========================================================

def enmascarar(variable):
    texto = str(variable)
    # Si tiene menos de 4 caracteres, lo devuelvo tal cual
    if len(texto) <= 4:
        return texto
    # Enmascaramos todo menos los últimos 4
    return "#" * (len(texto) - 4) + texto[-4:]

# Prueba
print("\n--- Ejercicio 29 ---")
print(enmascarar(1234567890))
print(enmascarar("mi_contraseña_secreta"))


# ===========================================================
# Ejercicio 30: Función que determine si dos palabras son
# anagramas (formadas por las mismas letras en diferente orden).
# ===========================================================

def son_anagramas(palabra1, palabra2):
    # Ordeno las letras de cada palabra y comparo
    # Paso a minúsculas para no tener problemas con mayúsculas
    return sorted(palabra1.lower()) == sorted(palabra2.lower())

# Prueba
print("\n--- Ejercicio 30 ---")
print(son_anagramas("amor", "roma"))
print(son_anagramas("hola", "mundo"))


# ===========================================================
# Ejercicio 31: Función que solicite al usuario una lista de
# nombres y luego busque un nombre. Si no está, lanza excepción.
# ===========================================================

def buscar_nombre():
    # Pido los nombres separados por coma
    entrada = input("Introduce nombres separados por coma: ")
    lista_nombres = [nombre.strip() for nombre in entrada.split(",")]
    nombre_buscado = input("¿Qué nombre quieres buscar? ")
    
    if nombre_buscado in lista_nombres:
        print(f"El nombre '{nombre_buscado}' fue encontrado en la lista.")
    else:
        raise Exception(f"El nombre '{nombre_buscado}' no está en la lista.")

print("\n--- Ejercicio 31 ---")
print("Función buscar_nombre() definida (requiere input del usuario)")


# ===========================================================
# Ejercicio 32: Función que tome un nombre completo y una lista
# de empleados y devuelva el puesto del empleado.
# ===========================================================

def buscar_empleado(nombre_completo, lista_empleados):
    for empleado in lista_empleados:
        if empleado["nombre"] == nombre_completo:
            return empleado["puesto"]
    return "Esta persona no trabaja aquí."

# Prueba
print("\n--- Ejercicio 32 ---")
empleados = [
    {"nombre": "Ana García", "puesto": "Desarrolladora"},
    {"nombre": "Luis Martínez", "puesto": "Diseñador"},
    {"nombre": "Marta López", "puesto": "Project Manager"},
]
print(buscar_empleado("Ana García", empleados))
print(buscar_empleado("Juan Pérez", empleados))


# ===========================================================
# Ejercicio 33: Función lambda que sume elementos
# correspondientes de dos listas dadas.
# ===========================================================

sumar_listas = lambda l1, l2: list(map(lambda x, y: x + y, l1, l2))

# Prueba
print("\n--- Ejercicio 33 ---")
print(sumar_listas([1, 2, 3], [4, 5, 6]))


# ===========================================================
# Ejercicio 34: Clase Arbol con métodos para manipular la
# estructura del árbol (tronco y ramas).
# ===========================================================

class Arbol:
    def __init__(self):
        # El árbol empieza con tronco de longitud 1 y sin ramas
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        # El tronco crece una unidad
        self.tronco += 1

    def nueva_rama(self):
        # Añado una nueva rama de longitud 1
        self.ramas.append(1)

    def crecer_ramas(self):
        # Todas las ramas crecen una unidad
        # Uso un bucle porque me resulta más claro que una lista por comprensión
        for i in range(len(self.ramas)):
            self.ramas[i] += 1

    def quitar_rama(self, posicion):
        # Elimino la rama en la posición indicada
        if posicion < len(self.ramas):
            self.ramas.pop(posicion)
        else:
            print("Posición no válida, no existe esa rama.")

    def info_arbol(self):
        return {
            "longitud_tronco": self.tronco,
            "numero_ramas": len(self.ramas),
            "longitudes_ramas": self.ramas
        }

# Caso de uso del ejercicio
print("\n--- Ejercicio 34 ---")
mi_arbol = Arbol()                  # 1. Crear un árbol
mi_arbol.crecer_tronco()            # 2. Crecer el tronco una unidad
mi_arbol.nueva_rama()               # 3. Añadir una nueva rama
mi_arbol.crecer_ramas()             # 4. Crecer todas las ramas
mi_arbol.nueva_rama()               # 5. Añadir dos nuevas ramas
mi_arbol.nueva_rama()
mi_arbol.quitar_rama(2)             # 6. Retirar la rama en posición 2
print(mi_arbol.info_arbol())        # 7. Info del árbol


# ===========================================================
# Ejercicio 36: Clase UsuarioBanco con métodos para retirar,
# transferir y agregar dinero.
# ===========================================================

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def retirar_dinero(self, cantidad):
        # Compruebo que tiene cuenta y que tiene saldo suficiente
        if not self.cuenta_corriente:
            raise Exception(f"{self.nombre} no tiene cuenta corriente.")
        if cantidad > self.saldo:
            raise Exception(f"Saldo insuficiente. {self.nombre} tiene {self.saldo}€.")
        self.saldo -= cantidad
        print(f"Se han retirado {cantidad}€ de la cuenta de {self.nombre}. Saldo actual: {self.saldo}€")

    def transferir_dinero(self, otro_usuario, cantidad):
        # El otro usuario es quien envía el dinero
        if not otro_usuario.cuenta_corriente:
            raise Exception(f"{otro_usuario.nombre} no tiene cuenta corriente.")
        if cantidad > otro_usuario.saldo:
            raise Exception(f"Saldo insuficiente en la cuenta de {otro_usuario.nombre}.")
        otro_usuario.saldo -= cantidad
        self.saldo += cantidad
        print(f"Transferencia de {cantidad}€ desde {otro_usuario.nombre} a {self.nombre}. Saldo {self.nombre}: {self.saldo}€")

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad
        print(f"Se han añadido {cantidad}€ a la cuenta de {self.nombre}. Saldo actual: {self.saldo}€")

# Caso de uso
print("\n--- Ejercicio 36 ---")
alicia = UsuarioBanco("Alicia", 100, True)   # 1. Crear usuarios
bob = UsuarioBanco("Bob", 50, True)
bob.agregar_dinero(20)                        # 2. Agregar 20 a Bob
alicia.transferir_dinero(bob, 80)             # 3. Transferir 80 de Bob a Alicia
alicia.retirar_dinero(50)                     # 4. Retirar 50 a Alicia


# ===========================================================
# Ejercicio 37: Función procesar_texto que procesa un texto
# según la opción: contar, reemplazar o eliminar.
# ===========================================================

def contar_palabras(texto):
    # Cuento cuántas veces aparece cada palabra
    palabras = texto.split()
    conteo = {}
    for palabra in palabras:
        palabra = palabra.lower()
        if palabra in conteo:
            conteo[palabra] += 1
        else:
            conteo[palabra] = 1
    return conteo

def reemplazar_palabras(texto, palabra_original, palabra_nueva):
    return texto.replace(palabra_original, palabra_nueva)

def eliminar_palabra(texto, palabra):
    # Divido, filtro la palabra y vuelvo a unir
    palabras = texto.split()
    palabras_filtradas = [p for p in palabras if p.lower() != palabra.lower()]
    return " ".join(palabras_filtradas)

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        # args[0] = palabra original, args[1] = palabra nueva
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])
    else:
        return "Opción no válida. Usa: contar, reemplazar o eliminar."

# Caso de uso
print("\n--- Ejercicio 37 ---")
texto_prueba = "el gato come pescado y el perro come carne y el gato duerme"
print(procesar_texto(texto_prueba, "contar"))
print(procesar_texto(texto_prueba, "reemplazar", "gato", "ratón"))
print(procesar_texto(texto_prueba, "eliminar", "el"))


# ===========================================================
# Ejercicio 38: Programa que diga si es de noche, de día o
# tarde según la hora proporcionada por el usuario.
# ===========================================================

def momento_del_dia(hora):
    if 6 <= hora < 14:
        return "Es de día"
    elif 14 <= hora < 21:
        return "Es tarde"
    elif 21 <= hora <= 23 or 0 <= hora < 6:
        return "Es de noche"
    else:
        return "Hora no válida"

# Prueba
print("\n--- Ejercicio 38 ---")
print(momento_del_dia(10))
print(momento_del_dia(15))
print(momento_del_dia(22))


# ===========================================================
# Ejercicio 39: Programa que determine la calificación en texto
# según la calificación numérica del alumno.
# 0-69: insuficiente, 70-79: bien, 80-89: muy bien, 90-100: excelente
# ===========================================================

def calificacion_texto(nota):
    if 0 <= nota <= 69:
        return "Insuficiente"
    elif 70 <= nota <= 79:
        return "Bien"
    elif 80 <= nota <= 89:
        return "Muy bien"
    elif 90 <= nota <= 100:
        return "Excelente"
    else:
        return "Nota fuera de rango"

# Prueba
print("\n--- Ejercicio 39 ---")
print(calificacion_texto(55))
print(calificacion_texto(75))
print(calificacion_texto(85))
print(calificacion_texto(95))


# ===========================================================
# Ejercicio 40: Función que tome una figura y datos (tupla)
# y calcule el área. Las figuras posibles son: rectangulo,
# circulo y triangulo.
# ===========================================================

def calcular_area(figura, datos):
    if figura == "rectangulo":
        # datos = (base, altura)
        base, altura = datos
        return base * altura
    elif figura == "circulo":
        # datos = (radio,)
        radio = datos[0]
        return math.pi * radio ** 2
    elif figura == "triangulo":
        # datos = (base, altura)
        base, altura = datos
        return (base * altura) / 2
    else:
        return "Figura no reconocida"

# Prueba
print("\n--- Ejercicio 40 ---")
print(calcular_area("rectangulo", (5, 3)))
print(calcular_area("circulo", (4,)))
print(calcular_area("triangulo", (6, 4)))


# ===========================================================
# Ejercicio 41: Programa que calcule el precio final de una
# compra con descuento opcional usando condicionales.
# ===========================================================

def calcular_precio_final():
    try:
        precio = float(input("Introduce el precio original del artículo: "))
        cupon = input("¿Tienes un cupón de descuento? (sí/no): ").strip().lower()

        if cupon == "sí" or cupon == "si":
            descuento = float(input("Introduce el valor del cupón de descuento: "))
            if descuento > 0:
                precio_final = precio - descuento
                print(f"Descuento aplicado de {descuento}€. Precio final: {precio_final}€")
            else:
                print(f"El cupón no es válido. Precio final sin descuento: {precio}€")
        else:
            print(f"Sin descuento. Precio final: {precio}€")
    except ValueError:
        print("Error: Debes introducir un valor numérico.")

print("\n--- Ejercicio 41 ---")
print("Función calcular_precio_final() definida (requiere input del usuario)")
