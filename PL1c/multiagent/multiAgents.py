# multiAgents.py
# --------------
import statistics

from util import manhattanDistance
from game import Directions
import random, util

from game import Agent


class ReflexAgent(Agent):
    """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
    """

    def getAction(self, gameState):
        """
        You do not need to change this method, but you're welcome to.

        getAction chooses among the best options according to the evaluation function.

        Just like in the previous project, getAction takes a GameState and returns
        some Directions.X for some X in the set {NORTH, SOUTH, WEST, EAST, STOP}
        """
        # Collect legal moves and successor states
        legalMoves = gameState.getLegalActions()
        # Choose one of the best actions
        scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        "Add more of your code here if you want to"

        return legalMoves[chosenIndex]

    def evaluationFunction(self, currentGameState, action):
        """
        Design a better evaluation function here.

        The evaluation function takes in the current and proposed successor
        GameStates (pacman.py) and returns a number, where higher numbers are better.

        The code below extracts some useful information from the state, like the
        remaining food (newFood) and Pacman position after moving (newPos).
        newScaredTimes holds the number of moves that each ghost will remain
        scared because of Pacman having eaten a power pellet.

        Print out these variables to see what you're getting, then combine them
        to create a masterful evaluation function.
        """
        # Useful information you can extract from a GameState (pacman.py)
        # pacman should never stop
        if action == "Stop":
            return -1E1000
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        newPos = successorGameState.getPacmanPosition()
        newGhostStates = successorGameState.getGhostStates()
        distanceToMonster = [util.manhattanDistance(newPos, ghost.getPosition()) for ghost in newGhostStates]
        distanceToFood = [- util.manhattanDistance(newPos, food) for food in currentGameState.getFood().asList()]

        run = 0
        if min(distanceToMonster) <= 3:
            run = -1E10

        return max(distanceToFood) + run


def scoreEvaluationFunction(currentGameState):
    """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
    """
    return currentGameState.getScore()


class MultiAgentSearchAgent(Agent):
    """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
    """

    def __init__(self, evalFn='scoreEvaluationFunction', depth='2'):
        self.index = 0  # Pacman is always agent index 0
        self.evaluationFunction = util.lookup(evalFn, globals())
        self.depth = int(depth)


class MinimaxAgent(MultiAgentSearchAgent):
    """
    Your minimax agent (question 2)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action from the current gameState using self.depth
        and self.evaluationFunction.

        Here are some method calls that might be useful when implementing minimax.

        gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

        gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

        gameState.getNumAgents():
        Returns the total number of agents in the game

        gameState.isWin():
        Returns whether or not the game state is a winning state

        gameState.isLose():
        Returns whether or not the game state is a losing state
        """
        "*** YOUR CODE HERE ***"
        # Collect legal moves of pacman
        legalMoves = gameState.getLegalActions(0)
        # Get minimax score
        scores = []
        for action in legalMoves:
            nextGame = gameState.generateSuccessor(0, action)
            scores.append(self.minimaxEvaluation(nextGame, 1, gameState.getNumAgents() * self.depth - 1))
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        return legalMoves[chosenIndex]

    def minimaxEvaluation(self, gameState, currentAgent: int, depth: int):
        # we reached a terminal point
        if (depth <= 0) | gameState.isWin() | gameState.isLose():
            return self.evaluationFunction(gameState)
        else:
            scores = []
            # setter for nextAgent
            newAgent = 0
            if currentAgent != gameState.getNumAgents() - 1:
                newAgent = currentAgent + 1

            for action in gameState.getLegalActions(currentAgent):
                nextGame = gameState.generateSuccessor(currentAgent, action)
                scores.append(self.minimaxEvaluation(nextGame, newAgent, depth - 1))
            # agent 0 == pacman, else ghost
            if currentAgent == 0:
                return max(scores)
            else:
                return min(scores)


