# monty-hall-paradox
### Paradoja>

Tenes **3 puertas** en las cuales una de ellas contiene un premio:

Tu objetivo es elegir la puerta correcta. Elegis una puerta al azar, y yo (que se donde esta el premio) te abro una puerta de **las dos** que quedan mostrandote que el premio no se encuentra en una de ellas.. por lo tanto, te quedan 2 puertas: **la que elegiste principalmente** y la **otra**.. te doy la chance de cambiar de puerta.

Si pensas que es mejor quedarse con la puerta que elegiste, o pensas que da lo mismo puesto que es una probabilidad de **50 - 50**: 
**Bienvenido, estas dentro del 95% de la gente, la cual esta equivocada**.

Al cambiar de puerta, **DUPLICAS** tus chances de ganar, hay incontables formas de probar esto.. pero la mas sencilla para el comun de las personas es por conteo: contar en cuantos casos (al azar) , ganas cambiando de puerta.
Tal vez genera confusion pensarlo con 3 puertas, por un tema de sentido comun y tambien porque a pesar de que la probabilidad de que aciertes habiendo 3 puertas es **1/3** (0.33) , lo cual no es tan baja proporcionalmente, y podria pasar que con tal vez 10 casos, tu resultado quedandonte con la puerta que elegiste supere al resultado cambiando de puerta, aunque es simplemente por suerte y por sus pocos casos.. por eso te propongo probar mi algoritmo probando con miles de casos, y viendo la diferencia abismal en los resultados.

Podes leer mas sobre la [Paradoja de Monty Hall](https://es.wikipedia.org/wiki/Problema_de_Monty_Hall) en cualquier sitio.

Desarrolle un simple algoritmo en **Python**, que simula la situacion con los casos que quieras (obviamente con 3 puertas, puesto que a medida que se incrementen las puertas, menos chances vas a tener de ganar quedandote con tu decision).

Esto surge despues de una discusion un sabado a las *4:05 AM* , al no tener forma de explicar y/o hacer entender a mis amigos.


# Instalacion

 1. clonar el repositorio `git clone https://github.com/guidoenr4/monty-hall-paradox`
 
 2. entrar al directorio `monty-hall-paradox`
 
 3. instalar **`python3`** o cualquier version superior para poder correrlo en una terminal
 
 4. ejecutar el comando **`python3 main.py`** e ingresar un numero entero que corresponda a cuantos casos queres testear.
 
 ```python
#@author: github.com/guidoenr4
#@date: 07-09-2020

import bcolors
from random import randrange

def test_cases(cases):
    changing = 0
    staying = 0
    for i in range(0, cases):
        correct, choice = new_case()
        if not choice == correct : changing+=1
        else : staying+=1
    bcolors.print_green("changing the door: " + str(changing) + " cases" )
    bcolors.print_blue("staying with your decision: " + str(staying) + " cases" )


def new_case():
    return randrange(3), randrange(3)

if __name__ == '__main__':
    bcolors.print_best("MONTY-HALL PARADOX, @author> guidoenr4")
    cases = int(input("insert the cases to test (with 3 doors): "))
    test_cases(cases)
 
 ```
 
 
 
 



