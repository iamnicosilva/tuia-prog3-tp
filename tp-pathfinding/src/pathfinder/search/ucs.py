from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class UniformCostSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Uniform Cost Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the frontier with the initial node as a Priority Queue
        frontier = PriorityQueueFrontier()

        frontier.add(node)

        # Se crea un diccionario
        alcanzados = {}

        # Se asigna el costo al nodo actual
        alcanzados[node.state] = node.cost

        while True:
            #  Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(alcanzados)

            # Remove a node from the frontier
            node = frontier.pop()

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
                    # Add the new node to the frontier
                    frontier.add(new_node,costo)





















