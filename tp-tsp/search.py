"""Este modulo define la clase LocalSearch.

LocalSearch representa un algoritmo de busqueda local general.

Las subclases que se encuentran en este modulo son:

* HillClimbing: algoritmo de ascension de colinas. Se mueve al sucesor con
mejor valor objetivo, y los empates se resuelvan de forma aleatoria.
Ya viene implementado.

* HillClimbingReset: algoritmo de ascension de colinas de reinicio aleatorio.
No viene implementado, se debe completar.

* Tabu: algoritmo de busqueda tabu.
No viene implementado, se debe completar.
"""


from __future__ import annotations
from problem import OptProblem
from random import choice
from time import time


class LocalSearch:
    """Clase que representa un algoritmo de busqueda local general."""

    def __init__(self) -> None:
        """Construye una instancia de la clase."""
        self.niters = 0  # Numero de iteraciones totales
        self.time = 0  # Tiempo de ejecucion
        self.tour = []  # Solucion, inicialmente vacia
        self.value = None  # Valor objetivo de la solucion

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion."""
        self.tour = problem.init
        self.value = problem.obj_val(problem.init)


class HillClimbing(LocalSearch):
    """Clase que representa un algoritmo de ascension de colinas.

    En cada iteracion se mueve al estado sucesor con mejor valor objetivo.
    El criterio de parada es alcanzar un optimo local.
    """

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con ascension de colinas.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Arrancamos del estado inicial
        actual = problem.init
        value = problem.obj_val(problem.init)

        while True:

            # Determinar las acciones que se pueden aplicar
            # y las diferencias en valor objetivo que resultan
            diff = problem.val_diff(actual)

            # Buscar las acciones que generan el mayor incremento de valor obj
            max_acts = [act for act, val in diff.items() if val ==
                        max(diff.values())]

            # Elegir una accion aleatoria
            act = choice(max_acts)

            # Retornar si estamos en un optimo local 
            # (diferencia de valor objetivo no positiva)
            if diff[act] <= 0:

                self.tour = actual
                self.value = value
                end = time()
                self.time = end-start
                return

            # Sino, nos movemos al sucesor
            else:

                actual = problem.result(actual, act)
                value = value + diff[act]
                self.niters += 1


class HillClimbingReset(LocalSearch):
    """Algoritmo de ascension de colinas con reinicio aleatorio."""

    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con ascension de colinas.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Arrancamos del estado inicial
        actual = problem.init
        #Valor objetivo
        value = problem.obj_val(problem.init)

        #Posibles soluciones
        soluciones = {}
        restart_count = 0

        while True:

            # Determinar las acciones que se pueden aplicar
            # y las diferencias en valor objetivo que resultan
            diff = problem.val_diff(actual)
            # print('dif: ',diff)
            print('valor: ',value)
            print(actual)

            # LINEA ORIGINAL:
            # Buscar las acciones que generan el mayor incremento de valor obj
            # max_acts = [act for act, val in diff.items() if val == max(diff.values())]

            # CODIGO REESCRITO: 
            # Buscar las acciones que generan el mayor incremento de valor obj
            max_acts = []  # Creamos una lista vacía llamada max_acts

            # Obtenemos el valor máximo en el diccionario diff
            max_value = max(diff.values())

            # Iteramos a través de los elementos del diccionario diff
            for act, val in diff.items():
                # Comprobamos si el valor actual (val) es igual al valor máximo
                if val == max_value:
                    # Si es igual, agregamos la acción (act) a la lista max_acts
                    max_acts.append(act)


            # Elegir una accion aleatoria
            act = choice(max_acts)

            # Retornar si estamos en un optimo local 
            # (diferencia de valor objetivo no positiva)

            if diff[act] <= 0:
                print('diff[act] no positivo: ',diff[act])
                soluciones[value] = actual
                # ACA EN VEZ DE RETORNAR, TENEMOS QUE RESETEAR Y GUARDAR
                # LOS VALORES DE ESTA PSEUDO-SOLUCIÓN PARA DESPUES 
                # PODER QUEDARNOS CON LA MEJOR
                # NECESITAMOS ESTABLECER CUANTAS VECES SE VA A REINICIAR
                # USANDO UN CONTADOR QUE DEPENDA DE LA CANTIDAD DE CIUDADES
                # DEL MAPA
                # soluciones[count] = diff[act],actual,value,time(),end-start

            #Si no se reseteo 10 veces, se resetea y cuenta el reseteo
            # El contador 10 tiene que ser dinamico segun la cant de ciudades.
                if restart_count < 5:
                    actual = problem.random_reset()
                    value = problem.obj_val(actual) #value + diff[act]
                    restart_count +=1
                    continue
            
            #Ya se reseteó al menos 10 veces hay que definir cual es la mejor solucion
                #TOUR: mejor solucion       
                #Buscamos el maximo
                mejor_solucion = max(soluciones)
                self.tour = soluciones[mejor_solucion]
                self.value = mejor_solucion 

                end = time()
                self.time = end-start

                return

            # Sino, nos movemos al sucesor
            else:

                print('diff act ',diff[act])
                actual = problem.result(actual, act)
                value = value + diff[act]
                self.niters += 1



class Tabu(LocalSearch):
    """Algoritmo de busqueda tabu."""
    def solve(self, problem: OptProblem):
        actual = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 0]
        value = problem.obj_val(problem.init)
        start = time()

        self.tour = actual
        self.value = value
        end = time()
        self.time = end-start

        return
