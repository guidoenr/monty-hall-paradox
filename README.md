# monty-hall-paradox
### Paradoja>

Tenes **3 puertas** en las cuales una de ellas contiene un premio, tu objetivo es elegir la correcta. Elegis una puerta al azar, y yo (que se donde esta el premio) te abro una puerta de **las dos** que quedan mostrandote que el premio no se encuentra en una de ellas.. por lo tanto, te quedan 2 puertas: **la que elegiste principalmente** y la **otra**.. te doy la chance de cambiar de puerta.

Si pensas que es mejor quedarse con la puerta que elegiste, o pensas que da lo mismo puesto que es una probabilidad de **50 - 50**: 
**Bienvenido, estas dentro del 95% de la gente, la cual esta equivocada**.

Al cambiar de puerta, **DUPLICAS** tus chances de ganar, hay incontables formas de probar esto.. pero la mas sencilla para el comun de las personas es por conteo: contar en cuantos casos (al azar) , ganas cambiando de puerta.
Tal vez genera confusion pensarlo con 3 puertas, por un tema de sentido comun y tambien porque a pesar de que la probabilidad de que aciertes habiendo 3 puertas es **1/3** , lo cual no es tan baja proporcionalmente, y podria pasar que con tal vez 10 casos, tu resultado quedandonte con la puerta que elegiste supere al resultado cambiando de puerta, aunque es simplemente por suerte y por sus pocos casos.. por eso te propongo probar mi algoritmo probando con millones de casos, y viendo la diferencia abismal en los resultados.

Podes leer mas sobre la [paradoja](https://es.wikipedia.org/wiki/Problema_de_Monty_Hall) en cualquier sitio.

Programe un algoritmo , en python3.8, que simula la situacion con los casos que quieras.


# Instalacion

 1. clonar el repositorio `git clone https://github.com/guidoenr4/monty-hall-paradox`
 
 2. entrar al directorio `monty-hall-paradox`
 
 3. instalar **`python3`** o cualquier version superior para poder correrlo en una terminal
 
 4. ejecutar el comando **`python3 main.py`** e ingresar un numero entero que corresponda a cuantos casos queres testear.
 
 ```python
 
 #@author: github.com/guidoenr4
#@date: 07-09-2020

from random import randrange

def test_cases(cases):
    changin = 0
    staying = 0
    i = 0
    while i < cases:
        doors = new_case()
        correct = get_correct(doors)
        choice = randrange(3)
        if switch(doors, correct, choice):
            changin+=1
        else:
            staying+=1
        i+=1
    print("Changin: " + str(changin) + " cases" )
    print("Staying: " + str(staying) + " cases" )

def switch(doors, correct, choice):
    return not choice == correct

def get_correct(doors):
    i = 0
    for x in doors:
        if x == True:
            return i
        else:
            i+=1

def new_case():
    random = randrange(3)
    doors_array = [False, False, False]
    doors_array[random] = True
    return doors_array

if __name__ == '__main__':
    print("monty hall paradox por guidoti")
    cases = int(input("cases: "))
    test_cases(cases)
 
 ```
 
 
 
 



