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

        # Initialize the frontier with the initial node
        # In this example, the frontier is a queue
        frontier = PriorityQueueFrontier()
        frontier.add(node)
        alcanzados = {}
        alcanzados[node.state] = node.cost



        while True:

            #count += 1


            #  Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(alcanzados)

            # Remove a node from the frontier
            node = frontier.pop()
            #print('pop: ',node)

            if node.state == grid.end:
                return Solution(node, alcanzados)

            # Go right
            successors = grid.get_neighbours(node.state)

            #Recorremos succesors para obtener las acciones 


            for m in successors:


                # Obtenemos nuevo estado
                # s' = 
                new_state = successors[m]


                # Calculamos costo
                costo = node.cost + grid.get_cost(new_state)



                if new_state not in alcanzados or costo < alcanzados[new_state]:
                    # Initialize the son node
                    #n' = (...)
                    new_node = Node("", new_state, costo, parent=node, action=m)

                    alcanzados[new_node.state] = costo
                    
                    #alcanzados[new_node.state] = new_node.cost




                    # Add the new node to the frontier
                    frontier.add(new_node,costo)

# PREGUNTAR: VALIDAR EL COMPORTAMIENTO EN PRUEBAS CON DISTINTAS PONDERACIONES





















