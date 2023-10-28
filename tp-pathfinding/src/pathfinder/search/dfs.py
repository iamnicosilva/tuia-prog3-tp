from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points
            
        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", grid.start, 0)

        # Initialize the explored dictionary to be empty
        expandidos = {} 

        # Se comprueba si el nodo raiz es solución y se retorna
        if node.state == grid.end:
            return Solution(new_node, expandidos)
        
        # Se inicializa la frontera como una pila
        frontier = StackFrontier()
        # Se añade un nuevo nodo raíz
        frontier.add(node)

        while True:
            #  Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(expandidos)

            # Remove a node from the frontier
            node = frontier.remove()

            # Si el nodo esta en expandidos saltea la iteración
            if node.state in expandidos:
                continue
            # Sino se agrega a expandidos
            expandidos[node.state] = True

            # Se obtienen los vecinos
            successors = grid.get_neighbours(node.state)

            #Recorremos succesors para obtener las acciones 
            for m in successors:
                new_state = successors[m]
            
                # Initialize the son node
                new_node = Node("", new_state,
                                node.cost + grid.get_cost(new_state),
                                parent=node, action=m)

                # Se verifica que el estado del nuevo nodo no esta en expandidos
                if new_node.state not in expandidos:
                # Return if the node contains a goal state
                    if new_state == grid.end:
                        return Solution(new_node, expandidos)
                    
                # Si el nuevo estado no es solución se añade a la frontera
                frontier.add(new_node)

        
