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


        # Initialize the explored dictionary to be empty
        #reached = {}
        
        # Add the node to the explored dictionary
        #reached[node.state] = 0
        #eached[node.cost] = 0
        #print(reached)
        
        # return NoSolution(explored)

                # Return if the node contains a goal state
        #if node.state == grid.end:
        #    return Solution(node, reached)


        #count = 0

        while True:

            #count += 1


            #  Fail if the frontier is empty
            if frontier.is_empty():
                return NoSolution(reached)

            # Remove a node from the frontier
            node = frontier.pop()
            #print('pop: ',node)

            if node.state == grid.end:
                return Solution(node, reached)

            # Go right
            successors = grid.get_neighbours(node.state)

            #Recorremos succesors para obtener las acciones 


            #SEGUIR DESDE ACA: QUEREMOS OBTENER EL VECINO CON MENOR COSTO Y SACAR LA ITERACION MAL ORDENADA:
            #costos = {}


            for m in successors:


                new_state = successors[m]


                # Initialize the son node
                new_node = Node("", new_state,
                                node.cost + grid.get_cost(new_state),
                                parent=node, action=m)


                if new_state not in alcanzados or new_node.cost < alcanzados[new_state]:
                    

                    # Return if the node contains a goal state
                    # In this example, the goal test is run
                    # before adding a new node to the frontier


                    # Add the new node to the frontier
                    frontier.add(new_node,5)

                    print(reached)

                    if count == 10:
                        return






















        #return NoSolution(reached)
