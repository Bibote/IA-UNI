# search.py

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).
    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state
        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state
        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take
        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.
    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.
    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    visitados = []
    pila = util.Stack()
    pila.push((problem.getStartState(), []))
    while not pila.isEmpty():
        nodo, accion = pila.pop()
        if nodo not in visitados:
            visitados.append(nodo)
            if problem.isGoalState(nodo):
                return accion
            for hijo, accion_hijo, coste in problem.getSuccessors(nodo):
                pila.push((hijo, accion + [accion_hijo]))


def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    visitados = []
    cola = util.Queue()
    cola.push((problem.getStartState(), []))
    while not cola.isEmpty():
        nodo, accion = cola.pop()
        if nodo not in visitados:
            print(nodo)
            visitados.append(nodo)
            if problem.isGoalState(nodo):
                return accion
            for hijo, accion_hijo, coste in problem.getSuccessors(nodo):
                cola.push((hijo, accion + [accion_hijo]))

def myFunc(e):
  return e[-1]
def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    visitados = []
    lista = []
    lista.append((problem.getStartState(), [],0))
    while not len(lista)==0:
        nodo, accion, coste = lista.pop()
        if nodo not in visitados:  
            visitados.append(nodo)
            if problem.isGoalState(nodo):
                return accion
            for hijo, accion_hijo, coste_hijo in problem.getSuccessors(nodo):
                lista.append((hijo, accion+[accion_hijo],coste+coste_hijo))
            lista.sort(reverse=True,key=myFunc)

                

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0
def sumCosteHeuristico(nodo):
    return nodo[-1]+ nodo[-2]

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    visitados = []
    lista = []
    lista.append((problem.getStartState(), [],0,heuristic(problem.getStartState(),problem)))
    while not len(lista)==0:
        nodo, accion, coste,costeHeuristico = lista.pop()
        if nodo not in visitados:  
            visitados.append(nodo)
            if problem.isGoalState(nodo):
                return accion
            for hijo, accion_hijo, coste_hijo in problem.getSuccessors(nodo):
                if(hijo not in visitados):
                    lista.append((hijo, accion+[accion_hijo],coste+coste_hijo,heuristic(hijo,problem)))
            lista.sort(reverse=True,key=sumCosteHeuristico)

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch