# perceptron.py
# -------------
import random

# Perceptron implementation
import util
import pickle
import DataLoad

PRINT = True


class PerceptronClassifier:
    """
    Perceptron classifier.

    Note that the variable 'datum' in this code refers to a counter of features
    (not to a raw samples.Datum).
    """

    def __init__(self, legalLabels, max_iterations):
        self.legalLabels = legalLabels
        self.type = "perceptron"
        self.max_iterations = 5  # max_iterations
        self.weights = {}
        for label in legalLabels:
            self.weights[label] = util.Counter()  # this is the data-structure you should use

    def setWeights(self, weights):
        assert len(weights) == len(self.legalLabels)
        self.weights = weights

    def train(self, trainingData, trainingLabels, validationData, validationLabels):
        """
        The training loop for the perceptron passes through the training data several
        times and updates the weight vector for each label based on classification errors.
        See the project description for details.

        Use the provided self.weights[label] data structure so that
        the classify method works correctly. Also, recall that a
        datum is a counter from features to values for those features
        (and thus represents a vector a values).
        """
        trainingData = DataLoad.loadTrainingData()
        trainingLabels = DataLoad.loadTrainingLabels()

        self.features = trainingData[0].keys()  # could be useful later

        # initialize weights to 1
        for i in self.weights:
            self.weights[i].incrementAll(self.features, 1)

        # THE AUTOGRADER WILL LIKELY DEDUCT POINTS.
        print("Length trainingData: ", len(trainingData))
        print("Length trainingLabels: ", len(trainingLabels))

        for iteration in range(self.max_iterations):
            print("Starting iteration ", iteration, "...")
            bestWeight = 0
            for index in range(len(trainingData)):
                for i in trainingData[index]:
                    sum = []
                    for j in range(len(self.weights)):
                        sum.append(trainingData[index].get(i) * self.weights[j][i])
                    bestWeight = max(enumerate(sum), key=lambda x: x[1])
                    # update weights
                    if bestWeight[0] != trainingLabels[index]:
                        self.weights[bestWeight[0]][i] -= bestWeight[1]
                        self.weights[trainingLabels[index]][i] += bestWeight[1]

    def classify(self, data):
        """
        Classifies each datum as the label that most closely matches the prototype vector
        for that label.  See the project description for details.

        Recall that a datum is a util.counter...
        """

        data = DataLoad.loadValidationData()

        guesses = []
        for i in range(len(data)):
            scores = util.Counter()
            for label in self.legalLabels:
                scores[label] = self.weights[label] * data[i]
            guesses.append(scores.argMax())
        return guesses

        return guesses
