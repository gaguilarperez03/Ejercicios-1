#1.1 Escribe una función cuya firma sea multiple(n, m), y que tome dos enteros y devuelva True is n es un múltiplo de m,
# es decir n = m*i, paa una algún entero i, o False en cualquier otro caso.

from asyncio.windows_events import NULL
from cmath import pi
from random import randint

def multiple(n, m):
    valor = 0
    if n % m == 0:
        valor = "True"
    else:
        valor = "False"
    return valor
print(multiple(3, 9))

#1.2  Escribe una función cuya firma sea even(k), y que tome un valor entero y devuelva True is k es par o False en otro caso.

def even(k):
    valor = 0
    if k % 2== 0:
        valor = "True"
    else:
        valor = "False"
    return valor
print(even(2))

#1.3 Escribe una función cuya firma sea minmax(data), y que tome una secuencia de uno o mas números, y que devuelva el máximo y mínimo de la secuencia
# No se puede usar las funciones min o max para implementar la solución.

import random
sequence = [1, 2, 3, 4, 5, 6]
def minimax(sequence):
    minimo = sequence[0]
    maximo = sequence[0]
    for i in sequence:
        if i < minimo:
            minimo = i
        elif i > maximo:
            maximo = i
    valor = [minimo, maximo]


#1.4 Escribe una función  que come una numero entero positivo n y devuelva la suma de los cuadrados  de los cuadrados de todos los enteros positivos 
# menores a n. 
# Ejemplo: n = 5, solución 4**2 + 3**2 + 2**2 + 1**1

def entero_positivo(n):
    valor = 0
    for i in range(n):
        valor += i**2
    return valor
print(entero_positivo(2))

#1.5 Escribe una función que tome un entero positivo y devuelva la suma de los cuadrados de los cuadrados de todos los números impares menores
# a n.
# Ejemplo: n = 7, solución 5**2 + 3**2 + 1**1

def enteropositivo(n):
    valor = 0
    list = []
    for i in range(n):
        list.append(i)
    for i in list:
        if i % 2 != 0:
            valor += i**2
    return valor
print(enteropositivo(2))

#1.6 Python permite utilizar números negativos como indices en un secuencia, tal como un string. Si el string tiene una longitud n, y la expresión
#  s[k] se usa para los indices −n ≤ k < 0, cual es el el indice equivalente  j ≥ 0 tal que s[j] have referencia a los mismos elementos?

secuencia = "123456789"
k = -1
j = len(secuencia) + k
print(secuencia[k], secuencia[j])

#1.7 Cuales son los parámetros que se deben usar en el constructor de la función range para producir los valores, s 50, 60, 70, 80?

n = 50
listas = []
def nums(listas):
    for i in range(n, 81, 10):
        listas.append(i)
    return listas
print(nums(listas))

#1.8 Cuales son los parámetros que se deben usar en el constructor de la función range para producir los valores, 8, 6, 4, 2, 0, −2, −4, −6, −8?

n = 8
listas = []
def nums(listas):
    for i in range(n, -9, -2):
        listas.append(i)
    return listas
print(nums(listas))

#1.9 Escribe una funcion que tome una secuencia de números y determine si todos los números en la secuencia son diferentes.

listas = [2, 4, 6, 8]
def dif(listas):
    valor = 0
    for i in listas:
        for j in listas:
            if i == j:
                valor += 1
        if valor >= 2:
            break
        else:
            valor = 0
    if valor >= 2:
        valor = "True"
    else:
        valor = "False"
    return valor
print(dif(listas))

#1.10 Escribe una función que tome dos listas a y b de longitud n de números enteros, y devuelva el producto escalar de a y b.
# Es decir, devuelva una vector c de longitud n tal que  c[i] = a[i] · b[i], para i = 0,...,n− 1.

list1 = [1, 3, 5]
list2 = [2, 4, 6]
def producto(list1, list2):
    vectorc = [1, 2, 3]
    for i in range(len(list1)):
        vectorc[i] = list1[i]*list2[i]
    return vectorc
print(producto(list1, list2))

# 1.11 Escribe una función que cuente el numero de vocales en una un cadena de caracteres dada.

cadena_caracteres = "que sea ya fin de semana"
def words(string):
    valor = 0
    listas = list(cadena_caracteres)
    for i in listas:
        if i == "a" or i == "e" or i == "i" or i == "0" or i =="u":
            valor += 1
    return valor
print(words(cadena_caracteres))

# 1.12 Identifica el tipo de dato (int, float, string o list) de los siguientes valores literales:
"Hola Mundo" #str    
[1, 10, 100]     #list 
-25      #int        
1.167    #float         
["Hola", "Mundo"]    #list

# 1.13 Realiza un programa que siga las siguientes instrucciones:
#    • Crea un conjunto llamado usuarios con los usuarios Marta, David, Elvira, Juan y Marcos
#    • Crea un conjunto llamado administradores con los administradores Juan y Marta.
#    • Borra al administrador Juan del conjunto de administradores.
#    • Añade a Marcos como un nuevo administrador, pero no lo borres del conjunto de usuarios.
#    • Muestra todos los usuarios por pantalla de forma dinámica, además debes indicar cada usuario es administrador o no.

users = {"Marta", "David", "Elvira", "Juan", "Marcos"}
administradores = {"Juan", "Marta"}
def names(users, administradores):
    administradores.discard("Juan")
    administradores.append("Marcos")
    for i in users:
        if i in administradores:
            print(i + " es un administrador")
        else:
            print(i)
    return
names(users, administradores)
 
# 1.14 Crea un script llamado tabla.py que realice las siguientes tareas:
#    • Debe tomar 2 argumentos, ambos números enteros positivos del 1 al 9, sino mostrará un error.
#    • El primer argumento hará referencia a las filas de una tabla, el segundo a las columnas.
#    • En caso de no recibir uno o ambos argumentos, debe mostrar información acerca de cómo utilizar el script.
#    • El script contendrá un bucle for que itere el número de veces del primer argumento.
#    • Dentro del for, añade un segundo for que itere el número de veces del segundo argumento.
#    • Dentro del segundo for ejecuta una instrucción print(" * ", end=''), (**end=''* evita el salto de línea)*.
#    • Ejecuta el código y observa el resultado.
#    • Intenta deducir dónde y cómo añadir otra instruccion print() para dibujar una tabla.
# 1.15 Localiza el error en el siguiente bloque de código. Crea una excepción para evitar que el programa se bloquee y además explica en un mensaje al usuario la causa y/o solución:
#resultado = 10/0

try:
    10/0
except:
    print("ZeroDivisionError: division by zero, no se puede dividir entre 0 ya que es indeterminado")