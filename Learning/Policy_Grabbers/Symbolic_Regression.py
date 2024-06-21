#https://github.com/MilesCranmer/PySR
#https://arxiv.org/pdf/2305.01582.pdf

import pysr
from pysr import PySRRegressor
from Testing.Configuration import test_metrics
from matplotlib import pyplot as plt 


class symbolic_reg:
    
    #Initializing Values
    def __init__(self):
        testing_values = test_metrics()
        
        self.niterations = testing_values.iterations
        self.binary_operators = testing_values.binary_operators
        self.unary_operators = testing_values.unary_operators
        self.complexity = testing_values.complexity
    
    
    def symbolic_regression(self,features, predictions):

        if features.is_cuda:
            features = features.to('cuda:0')

        if predictions.is_cuda:
            predictions = predictions.to('cuda:0')

        model = PySRRegressor(
        maxsize=self.complexity,
        niterations=self.niterations,
        binary_operators=self.binary_operators,
        unary_operators=self.unary_operators,
        extra_sympy_mappings={"inv": lambda x: 1 / x},
        progress=False,
        verbosity=0,
        elementwise_loss="loss(prediction, target) = (prediction - target)^2",
        # ^ Custom loss function (julia syntax)
        equation_file="Logfile/Logoutput/Logoutput.csv",
        populations= 1,
        constraints={'pow': (-1, 1)}    #says that power laws can have any complexity left argument, but only 1 complexity in the right argument. Use this to force more interpretable solutions.
        )
        
        model.fit(features, predictions)
        
        found_prediction = model.predict(features)
        
        #print("Predictions", type(found_prediction))
        
        return found_prediction