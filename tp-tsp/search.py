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

        # Inicializamos contador de reseteos
        restart_count = 0

        # Se toma la mitad de la cantidad de ciudades para definir el número de reseteos
        # Debido a que es mas performante
        cant_reinicios = (len(actual)/2)

        while True:
            # Determinar las acciones que se pueden aplicar
            # y las diferencias en valor objetivo que resultan
            diff = problem.val_diff(actual)

            # Se crea una lista vacía
            max_acts = []  

            # Se busca las acciones que generan el mayor incremento de valor objetivo
            # Se obtiene el valor máximo en el diccionario diff
            max_value = max(diff.values())

            # Se itera los elementos del diccionario diff
            for act, val in diff.items():
            
            # Se comprueba si el valor actual (val) es igual al valor máximo
                if val == max_value:
            # Si es igual, se agrega la acción (act) a la lista max_acts
                    max_acts.append(act)

            # Se elige una acción aleatoria como criterio de desempate
            # cuando tiene varias opciones igual de óptimas
            act = choice(max_acts)

            # Se verifica si estamos en un óptimo local 
            # (diferencia de valor objetivo no positiva)
            if diff[act] <= 0:
                soluciones[value] = actual
            # Si es un máximo, se define el reseteo o retorno

            # Si no se reseteó X cant de veces: se resetea, cuenta el reseteo
            # y continua a la prox iteración del bucle sin retornar
                if restart_count <= cant_reinicios:
                    # Reseteo:
                    actual = problem.random_reset()
                    # Se asigna el nuevo estado
                    value = problem.obj_val(actual)
                    # Se contabiliza el reseteo
                    restart_count +=1
                    # Se saltea a la siguiente iteración
                    continue
            
            # Ya se reseteó al menos X cant de veces
            # y se define cual es la mejor solución
                # Se busca el máximo
                mejor_solucion = max(soluciones)
                # Se asigna la mejor solucion
                self.tour = soluciones[mejor_solucion]
                # Se asigna el valor de la mejor solución
                self.value = mejor_solucion 

                # Reporta los datos del tiempo de ejecución
                end = time()
                self.time = end-start
                return

            # Si no estamos en un óptimo local, se mueve al sucesor
            else:
                # Se asigna el nuevo estado tras aplicar la mejor acción
                actual = problem.result(actual, act)
                # Se incrementa el costo total del estado
                value = value + diff[act]
                # Se incrementa la iteración
                self.niters += 1

class Tabu(LocalSearch):
    """Algoritmo de busqueda tabu."""
  
    def solve(self, problem: OptProblem):
        """Resuelve un problema de optimizacion con Búsqueda Tabú.

        Argumentos:
        ==========
        problem: OptProblem
            un problema de optimizacion
        """
        # Inicio del reloj
        start = time()

        # Arrancamos del estado inicial
        actual = problem.init
        mejor = actual

        # Se inicializa la lista de memoria de corto plazo
        tabu = []

        # Valor objetivo
        value = problem.obj_val(problem.init)

        # Criterio de parada por iteraciones totales:
        # Se calcula el minimo entre la cantidad de ciudades*20 o 1000 como límite 
        total_iter= min(len(actual)*20,1000)

        # Límite de longitud de memoria de corto plazo
        # Se calcula el minimo entre el doble de la cantidad de ciudades o 100 como límite 
        total_tabu= min(len(actual)*2,100)
        
        # Se itera mientras que el número de iteraciones sea menor que el Criterio de parada
        while self.niters < total_iter:

        # Se inicializa los diccionarios
            no_tabu = {}
            sucesores = {}
            
            # Determinar las acciones que se pueden aplicar y las diferencias
            # en valor objetivo que resultan (OBTENER VECINOS)
            # Posibles_acciones: Clave: tupla (acción)
            # Valor: es la diferencia de Costo respecto al estado actual
            posibles_acciones = problem.val_diff(actual)

            # Se itera entre las posibles acciones para obtener 
            # su estado resultante y se guarda en un diccionario
            for accion in posibles_acciones:
                # SUCESORES:
                # Clave: Accion,  Valor 1: Lista de Estados, Valor 2: Diferencia de Costo  
                sucesores[accion] = problem.result(actual,accion), posibles_acciones[accion]

            # Se itera entre los sucesores para verificar
            for sucesor in sucesores:
                # Si el estado del sucesor no está en los últimos recorridos
                if sucesores[sucesor][0] not in tabu:
                # Se guarda el sucesor en el diccionario no_tabu
                    no_tabu[sucesor] = sucesores[sucesor][0],sucesores[sucesor][1]

            # Se verifica si ya recorrió X cant de estados (elementos en tabu)
            # si se cumple se elimina el estado más antiguo para limpiar memoria
            if self.niters > total_tabu:
                tabu.pop(0)
            
            # SUCESOR (diccionario) 
            # Clave: Accion, Valor 1: Lista de Estado (Orden que recorre las ciudades)
            # Valor 2: Diferencia de Costo 
            mejor_accion = max(no_tabu, key=lambda key: no_tabu[key][1])
            sucesor = no_tabu[mejor_accion][0]

            # Si el sucesor encontrado es más óptimo que el mejor se reemplaza
            if problem.obj_val(mejor) < problem.obj_val(sucesor):
                mejor = sucesor
            
            # Se agrega el sucesor elegido a la lista de los últimos recorridos
            tabu.append(sucesor)
            # Se mueve al sucesor elegido
            actual = sucesor

            # Se incrementa el contador 
            self.niters += 1

        # Se almacena la mejor solución encontrada en self.tour
        self.tour = mejor

        # Se registra el valor objetivo en self.value.
        self.value = problem.obj_val(mejor)

        # Se reporta los datos del tiempo de ejecución
        end = time()
        self.time = end-start
        return