class AlphaBetaAgent(MultiAgentSearchAgent):
    """
    Your minimax agent with alpha-beta pruning (question 3)
    """

    def getAction(self, gameState):
        """
        Returns the minimax action using self.depth and self.evaluationFunction
        """
        # Collect legal moves of pacman
        legalMoves = gameState.getLegalActions(0)
        # Get minimax score
        scores = []
        alfa = float("-inf")
        beta = float("inf")
        for action in legalMoves:
            nextGame = gameState.generateSuccessor(0, action)
            score = self.minimaxEvaluation(nextGame, 1, gameState.getNumAgents() * self.depth - 1, alfa, beta)
            scores.append(score)
            alfa = max(alfa, score)
            if beta < alfa:
                break
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        return legalMoves[chosenIndex]

    def minimaxEvaluation(self, gameState, currentAgent: int, depth: int, alfa: float, beta: float):
        # we reached a terminal point
        if (depth <= 0) | gameState.isWin() | gameState.isLose():
            return self.evaluationFunction(gameState)
        else:
            # setter for nextAgent
            newAgent = 0
            if currentAgent != gameState.getNumAgents() - 1:
                newAgent = currentAgent + 1

            scores = []
            for action in gameState.getLegalActions(currentAgent):
                nextGame = gameState.generateSuccessor(currentAgent, action)
                score = self.minimaxEvaluation(nextGame, newAgent, depth - 1, alfa, beta)
                scores.append(score)
                if currentAgent == 0:
                    alfa = max(alfa, score)
                    if beta < score:
                        break
                else:
                    beta = min(beta, score)
                    if alfa > score:
                        break
            # agent 0 == pacman, else ghost
            if currentAgent == 0:
                return max(scores)
            else:
                return min(scores)


class ExpectimaxAgent(MultiAgentSearchAgent):
    """
      Your expectimax agent (question 4)
    """

    def getAction(self, gameState):
        """
        Returns the expectimax action using self.depth and self.evaluationFunction

        All ghosts should be modeled as choosing uniformly at random from their
        legal moves.
        """
        # Collect legal moves of pacman
        legalMoves = gameState.getLegalActions(0)
        # Get minimax score
        scores = []
        for action in legalMoves:
            nextGame = gameState.generateSuccessor(0, action)
            scores.append(self.expectimaxEvaluation(nextGame, 1, gameState.getNumAgents() * self.depth - 1))
        bestScore = max(scores)
        bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
        chosenIndex = random.choice(bestIndices)  # Pick randomly among the best

        return legalMoves[chosenIndex]

    def expectimaxEvaluation(self, gameState, currentAgent: int, depth: int):
        # we reached a terminal point
        if (depth <= 0) | gameState.isWin() | gameState.isLose():
            return self.evaluationFunction(gameState)
        else:
            scores = []
            # setter for nextAgent
            newAgent = 0
            if currentAgent != gameState.getNumAgents() - 1:
                newAgent = currentAgent + 1

            for action in gameState.getLegalActions(currentAgent):
                nextGame = gameState.generateSuccessor(currentAgent, action)
                scores.append(self.expectimaxEvaluation(nextGame, newAgent, depth - 1))
            # agent 0 == pacman, else ghost
            if currentAgent == 0:
                return max(scores)
            else:
                return statistics.mean(scores)


def betterEvaluationFunction(currentGameState):
    """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
    """
    "*** YOUR CODE HERE ***"
    pos = currentGameState.getPacmanPosition()
    ghostStates = currentGameState.getGhostStates()
    distanceToMonster = [util.manhattanDistance(pos, ghost.getPosition()) for ghost in ghostStates]
    distanceToFood = [- util.manhattanDistance(pos, food) for food in currentGameState.getFood().asList()]
    capsules = currentGameState.getCapsules()

    if not distanceToFood:
        distanceToFood = [1E1000]

    run = 0
    if min(distanceToMonster) <= 3:
        run = - 1E10

    return currentGameState.getScore() * 1E1 + max(distanceToFood) - len(capsules) * 1E4 + run


# Abbreviation
better = betterEvaluationFunction
