from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

# Heuristica Manhatan
# def heuristica(celda,objetivo):
#    distanciax = abs(objetivo[0] - celda[0])
#    distanciay = abs(objetivo[1] - celda[1])
#    distancia = distanciax + distanciay
#    return distancia

# Heuristica euclidia: Se decidió usar esta función ya que visita menos nodos y es mas eficiente
def heuristica(celda,objetivo):
     distanciax = abs(objetivo[0] - celda[0])
     distanciay = abs(objetivo[1] - celda[1])
     distancia = (distanciax**2 + distanciay**2)**0.5
     return distancia

class AStarSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using A* Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)
        # Initialize the frontier with the initial node as a PriorityQueue
        frontier = PriorityQueueFrontier()

        # Se añade el nodo con la suma del costo heuristico y costo del nodo
        frontier.add(node,heuristica(grid.start,grid.end)+node.cost)
        # Se inicializa el diccionario alcanzados
        alcanzados = {}
        # Se guarda el nodo raíz
        alcanzados[node.state] = node.cost

        while True:
            #  Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(alcanzados)

            # Remove a node from the frontier
            node = frontier.pop()

            # Se verifica si el nodo es solución
            if node.state == grid.end:
                return Solution(node, alcanzados)

            # Se obtienen los vecinos
            successors = grid.get_neighbours(node.state)

            # Se recorre succesors para obtener las acciones 
            for m in successors:
                # Se obtiene el nuevo estado
                new_state = successors[m]

                # Se calcula el costo
                costo = node.cost + grid.get_cost(new_state)
                # Se verifica que el nuevo estado no se encuentre en alcanzados 
                # o que pueda mejorar su costo
                if new_state not in alcanzados or costo < alcanzados[new_state]:
                    # Initialize the son node
                    new_node = Node("", new_state, costo, parent=node, action=m)
                    # Se asigna el nuevo costo
                    alcanzados[new_node.state] = costo
                    
                    # Se calcula la suma del costo heuristico y el costo del nodo
                    costo = heuristica(new_node.state,grid.end)+new_node.cost
                    # Add the new node to the frontier
                    frontier.add(new_node,costo)