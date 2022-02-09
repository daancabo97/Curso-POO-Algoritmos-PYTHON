# INTRODUCCION A LA COMPLEJIDAD ALGORITMICA

      # Se define con una funcion que se puede llamar t que recibe un input que se puede llamar n :T(n)

# -> APROXIMIDACIONES:

      # Cronometrar el tiempo en el que corre un algoritmo
      # Contar los pasos con una medidad abstracta de operacion
      # Contar los pasos conforme nos aproximamos al infinito
 

 # EJM

import time                             # -> Importar time

def factorial(n):                      
    respuesta = 1
    while n > 1:                      
       respuesta *= n                   # -> Mientras n sea mayor a 1 multiplique respuesta por n
       n -= 1                           # -> y que n sea cada vez mas pequeño
    return respuesta                    # -> Regresar la respuesta


def factorial_r(n):
    if n == 1:                          # -> si n es igual a 1 regresara 1
          return 1
    return n * factorial( n- 1)         # -> si no lo es regresara n por el fatorial de n - 1

if __name__ == "__main__":
    n = 1000

    comienzo = time.time()              # Comienzo es igual a time con la funcion time , se mide el tiempo
    factorial(n)                        # Imprimir cual es el factorial de n
        # print(factorial(n)) 
    final = time.time()                 # Definir que el final es igual a time.time()
    print(final -comienzo)              # medir el tiempo de ejecucion de un algoritmo 

    comienzo = time.time()
    (factorial_r(n))
        # print(factorial_r(n))
    final = time.time()
    print(final -comienzo)











