# mira.py
# -------
import math

# Mira implementation
import DataLoad
import util

PRINT = True

class MiraClassifier:
    """
    Mira classifier.

    Note that the variable 'datum' in this code refers to a counter of features
    (not to a raw samples.Datum).
    """
    def __init__( self, legalLabels, max_iterations):
        self.legalLabels = legalLabels
        self.type = "mira"
        self.automaticTuning = False
        self.C = 0.001
        self.max_iterations = max_iterations
        self.initializeWeightsToZero()

    def initializeWeightsToZero(self):
        "Resets the weights of each label to zero vectors"
        self.weights = {}
        for label in self.legalLabels:
            self.weights[label] = util.Counter() # this is the data-structure you should use

    def train(self, trainingData, trainingLabels, validationData, validationLabels):
        "Outside shell to call your method. Do not modify this method."

        if (self.automaticTuning):
            Cgrid = [0.002, 0.004, 0.008]
        else:
            Cgrid = [self.C]

        return self.trainAndTune(trainingData, trainingLabels, validationData, validationLabels, Cgrid)

    
    
    
    def trainAndTune(self, trainingData, trainingLabels, validationData, validationLabels, Cgrid):
        
       
        # DO NOT ZERO OUT YOUR WEIGHTS BEFORE STARTING TRAINING, OR
        # THE AUTOGRADER WILL LIKELY DEDUCT POINTS.
        
        
        trainingData=DataLoad.loadTrainingData()
        validationData=DataLoad.loadValidationData()
        trainingLabels=DataLoad.loadTrainingLabels()
        validationLabels=DataLoad.loadValidationLabels()

        print("trainingData:", len(trainingData))
        print("trainingLabels:", len(trainingLabels))
        print("validationData:", len(validationData))
        print("validationLabels:", len(validationLabels))

        self.features = trainingData[0].keys()

        newWeights = self.weights.copy()
        listaPesos = []
        for c in Cgrid:
            self.weights = newWeights.copy()
            for iteration in range(self.max_iterations):
                print ("Starting iteration ", iteration, "...")
                for index in range(len(trainingData)):
                    weightIndex = 0
                    maximumScore = -math.inf
                    for j in range(len(self.weights)):
                        suma = 0
                        for i in trainingData[index]:
                            suma += trainingData[index].get(i) * self.weights[j][i]
                        if maximumScore < suma:
                            maximumScore = suma
                            weightIndex = j
                    if weightIndex != trainingLabels[index]:
                        for i in trainingData[index]:
                            t=min(((self.weights[weightIndex][i]-self.weights[trainingLabels[index]][i])*trainingData[index].get(i)+1)/2*trainingData[index].get(i)*trainingData[index].get(i),c)
                            self.weights[weightIndex][i] -= trainingData[index].get(i)*t
                            self.weights[trainingLabels[index]][i] += trainingData[index].get(i)*t
            listaPesos.append(self.weights.copy())
        maxScore=0
        for peso in listaPesos:
            score=0
            for index in range(len(validationData)):
                    weightIndex = 0
                    maximumScore = -math.inf
                    for j in range(len(peso)):
                        suma = 0
                        for i in validationData[index]:
                            suma += validationData[index].get(i) * peso[j][i]
                        if maximumScore < suma:
                            maximumScore = suma
                            weightIndex = j
                        if weightIndex == trainingLabels[index]:
                            score+=1
            if score>maxScore:
                maxScore=score
                self.weights=peso.copy()
     
              
    
    
             
    def classify(self, data ):
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


