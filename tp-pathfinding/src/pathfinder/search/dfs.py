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

        #Comprobamos que el nodo raiz sea solución
        if node.state == grid.end:
            return Solution(new_node, expandidos)
        
        # Add the node to the explored dictionary
        # nodo raiz no alo agregamos a expandidos, 
        # solo se agrega a expandidos los nodos que removemos de la frontera
        #expandidos[node.state] = True

        frontier = StackFrontier()
        frontier.add(node)





        while True:

            #  Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(expandidos)

            # Remove a node from the frontier
            node = frontier.remove()

            if node.state in expandidos:
                continue

            expandidos[node.state] = True


            # Go right
            successors = grid.get_neighbours(node.state)

            #Recorremos succesors para obtener las acciones 

            for m in successors:
                
                new_state = successors[m]
            
                #if new_state not in expandidos:

                        # Initialize the son node
                new_node = Node("", new_state,
                                node.cost + grid.get_cost(new_state),
                                parent=node, action=m)

                if new_node.state not in expandidos:

                # Return if the node contains a goal state
                # In this example, the goal test is run
                # before adding a new node to the frontier
                    if new_state == grid.end:
                        return Solution(new_node, expandidos)




                # Mark the successor as expandidos
                #expandidos[new_state] = True

                # Add the new node to the frontier
                frontier.add(new_node)
                #print(expandidos)
                        
# PREGUNTAR: SI EL ORDEN EN QUE VISITA LOS NODOS ES CORECTO PARA DFS

        
